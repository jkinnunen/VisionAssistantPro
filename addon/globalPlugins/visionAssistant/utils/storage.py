# -*- coding: utf-8 -*-
import hashlib
import json
import logging
import os
import threading
import time

log = logging.getLogger(__name__)

_HISTORY_MAX_ITEMS = 100
_GEMINI_CACHE_MAX_AGE = 48 * 3600
_OCR_TEXT_MAX_ENTRIES = 20
_OCR_TEXT_MAX_PAGES = 2000


class JsonStore:
    def __init__(self, file_path):
        self._file_path = file_path
        self._lock = threading.Lock()

    def _read_all(self):
        if not os.path.exists(self._file_path):
            return {}
        try:
            with open(self._file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                return data
        except Exception:
            pass
        return {}

    def _write_all(self, data):
        try:
            tmp = self._file_path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            os.replace(tmp, self._file_path)
        except Exception as e:
            log.warning(f"Failed to write {self._file_path}: {e}")

    def get(self, key):
        with self._lock:
            return self._read_all().get(key)

    def set(self, key, value):
        with self._lock:
            data = self._read_all()
            data[key] = value
            self._write_all(data)

    def delete(self, key):
        with self._lock:
            data = self._read_all()
            if key in data:
                del data[key]
                self._write_all(data)

    def clear(self):
        with self._lock:
            self._write_all({})


class HistoryStore(JsonStore):
    def load_all(self):
        with self._lock:
            items = [i for i in self._read_all().values() if isinstance(i, dict)]
        return sorted(items, key=lambda i: i.get("timestamp", 0), reverse=True)

    def save(self, item):
        if not isinstance(item, dict) or not item.get("id") or not item.get("type"):
            return
        with self._lock:
            data = self._read_all()
            data[item["id"]] = item
            items = sorted(data.values(), key=lambda i: i.get("timestamp", 0), reverse=True)
            data = {i["id"]: i for i in items[:_HISTORY_MAX_ITEMS]}
            self._write_all(data)

    def delete(self, item_id):
        super().delete(item_id)

    def clear(self, item_type=None):
        with self._lock:
            data = self._read_all()
            if item_type:
                data = {k: v for k, v in data.items() if v.get("type") != item_type}
            else:
                data = {}
            self._write_all(data)


def key_fingerprint(api_key):
    if not api_key:
        return None
    return hashlib.sha256(api_key.encode("utf-8")).hexdigest()[:16]


class GeminiFileCache(JsonStore):
    def get(self, path, api_key):
        entry = super().get(path)
        if not entry:
            return None
        if entry.get("key_fp") != key_fingerprint(api_key):
            return None
        if time.time() - entry.get("uploaded_at", 0) >= _GEMINI_CACHE_MAX_AGE:
            return None
        return entry.get("file_uri")

    def put(self, path, api_key, file_uri):
        self.set(path, {
            "file_uri": file_uri,
            "uploaded_at": time.time(),
            "key_fp": key_fingerprint(api_key),
        })


def file_signature(path):
    try:
        st = os.stat(path)
        return {"mtime": st.st_mtime, "size": st.st_size}
    except Exception:
        return None


class OCRTextCache(JsonStore):
    def get_valid(self, key):
        entry = self.get(key)
        if not entry:
            return None
        files = entry.get("files") or {}
        for path, sig in files.items():
            if file_signature(path) != sig:
                return None
        return entry

    def put(self, key, entry):
        if len(entry.get("pages", {})) > _OCR_TEXT_MAX_PAGES:
            return
        with self._lock:
            data = self._read_all()
            data[key] = entry
            items = sorted(data.items(), key=lambda kv: kv[1].get("timestamp", 0), reverse=True)
            data = dict(items[:_OCR_TEXT_MAX_ENTRIES])
            self._write_all(data)
