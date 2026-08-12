# -*- coding: utf-8 -*-
import os
import json
import threading
import logging
import re
import tempfile
import ctypes
import io
import wx
import winUser
import api
from functools import wraps

try:
    import comtypes.client
except ImportError:
    pass

log = logging.getLogger(__name__)

try:
    import fitz
except ImportError:
    fitz = None

try:
    import markdown as markdown_lib
except ImportError:
    markdown_lib = None

from .. import vision_config

class OCRProgressStore:
    _lock = threading.Lock()

    @staticmethod
    def _read_all():
        if not os.path.exists(vision_config.OCR_PROGRESS_FILE):
            return {}
        try:
            with open(vision_config.OCR_PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    @staticmethod
    def _write_all(data):
        try:
            tmp = vision_config.OCR_PROGRESS_FILE + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            os.replace(tmp, vision_config.OCR_PROGRESS_FILE)
        except Exception as e:
            log.error(f"Failed to write OCR progress: {e}")

    @staticmethod
    def save(key, record):
        with OCRProgressStore._lock:
            data = OCRProgressStore._read_all()
            data[key] = record
            OCRProgressStore._write_all(data)

    @staticmethod
    def load(key):
        with OCRProgressStore._lock:
            return OCRProgressStore._read_all().get(key)

    @staticmethod
    def clear(key):
        with OCRProgressStore._lock:
            data = OCRProgressStore._read_all()
            if key in data:
                del data[key]
                OCRProgressStore._write_all(data)


def _is_failed_ocr_page(text):
    if not text:
        return True
    stripped = text.strip()
    return stripped.startswith("[") or stripped.startswith("ERROR:")


def get_focused_explorer_files():
    paths = []
    is_desktop = False
    hwnds = set()

    try:
        for obj_getter in (api.getFocusObject, api.getForegroundObject):
            try:
                obj = obj_getter()
                if obj and getattr(obj, "windowHandle", 0):
                    h = obj.windowHandle
                    hwnds.add(h)
                    try:
                        hwnds.add(winUser.getAncestor(h, winUser.GA_ROOT))
                    except Exception:
                        pass
            except Exception:
                pass

        if not hwnds:
            return []

        for h in hwnds:
            try:
                cls = winUser.getClassName(h)
                if cls in ("Progman", "WorkerW", "SysListView32", "SHELLDLL_DefView"):
                    is_desktop = True
                    break
            except Exception:
                pass

        shell = None
        windows = None
        try:
            shell = comtypes.client.CreateObject("Shell.Application")
            windows = shell.Windows()
            for win in windows:
                doc = None
                selected = None
                try:
                    win_hwnd = getattr(win, "HWND", None)
                    if not win_hwnd:
                        continue

                    is_target = win_hwnd in hwnds
                    if not is_target and is_desktop:
                        try:
                            win_cls = winUser.getClassName(win_hwnd)
                            if win_cls in ("Progman", "WorkerW"):
                                is_target = True
                        except Exception:
                            pass

                    if is_target:
                        doc = win.Document
                        if doc:
                            selected = doc.SelectedItems()
                            if selected and selected.Count > 0:
                                for i in range(selected.Count):
                                    try:
                                        item = selected.Item(i)
                                        p = getattr(item, "Path", "")
                                        if not p and hasattr(item, "Target"):
                                            try:
                                                p = item.Target.Path
                                            except Exception:
                                                pass
                                        if p:
                                            paths.append(p)
                                        del item
                                    except Exception:
                                        continue
                                if paths:
                                    break
                except Exception:
                    continue
                finally:
                    if selected:
                        del selected
                    if doc:
                        del doc
        except Exception:
            pass
        finally:
            if windows:
                del windows
            if shell:
                del shell

        if paths:
            return paths

    except Exception:
        pass

    try:
        ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0x43, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0x43, 0, 2, 0)
        ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)

        for _ in range(5):
            ctypes.windll.kernel32.Sleep(50)
            if wx.TheClipboard.Open():
                try:
                    if wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_FILENAME)):
                        files = wx.FileDataObject()
                        if wx.TheClipboard.GetData(files):
                            paths = list(files.GetFilenames())
                            if paths:
                                break
                finally:
                    wx.TheClipboard.Close()
    except Exception:
        pass

    return paths


class VirtualDocument:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.page_map = [] 
        self.total_pages = 0
        self.is_single_pdf = (len(file_paths) == 1 and file_paths[0].lower().endswith('.pdf'))
        self.single_pdf_path = file_paths[0] if self.is_single_pdf else None

    def scan(self):
        if not fitz: return
        for path in self.file_paths:
            try:
                doc = fitz.open(path)
                count = len(doc)
                for i in range(count):
                    self.page_map.append((path, i))
                doc.close()
            except Exception as e:
                log.error(f"Error scanning file {path}: {e}", exc_info=True)
        self.total_pages = len(self.page_map)

    def get_page_info(self, global_page_index):
        if 0 <= global_page_index < self.total_pages:
            return self.page_map[global_page_index]
        return None, None

    def create_merged_pdf(self, start_page, end_page):
        if not fitz: return None
        try:
            out_doc = fitz.open()
            for i in range(start_page, end_page + 1):
                f_path, f_idx = self.get_page_info(i)
                src_doc = fitz.open(f_path)
                if src_doc.is_pdf:
                    out_doc.insert_pdf(src_doc, from_page=f_idx, to_page=f_idx)
                else:
                    pdf_bytes = src_doc.convert_to_pdf(from_page=f_idx, to_page=f_idx)
                    img_pdf = fitz.open("pdf", pdf_bytes)
                    out_doc.insert_pdf(img_pdf)
                    img_pdf.close()
                src_doc.close()
            
            fd, temp_path = tempfile.mkstemp(suffix=".pdf")
            os.close(fd)
            out_doc.save(temp_path)
            out_doc.close()
            return temp_path
        except Exception as e:
            log.error(f"Error merging PDF: {e}", exc_info=True)
            return None


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
    
    html_body = ""
    use_regex_fallback = False
    
    if markdown_lib:
        try:
            html_body = markdown_lib.markdown(text, extensions=['tables', 'fenced_code'])
        except Exception as e:
            log.warning(f"Markdown library failed: {e}")
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

def convert_json_to_srt_string(json_text, chunk_size=1200, segments=None, global_chars=None):
    def parse_seconds(ts):
        ts_str = str(ts).strip()
        total_seconds = 0.0
        if re.match(r'^\d+(?:[.,]\d+)?$', ts_str):
            try:
                total_seconds = float(ts_str.replace(',', '.'))
            except Exception:
                pass
        else:
            ts_clean = ts_str.replace('.', ',')
            main_time = ts_clean.split(',', 1)[0]
            parts = main_time.split(':')
            try:
                if len(parts) == 2:
                    total_seconds = float(int(parts[0]) * 60 + int(parts[1]))
                elif len(parts) == 3:
                    total_seconds = float(int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2]))
            except Exception:
                pass
        return total_seconds

    def format_srt_time(total_seconds):
        if total_seconds < 0:
            total_seconds = 0.0
        h = int(total_seconds // 3600)
        m = int((total_seconds % 3600) // 60)
        s = int(total_seconds % 60)
        ms = int(round((total_seconds - int(total_seconds)) * 1000))
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    def normalize_timestamp(ts, seg_window=None):
        total_seconds = parse_seconds(ts)
        if seg_window is not None:
            seg_start, seg_end = seg_window
            if total_seconds < seg_start:
                if total_seconds < (seg_end - seg_start + 10):
                    total_seconds += seg_start
                else:
                    total_seconds = seg_start
            if total_seconds > seg_end and seg_end > 0:
                total_seconds = seg_end
        return format_srt_time(total_seconds)

    if isinstance(json_text, list):
        chunks = json_text
    else:
        chunks = [json_text]

    srt_content = ""
    counter = 1
    is_first_subtitle = True

    for chunk_idx, raw_chunk in enumerate(chunks):
        seg_window = None
        if segments and chunk_idx < len(segments):
            sw = segments[chunk_idx]
            if sw and sw[1] is not None and sw[1] > sw[0] >= 0:
                seg_window = sw
        clean_text = raw_chunk.strip()
        
        if "```json" in clean_text.lower():
            try:
                clean_text = re.split(r'```json', clean_text, flags=re.IGNORECASE)[1].split("```")[0].strip()
            except Exception: pass
        elif "```srt" in clean_text.lower():
            try:
                clean_text = re.split(r'```srt', clean_text, flags=re.IGNORECASE)[1].split("```")[0].strip()
            except Exception: pass
        elif "```" in clean_text:
            try:
                clean_text = clean_text.split("```")[1].split("```")[0].strip()
            except Exception: pass

        try:
            data = json.loads(clean_text)
            descriptions = []
            if isinstance(data, list):
                descriptions = data
            elif isinstance(data, dict):
                descriptions = data.get("descriptions", data.get("descriptions_list", []))
            
            for desc in descriptions:
                start_val = desc.get("start")
                end_val = desc.get("end")
                text = desc.get("label", desc.get("text", "")).strip()
                
                if not text:
                    continue
                    
                start = normalize_timestamp(start_val, seg_window)
                end = normalize_timestamp(end_val, seg_window)
                
                if start == "00:00:00,000" and end == "00:00:00,000":
                    continue
                
                if is_first_subtitle and global_chars:
                    text = f"{global_chars.strip()}\n{text}"
                    is_first_subtitle = False
                    
                srt_content += f"{counter}\n{start} --> {end}\n{text}\n\n"
                counter += 1
                
        except Exception:
            blocks = re.findall(r'\{[^{}]*?"start"\s*:[^{}]*?\}', clean_text, re.DOTALL|re.IGNORECASE)
            if blocks:
                for block in blocks:
                    start_m = re.search(r'"start"\s*:\s*"([^"]+)"', block, re.IGNORECASE)
                    end_m = re.search(r'"end"\s*:\s*"([^"]+)"', block, re.IGNORECASE)
                    
                    label_m = re.search(r'"(?:label|text)"\s*:\s*"(.*?)"\s*(?:,|})', block, re.IGNORECASE | re.DOTALL)
                    
                    if start_m and end_m and label_m:
                        start_val = start_m.group(1)
                        end_val = end_m.group(1)
                        text = label_m.group(1).strip().replace('\\"', '"')
                        
                        start = normalize_timestamp(start_val, seg_window)
                        end = normalize_timestamp(end_val, seg_window)
                        
                        if start == "00:00:00,000" and end == "00:00:00,000":
                            continue
                        
                        if is_first_subtitle and global_chars:
                            text = f"{global_chars.strip()}\n{text}"
                            is_first_subtitle = False
                            
                        srt_content += f"{counter}\n{start} --> {end}\n{text}\n\n"
                        counter += 1
            else:
                pattern = r'\[(\d{1,2}:\d{2}(?::\d{2})?)\s*-\s*(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(.*)'
                matches = re.finditer(pattern, clean_text)
                for match in matches:
                    start_time = normalize_timestamp(match.group(1), seg_window)
                    end_time = normalize_timestamp(match.group(2), seg_window)
                    desc_text = match.group(3).strip()
                    
                    if desc_text:
                        if is_first_subtitle and global_chars:
                            desc_text = f"{global_chars.strip()}\n\n{desc_text}"
                            is_first_subtitle = False
                        srt_content += f"{counter}\n{start_time} --> {end_time}\n{desc_text}\n\n"
                        counter += 1

    if srt_content:
        return srt_content
        
    fallback_text = chunks[0].strip()
    if fallback_text.startswith("```json"):
        fallback_text = fallback_text[7:]
    if fallback_text.endswith("```"):
        fallback_text = fallback_text[:-3]
        
    if global_chars:
        fallback_text = f"{global_chars.strip()}\n\n{fallback_text}"
        
    return f"1\n00:00:00,000 --> 00:00:05,000\n{fallback_text.strip()}\n\n"


def get_mime_type(path):
    ext = os.path.splitext(path)[1].lower().strip()
    if ext == '.pdf': return 'application/pdf'
    if ext in ['.jpg', '.jpeg']: return 'image/jpeg'
    if ext == '.png': return 'image/png'
    if ext == '.webp': return 'image/webp'
    if ext in ['.tif', '.tiff']: return 'image/jpeg'
    if ext in ['.heic', '.heif']: return 'image/heic'
    if ext == '.mp3': return 'audio/mpeg'
    if ext == '.wav': return 'audio/wav'
    if ext == '.ogg': return 'audio/ogg'
    if ext == '.mp4': return 'video/mp4'
    import mimetypes
    guessed, _ = mimetypes.guess_type(path)
    if guessed:
        return guessed
    
    try:
        with open(path, 'rb') as f:
            header = f.read(12)
            if header.startswith(b'%PDF'): return 'application/pdf'
            if header.startswith(b'\xFF\xD8'): return 'image/jpeg'
            if header.startswith(b'\x89PNG'): return 'image/png'
            if header.startswith(b'RIFF') and b'WEBP' in header: return 'image/webp'
    except Exception:
        pass
    
    text_exts = ['.txt', '.csv', '.md', '.py', '.js', '.html', '.css', '.json', '.xml', '.log']
    if ext in text_exts:
        return 'text/plain'
        
    return 'application/octet-stream'

def show_error_dialog(message):
    import gui
    def run_dialog():
        gui.mainFrame.prePopup()
        title = f"{vision_config.ADDON_NAME} Error"
        gui.messageBox(message, title, wx.OK | wx.ICON_ERROR)
        gui.mainFrame.postPopup()
    wx.CallAfter(run_dialog)

def check_screen_curtain_active():
    try:
        if bool(ctypes.windll.nvdaHelperLocal.isScreenFullyBlack()):
            # Translators: Error message shown when trying to take a screenshot while NVDA's Screen Curtain is enabled.
            msg = "The Screen Curtain is currently enabled. Please disable it (NVDA+Control+Escape) before using visual recognition features."
            show_error_dialog(msg)
            return True
    except Exception:
        pass
    return False

def get_file_path(title, wildcard, mode="open", multiple=False, default_name=""):
    import gui
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST if mode == "open" else wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    if multiple: style |= wx.FD_MULTIPLE
    gui.mainFrame.prePopup()
    try:
        with wx.FileDialog(gui.mainFrame, title, wildcard=wildcard, style=style, defaultFile=default_name) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                return dlg.GetPaths() if multiple else dlg.GetPath()
    finally:
        gui.mainFrame.postPopup()
    return None

def _generate_object_signature(obj):
    role_type = int(getattr(obj, "role", 0))
    unique_signature = ""
    
    try:
        if hasattr(obj, "UIAElement") and obj.UIAElement.currentAutomationId:
            unique_signature = f"uia_{obj.UIAElement.currentAutomationId}"
    except Exception:
        pass
        
    if not unique_signature:
        try:
            win_ctrl_id = getattr(obj, "windowControlID", None)
            class_name = getattr(obj, "windowClassName", None)
            if win_ctrl_id and class_name:
                unique_signature = f"win_{class_name}_{win_ctrl_id}"
        except Exception:
            pass
            
    if not unique_signature:
        loc = getattr(obj, "location", None)
        if loc:
            try:
                handle = getattr(obj, "windowHandle", None)
                if handle:
                    rect = winUser.getWindowRect(handle)
                    w_left, w_top = rect.left, rect.top
                else:
                    w_left, w_top = 0, 0
            except Exception:
                w_left, w_top = 0, 0
            rel_x = loc.left - w_left
            rel_y = loc.top - w_top
            unique_signature = f"coords_{rel_x},{rel_y}"
            
    if not unique_signature:
        return None
        
    try:
        raw_name = obj._get_name() if hasattr(obj, '_get_name') else getattr(obj, "name", "")
    except Exception:
        raw_name = getattr(obj, "name", "")
    raw_name = raw_name or ""
    
    return f"sig_{role_type}_{unique_signature}_{raw_name}"