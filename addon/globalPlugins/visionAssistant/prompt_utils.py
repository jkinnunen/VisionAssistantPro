# -*- coding: utf-8 -*-
import os
import json
import logging
import re
from functools import wraps

import addonHandler
import config

from . import vision_config

log = logging.getLogger(__name__)

addonHandler.initTranslation()


def _normalize_required_markers(markers):
    if not isinstance(markers, (list, tuple)):
        return []
    normalized = []
    for marker in markers:
        if not isinstance(marker, str):
            continue
        marker = marker.strip()
        if marker and marker not in normalized:
            normalized.append(marker)
    return normalized

def _normalize_required_regex_checks(regex_checks):
    if not isinstance(regex_checks, (list, tuple)):
        return []
    normalized = []
    seen = set()
    for regex_item in regex_checks:
        if isinstance(regex_item, dict):
            pattern = regex_item.get("pattern")
            description = regex_item.get("description")
        else:
            pattern = regex_item
            description = ""
        if not isinstance(pattern, str):
            continue
        pattern = pattern.strip()
        if not pattern or pattern in seen:
            continue
        seen.add(pattern)
        if not isinstance(description, str):
            description = ""
        description = description.strip() or pattern
        normalized.append({"pattern": pattern, "description": description})
    return normalized

def get_builtin_default_prompts():
    builtins = []
    for item in vision_config.DEFAULT_SYSTEM_PROMPTS:
        p = str(item["prompt"]).strip()
        guarded = bool(item.get("guarded"))
        builtins.append({
            "key": item["key"],
            "section": item["section"],
            "label": item["label"],
            "display_label": f"{item['section']} - {item['label']}",
            "internal": bool(item.get("internal")),
            "guarded": guarded,
            "guardedFeatureLabel": str(item.get("guardedFeatureLabel", item["label"])).strip() if guarded else "",
            "requiredMarkers": _normalize_required_markers(item.get("requiredMarkers")),
            "requiredRegex": _normalize_required_regex_checks(item.get("requiredRegex")),
            "prompt": p,
            "default": p,
        })
    return builtins

def get_builtin_default_prompt_map():
    return {item["key"]: item for item in get_builtin_default_prompts()}

def _normalize_custom_prompt_items(items):
    normalized = []
    if not isinstance(items, list):
        return normalized

    for item in items:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        content = item.get("content")
        if not isinstance(name, str) or not isinstance(content, str):
            continue
        name = name.strip()
        content = content.strip()
        if name and content:
            normalized.append({"name": name, "content": content})
    return normalized

def parse_custom_prompts_v2(raw_value):
    if not isinstance(raw_value, str) or not raw_value.strip():
        return None
    try:
        data = json.loads(raw_value)
    except Exception as e:
        log.warning(f"Invalid custom_prompts_v2 config, falling back to legacy format: {e}")
        return None
    return _normalize_custom_prompt_items(data)

def serialize_custom_prompts_v2(items):
    normalized = _normalize_custom_prompt_items(items)
    if not normalized:
        return ""
    return json.dumps(normalized, ensure_ascii=False)

def load_configured_custom_prompts():
    try:
        raw_v2 = config.conf["VisionAssistant"]["custom_prompts_v2"]
    except Exception:
        raw_v2 = ""
    items_v2 = parse_custom_prompts_v2(raw_v2)
    if items_v2 is not None:
        return items_v2
    return []

def _sanitize_default_prompt_overrides(data):
    if not isinstance(data, dict):
        return {}, False

    changed = False
    valid_keys = set(get_builtin_default_prompt_map().keys())
    sanitized = {}
    for key, value in data.items():
        if key not in valid_keys or not isinstance(value, str):
            changed = True
            continue
        prompt_text = value.strip()
        if not prompt_text:
            changed = True
            continue
        if prompt_text != value:
            changed = True
        sanitized[key] = prompt_text
    return sanitized, changed

def load_default_prompt_overrides():
    try:
        raw = config.conf["VisionAssistant"]["default_refine_prompts"]
    except Exception:
        raw = ""
    if not isinstance(raw, str) or not raw.strip():
        return {}

    try:
        data = json.loads(raw)
    except Exception as e:
        log.warning(f"Invalid default_refine_prompts config, using built-ins: {e}")
        return {}

    overrides, _dummy = _sanitize_default_prompt_overrides(data)
    return overrides

def get_configured_default_prompt_map():
    prompt_map = get_builtin_default_prompt_map()
    overrides = load_default_prompt_overrides()
    for key, override in overrides.items():
        if key not in prompt_map:
            continue
        prompt_map[key]["prompt"] = override
    return prompt_map

def get_configured_default_prompts():
    prompt_map = get_configured_default_prompt_map()
    items = []
    for item in vision_config.DEFAULT_SYSTEM_PROMPTS:
        if item.get("internal"):
            continue
        key = item["key"]
        if key in prompt_map:
            items.append(dict(prompt_map[key]))
    items.sort(key=lambda item: item.get("display_label", "").casefold())
    return items

def get_prompt_text(prompt_key):
    prompt_map = get_configured_default_prompt_map()
    item = prompt_map.get(prompt_key)
    if item:
        return item["prompt"]
    return ""

def serialize_default_prompt_overrides(items):
    if not items:
        return ""

    base_map = {item["key"]: item["prompt"] for item in get_builtin_default_prompts()}
    overrides = {}
    for item in items:
        key = item.get("key")
        prompt_text = item.get("prompt", "")
        if key not in base_map:
            continue
        if not isinstance(prompt_text, str):
            continue
        prompt_text = prompt_text.strip()
        if prompt_text and prompt_text != base_map[key]:
            overrides[key] = prompt_text

    if not overrides:
        return ""
    return json.dumps(overrides, ensure_ascii=False)

def get_refine_menu_options():
    options = []
    prompt_map = get_configured_default_prompt_map()
    for key in vision_config.REFINE_PROMPT_KEYS:
        item = prompt_map.get(key)
        if item:
            options.append((item["label"], item["prompt"]))

    for item in load_configured_custom_prompts():
        options.append((item["name"], item["content"]))
    return options

def apply_prompt_template(template, replacements):
    if not isinstance(template, str):
        return ""

    text = template
    for key, value in replacements:
        text = text.replace("{" + key + "}", str(value))

    if "{image_desc_instruction}" in text:
        if config.conf["VisionAssistant"].get("describe_images_ocr", True):
            lang = config.conf["VisionAssistant"]["ai_response_language"]
            desc_text = get_prompt_text("ocr_image_desc_instruction")
            desc_text = desc_text.replace("{response_lang}", lang)
            text = text.replace("{image_desc_instruction}", desc_text)
        else:
            text = text.replace("{image_desc_instruction}", "")

    return text.strip()

def finally_(func, final):
    @wraps(func)
    def new(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            final()
    return new

def clean_markdown(text):
    if not text: return ""
    text = re.sub(r'\*\*|__|[*_]', '', text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'```', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'^\s*-\s+', '', text, flags=re.MULTILINE)
    return text.strip()

def strip_thinking_tags(text):
    if not text: return ""
    text = re.sub(r'\s*<think>.*?</think>\s*', '\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'\s*<reasoning>.*?</reasoning>\s*', '\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'\s*<thought>.*?</thought>\s*', '\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    return text.strip()

def markdown_to_html(text, full_page=False):
    if not text: return ""

    try:
        import markdown as markdown_lib
    except ImportError:
        markdown_lib = None

    html_body = ""
    use_regex_fallback = False

    if markdown_lib:
        try:
            html_body = markdown_lib.markdown(text, extensions=['tables', 'fenced_code'])
        except Exception as e:
            log.error(f"Markdown library failed: {e}")
            use_regex_fallback = True
    else:
        use_regex_fallback = True

    if use_regex_fallback:
        html = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)
        html = re.sub(r'__(.*?)__', r'<b>\1</b>', html)
        html = re.sub(r'^### (.*)', r'<h3>\1</h3>', html, flags=re.M)
        html = re.sub(r'^## (.*)', r'<h2>\1</h2>', html, flags=re.M)
        html = re.sub(r'^# (.*)', r'<h1>\1</h1>', html, flags=re.M)

        lines = html.split('\n')
        in_table = False
        new_lines = []
        table_style = 'border="1" style="border-collapse: collapse; width: 100%; margin-bottom: 10px;"'
        td_style = 'style="padding: 5px; border: 1px solid #ccc;"'

        for line in lines:
            stripped = line.strip()
            if stripped.startswith('|') or (stripped.count('|') > 1 and len(stripped) > 5):
                if not in_table:
                    new_lines.append(f'<table {table_style}>')
                    in_table = True
                if '---' in stripped: continue
                row_content = stripped.strip('|').split('|')
                cells = "".join([f'<td {td_style}>{c.strip()}</td>' for c in row_content])
                new_lines.append(f'<tr>{cells}</tr>')
            else:
                if in_table:
                    new_lines.append('</table>')
                    in_table = False
                if stripped: new_lines.append(line + "<br>")
                else: new_lines.append("<br>")
        if in_table: new_lines.append('</table>')
        html_body = "".join(new_lines)

    if not full_page: return html_body
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>body{{font-family:"Segoe UI",Arial,sans-serif;line-height:1.6;padding:20px;color:#333;max-width:800px;margin:0 auto}}h1,h2,h3{{color:#2c3e50;border-bottom:1px solid #eee;padding-bottom:5px}}pre{{background-color:#f4f4f4;padding:10px;border-radius:5px;overflow-x:auto;font-family:Consolas,monospace}}code{{background-color:#f4f4f4;padding:2px 5px;border-radius:3px;font-family:Consolas,monospace}}table{{border-collapse:collapse;width:100%;margin-bottom:10px}}td,th{{border:1px solid #ccc;padding:8px;text-align:left}}strong,b{{color:#000;font-weight:bold}}li{{margin-bottom:5px}}</style></head><body>{html_body}</body></html>"""
