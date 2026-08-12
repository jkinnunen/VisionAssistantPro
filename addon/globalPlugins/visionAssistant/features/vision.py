# -*- coding: utf-8 -*-
import os
import json
import threading
import logging
import re
import tempfile
import time
import subprocess
import shutil
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import wx

import addonHandler
import config
import gui
import ui
import core
import api
import tones
import scriptHandler
import controlTypes

log = logging.getLogger(__name__)
addonHandler.initTranslation()

from .. import plugin_state
from ..ai.core import AIHandler
from ..ai.providers.gemini import GeminiHandler
from ..ai.translation import GoogleTranslator
from ..ai.ocr import ChromeOCREngine, SmartProgrammersOCREngine
from ..utils.system import VirtualDocument, get_focused_explorer_files
from .. import vision_config
from ..vision_config import get_lang_name, get_localized_languages, ADDON_NAME, TARGET_NAMES, REFINE_PROMPT_KEYS
from ..prompt_utils import (
    get_builtin_default_prompt_map, get_builtin_default_prompts,
    get_configured_default_prompt_map, get_configured_default_prompts,
    get_prompt_text, load_configured_custom_prompts, load_default_prompt_overrides,
    parse_custom_prompts_v2, serialize_custom_prompts_v2,
    serialize_default_prompt_overrides, _normalize_custom_prompt_items,
    _normalize_required_markers, _normalize_required_regex_checks,
    _sanitize_default_prompt_overrides, apply_prompt_template,
    clean_markdown, markdown_to_html, strip_thinking_tags, get_refine_menu_options
)
from ..utils.system import get_mime_type, get_file_path, OCRProgressStore, _is_failed_ocr_page, show_error_dialog, check_screen_curtain_active, convert_json_to_srt_string
from ..utils.media_capture import LiveSession, get_proxy_opener
from ..features.upload import UploadMixin
from ..dialogs.media import LiveAssistantDialog
from ..dialogs.document import DocumentViewerDialog, RangeDialog
from ..dialogs.chat_dialog import VisionQADialog
try:
    import fitz
except ImportError:
    fitz = None


class VisionMixin:
    def _announce_translation(self, text):
        # Translators: Message reported when calling translation command
        msg = _("Translated: {text}").format(text=text)
        self.report_status(msg)
        tones.beep(1000, 100)
        wx.CallAfter(self._open_translation_dialog, text)


    def _ask_file_action(self, path):
        self._dialog_open = True
        # Translators: Options for the image file action menu
        choices = [_("Extract Text (OCR)"), _("Describe Image")]
        gui.mainFrame.prePopup()
        try:
            dlg = wx.SingleChoiceDialog(gui.mainFrame, _("Choose action:"), _("Image File"), choices)
            dlg.Raise()
            if dlg.ShowModal() == wx.ID_OK:
                selection = dlg.GetSelection()
                if selection == 0:
                    v_doc = VirtualDocument([path])
                    v_doc.scan()
                    if v_doc.total_pages > 1:
                        wx.CallAfter(self._show_ocr_range_dialog, v_doc)
                    else:
                        threading.Thread(target=self._process_file_ocr, args=(v_doc, 0, 0, False, get_lang_name("target_language")), daemon=True).start()
                else:
                    # Translators: Status reported when an image file is being analyzed
                    self.report_status(_("Analyzing Image File..."))
                    threading.Thread(target=self._thread_image_describe, args=(path,), daemon=True).start()
            dlg.Destroy()
        finally:
            gui.mainFrame.postPopup()
            self._dialog_open = False


    def _browse_file(self, wildcard):
        # Translators: Message announced by NVDA when the live voice conversation ends.
        return get_file_path(_("Open"), wildcard)


    def _end_live_session(self):
        if self.live_session:
            try: self.live_session.stop()
            except Exception: pass


    def _live_append(self, line):
        if getattr(self, "live_dlg", None):
            try: self.live_dlg.append_line(line)
            except Exception: pass


    def _live_on_closed(self):
        self.live_session = None
        if getattr(self, "_live_video_timer", None):
            try:
                self._live_video_timer.Stop()
                gui.mainFrame.Unbind(wx.EVT_TIMER, handler=self._on_live_video_tick, source=self._live_video_timer)
            except Exception: pass
            self._live_video_timer = None
        if getattr(self, "live_dlg", None) and LiveAssistantDialog.instance:
            try:
                self.live_dlg.set_active(False)
                # Translators: Line appended to the conversation when the live session has ended.
                self.live_dlg.append_line(_("--- Session ended ---"))
            except Exception: pass
        else:
            self.live_dlg = None
        tones.beep(440, 120)
        self.report_status(_("Live conversation ended."))


    def _live_status(self, msg):
        if msg.startswith("ERROR:"):
            show_error_dialog(msg[6:])
            self._end_live_session()
        elif msg.startswith("STATUS:"):
            self.report_status(msg[7:])


    def _live_stream(self, chunk):
        if getattr(self, "live_dlg", None):
            try: self.live_dlg.append_raw(chunk)
            except Exception: pass


    def _maybe_resume_ocr(self, context, paths):

        key = self._ocr_progress_key(context, paths)
        record = OCRProgressStore.load(key)
        if not record:
            return None

        total_pages = record.get("end", 0) - record.get("start", 0) + 1
        done_pages = min(len(record.get("pages", {})), total_pages)
        file_count = len(record.get("paths", paths))

        # Translators: Title of the dialog asking whether to resume an OCR operation that did not finish (for example after NVDA closed unexpectedly).
        title = _("Unfinished Operation")
        # Translators: Message asking whether to continue an interrupted OCR extraction. {done} is the number of pages already processed, {total} is the total number of pages, and {files} is the number of files involved.
        msg = _("You have an unfinished operation: {done} of {total} pages processed across {files} file(s). Would you like to continue from where it stopped?").format(done=done_pages, total=total_pages, files=file_count)

        result = {}
        done = threading.Event()

        def ask():
            try:
                result["yes"] = (gui.messageBox(msg, title, wx.YES_NO | wx.ICON_QUESTION) == wx.YES)
            finally:
                done.set()

        if wx.IsMainThread():
            ask()
        else:
            wx.CallAfter(ask)
            done.wait()

        if result.get("yes"):
            return record
        OCRProgressStore.clear(key)
        return None

    @staticmethod
    def _ocr_progress_key(context, paths):
        return context + "|" + "|".join(sorted(paths))


    def _on_live_video_tick(self, event):
        session = self.live_session
        if not session:
            return
        jpeg_b64, w, h, m = self._capture_fullscreen()
        if jpeg_b64:
            threading.Thread(target=session.send_video_frame, args=(jpeg_b64,), daemon=True).start()


    def _open_direct_chat_dialog(self, force_show=True, is_recall=False):
        self._last_result_data = (self._open_direct_chat_dialog, ())
        if not is_recall:
            self._last_chat_history = None
        if self.vision_dlg:
            try: self.vision_dlg.Destroy()
            except Exception: pass
            self.vision_dlg = None

        def cb(atts, q, history, sz):
            lang = get_lang_name("ai_response_language")
            attached_paths = sz.get('attachments', [])

            if not AIHandler.is_gemini():
                other_parts = []
                for path in attached_paths:
                    if not os.path.exists(path): continue
                    mime_type = get_mime_type(path)
                    if mime_type.startswith("image/"):
                        try:
                            with open(path, "rb") as f:
                                data = base64.b64encode(f.read()).decode("utf-8")
                            other_parts.append({"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{data}"}})
                        except Exception: pass
                        
                messages = []
                for h in history:
                    r = "assistant" if h.get("role") == "model" else "user"
                    txt = h["parts"][0]["text"] if h.get("parts") else ""
                    messages.append({"role": r, "content": txt})
                
                current_user_msg = {"role": "user", "content": [{"type": "text", "text": f"{q} (Answer strictly in {lang})"}] + other_parts}
                messages.append(current_user_msg)
                return AIHandler.call(messages), None

            keys = GeminiHandler._get_api_keys(task="chat")
            num_keys = len(keys)
            keys_exhausted = 0
            
            while keys_exhausted < num_keys:
                idx = getattr(GeminiHandler, '_working_key_idx', 0)
                key = keys[idx % num_keys]
                gemini_parts = []
                for path in attached_paths:
                    if not os.path.exists(path): continue
                    mime_type = get_mime_type(path)
                    
                    if "pdf" in mime_type.lower() or mime_type.startswith("audio/") or mime_type.startswith("video/"):
                        file_uri = self._upload_file_to_gemini(path, mime_type, api_key=key)
                        if file_uri:
                            gemini_parts.append({"file_data": {"mime_type": mime_type, "file_uri": file_uri}})
                    else:
                        try:
                            with open(path, "rb") as f:
                                data = base64.b64encode(f.read()).decode("utf-8")
                            gemini_parts.append({"inline_data": {"mime_type": mime_type, "data": data}})
                        except Exception: pass
                        
                current_user_msg = {"role": "user", "parts": [{"text": f"{q} (Answer strictly in {lang})"}] + gemini_parts}
                messages = []
                messages.extend(history)
                messages.append(current_user_msg)
                
                atts_for_forcing = [{"file_uri": p["file_data"]["file_uri"]} for p in gemini_parts if "file_data" in p]
                
                res = AIHandler.call(messages, attachments=atts_for_forcing if atts_for_forcing else None)
                
                if atts_for_forcing and res and res.startswith("ERROR:"):
                    err_msg_lower = res.lower()
                    if "quota" in err_msg_lower or "exhausted" in err_msg_lower or "429" in err_msg_lower or "permission" in err_msg_lower or "403" in err_msg_lower:
                        keys_exhausted += 1
                        GeminiHandler._working_key_idx = (GeminiHandler._working_key_idx + 1) % num_keys
                        continue
                        
                return res, None
                
            # Translators: Error when all available API keys fail
            return "ERROR:" + _("All API Keys failed (Quota/Server)."), None


        # Translators: Initial greeting message for the Direct Chat dialog.
        init_msg = _("Hello! I am Vision Assistant Pro. How can I help you today?")
        
        self.vision_dlg = VisionQADialog(
            gui.mainFrame, 
            # Translators: Dialog title for Direct Chat
            _("{name} - Direct Chat").format(name=ADDON_NAME), 
            init_msg, 
            None, 
            cb, 
            extra_info={'skip_init_history': True, 'restore_history': getattr(self, "_last_chat_history", None) if is_recall else None},
            raw_content=init_msg,
            status_callback=self.report_status,
            allow_attachments=True
        )
        self.vision_dlg.Show()
        self.vision_dlg.Raise()


    def _open_doc_chat_dialog(self, init_msg, initial_attachments, doc_text, raw_text_for_save=None, force_show=False, is_recall=False):
        self._last_result_data = (self._open_doc_chat_dialog, (init_msg, initial_attachments, doc_text, raw_text_for_save))
        if not is_recall:
            self._last_chat_history = None
        if config.conf["VisionAssistant"]["copy_to_clipboard"]:
            api.copyToClip(raw_text_for_save if raw_text_for_save else init_msg)

        if config.conf["VisionAssistant"]["skip_chat_dialog"] and not force_show:
            if not is_recall: tones.beep(1000, 100)
            ui.message(clean_markdown(init_msg))
            return

        if self.doc_dlg:
            try: 
                self.doc_dlg.Destroy()
            except Exception: pass
            self.doc_dlg = None
            
        if not is_recall:
            tones.beep(1000, 100)

        def doc_callback(ctx_atts, q, history, dum2):
            lang = get_lang_name("ai_response_language")
            system_template = get_prompt_text("document_chat_system")
            system_instr = apply_prompt_template(system_template, [("response_lang", lang)])
            
            if AIHandler.is_gemini():
                context_parts = []
                if ctx_atts:
                    for att in ctx_atts:
                        if 'file_uri' in att:
                            context_parts.append({"file_data": {"mime_type": att['mime_type'], "file_uri": att['file_uri']}})
                        elif 'data' in att:
                            context_parts.append({"inline_data": {"mime_type": att['mime_type'], "data": att['data']}})
                else:
                    context_parts.append({"text": f"Context content:\n{doc_text}"})
                
                context_parts.append({"text": f"Instruction: {system_instr}"})
                messages = [{"role": "user", "parts": context_parts}]
                ack_text = get_prompt_text("document_chat_ack") or "Context received. Ready for questions."
                messages.append({"role": "model", "parts": [{"text": ack_text}]})
                if history: messages.extend(history)
                messages.append({"role": "user", "parts": [{"text": q}]})
                return AIHandler.call(messages), None
            else:
                messages = []
                messages.append({"role": "user", "content": f"{system_instr}\n\nContext content:\n{doc_text}"})
                messages.append({"role": "assistant", "content": get_prompt_text("document_chat_ack") or "Context received."})
                if history:
                    for h in history:
                        role = "assistant" if h["role"] == "model" else "user"
                        messages.append({"role": role, "content": h["parts"][0]["text"]})
                messages.append({"role": "user", "content": q})
                return AIHandler.call(messages), None
            
        self.doc_dlg = VisionQADialog(
            gui.mainFrame, 
            # Translators: Dialog title for a Chat dialog
            _("{name} - Chat").format(name=ADDON_NAME), 
            init_msg, 
            initial_attachments, 
            doc_callback, 
            extra_info={'skip_init_history': True, 'restore_history': getattr(self, "_last_chat_history", None) if is_recall else None},
            raw_content=raw_text_for_save,
            status_callback=self.report_status
        )
        self.doc_dlg.Show()
        self.doc_dlg.Raise()


    def _open_document_reader(self):
        self._dialog_open = True
        # Translators: File dialog filter for supported files
        wc = _("Supported Files") + "|*.pdf;*.jpg;*.jpeg;*.png;*.tif;*.tiff;*.heic;*.heif"
        self._browse_and_run(self._scan_and_open, wc, multiple=True)
        self._dialog_open = False


    def _open_document_viewer(self, v_doc, settings, resume=None):
        self.doc_viewer_dlg = DocumentViewerDialog(gui.mainFrame, v_doc, settings, resume=resume)
        self.doc_viewer_dlg.Show()


    def _open_refine_dialog(self, captured_text):
        options = get_refine_menu_options()
        if not options:
            prompt_map = get_builtin_default_prompt_map()
            for key in REFINE_PROMPT_KEYS:
                if key in prompt_map:
                    item = prompt_map[key]
                    options.append((item["label"], item["prompt"]))
        
        display_choices = [opt[0] for opt in options]
        
        gui.mainFrame.prePopup()
        try:
            self.refine_menu_dlg = wx.SingleChoiceDialog(
                gui.mainFrame,
                # Translators: Title of the Refine dialog
                _("Choose action:"),
                _("Refine"),
                display_choices,
            )
            
            self.refine_menu_dlg.Raise()
            self.refine_menu_dlg.SetFocus()
            
            modal_res = self.refine_menu_dlg.ShowModal()
        finally:
            gui.mainFrame.postPopup()

        if modal_res == wx.ID_OK:
            selection_index = self.refine_menu_dlg.GetSelection()
            custom_content = options[selection_index][1]
            if self.refine_menu_dlg:
                self.refine_menu_dlg.Destroy()
                self.refine_menu_dlg = None

            file_paths = []
            needs_file = False
            wc = "Files|*.*"
            
            if "[file_ocr]" in custom_content:
                needs_file = True
                wc = "Images/PDF/TIFF|*.png;*.jpg;*.webp;*.pdf;*.tif;*.tiff;*.heic;*.heif"
            elif "[file_read]" in custom_content:
                needs_file = True
                wc = "Documents|*.txt;*.py;*.md;*.html;*.pdf;*.tif;*.tiff"
            elif "[file_audio]" in custom_content:
                needs_file = True
                wc = "Audio|*.mp3;*.wav;*.ogg"
            
            if needs_file:
                gui.mainFrame.prePopup()
                try:
                    dlg = wx.FileDialog(gui.mainFrame, _("Open"), wildcard=wc, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
                    if dlg.ShowModal() == wx.ID_OK:
                        file_paths = dlg.GetPaths()
                        file_paths.sort()
                        wx.CallLater(200, lambda: threading.Thread(target=self._thread_refine, args=(captured_text, custom_content, file_paths), daemon=True).start())
                    dlg.Destroy()
                finally:
                    gui.mainFrame.postPopup()
            else:
                # Translators: Message while processing request of the refine text command
                msg = _("Processing...")
                self.report_status(msg)
                wx.CallLater(200, lambda: threading.Thread(target=self._thread_refine, args=(captured_text, custom_content, None), daemon=True).start())
        else:
            if self.refine_menu_dlg:
                self.refine_menu_dlg.Destroy()
                self.refine_menu_dlg = None


    def _open_refine_result_dialog(self, result_text, attachments, original_text, initial_prompt, force_show=False, is_recall=False):
        self._last_result_data = (self._open_refine_result_dialog, (result_text, attachments, original_text, initial_prompt))
        if not is_recall:
            self._last_chat_history = None
        if config.conf["VisionAssistant"]["copy_to_clipboard"]:
            api.copyToClip(result_text)

        if config.conf["VisionAssistant"]["skip_chat_dialog"] and not force_show:
            if not is_recall: tones.beep(1000, 100)
            ui.message(clean_markdown(result_text))
            return

        if self.refine_dlg:
            try: self.refine_dlg.Destroy()
            except Exception: pass
            
        if not is_recall:
            tones.beep(1000, 100)

        def refine_callback(ctx, q, history, extra):
            atts, orig, first_p = ctx
            
            if AIHandler.is_gemini():
                parts = [{"text": q}]
                current_user_msg = {"role": "user", "parts": parts}
                messages = []
                if len(history) <= 1: 
                    sys_parts = [{"text": first_p}]
                    for att in atts:
                        if 'file_uri' in att:
                            sys_parts.append({"file_data": {"mime_type": att['mime_type'], "file_uri": att['file_uri']}})
                        elif 'data' in att:
                            sys_parts.append({"inline_data": {"mime_type": att['mime_type'], "data": att['data']}})
                    messages.append({"role": "user", "parts": sys_parts})
                    if history: messages.append(history[0])
                else:
                    messages.extend(history)
                messages.append(current_user_msg)
                return AIHandler.call(messages), None
            else:
                messages = []
                messages.append({"role": "user", "content": first_p})
                messages.append({"role": "assistant", "content": result_text})
                
                if history:
                    for h in history:
                        if h.get("role") == "model" and h["parts"][0]["text"] == result_text: continue
                        role = "assistant" if h["role"] == "model" else "user"
                        messages.append({"role": role, "content": h["parts"][0]["text"]})
                
                messages.append({"role": "user", "content": q})
                return AIHandler.call(messages), None

        context = (attachments, original_text, initial_prompt)
        has_file_context = any('file_uri' in a for a in attachments)

        self.refine_dlg = VisionQADialog(
            gui.mainFrame, 
            # Translators: Title of Refine Result dialog
            _("{name} - Refine Result").format(name=ADDON_NAME), 
            result_text, 
            context, 
            refine_callback, 
            extra_info={'file_context': has_file_context, 'skip_init_history': False, 'restore_history': getattr(self, "_last_chat_history", None) if is_recall else None},
            raw_content=result_text,
            status_callback=self.report_status
        )
        self.refine_dlg.Show()
        self.refine_dlg.Raise()


    def _open_smart_file_dialog(self):
        self._dialog_open = True
        wc = "Files|*.pdf;*.jpg;*.jpeg;*.png;*.webp;*.tif;*.tiff;*.heic;*.heif"
        self._browse_and_run(self._pre_process_smart_file, wc, multiple=True)
        self._dialog_open = False


    def _open_translation_dialog(self, text, force_show=False, is_recall=False):
        self._last_result_data = (self._open_translation_dialog, (text,))
        if not is_recall:
            self._last_chat_history = None
        if config.conf["VisionAssistant"]["copy_to_clipboard"]:
            api.copyToClip(text)
            
        if config.conf["VisionAssistant"]["skip_chat_dialog"] and not force_show:
            return
            
        if self.translation_dlg:
            try: self.translation_dlg.Destroy()
            except Exception: pass
            self.translation_dlg = None

        def noop_callback(ctx, q, history, extra):
            return None, None

        self.translation_dlg = VisionQADialog(
            gui.mainFrame, 
            # Translators: Dialog title for Translation results
            _("{name} - Translation").format(name=ADDON_NAME), 
            text, 
            None, 
            noop_callback, 
            extra_info={'skip_init_history': True, 'restore_history': getattr(self, "_last_chat_history", None) if is_recall else None},
            raw_content=text,
            status_callback=self.report_status,
            announce_on_open=False,
            allow_questions=False
        )
        self.translation_dlg.Show()
        self.translation_dlg.Raise()


    def _open_vision_dialog(self, text, atts, size, force_show=False, is_recall=False):
        self._last_result_data = (self._open_vision_dialog, (text, atts, size))
        if not is_recall:
            self._last_chat_history = None
        if config.conf["VisionAssistant"]["copy_to_clipboard"]:
            api.copyToClip(text)

        if config.conf["VisionAssistant"]["skip_chat_dialog"] and not force_show:
            if not is_recall: tones.beep(1000, 100)
            ui.message(clean_markdown(text))
            return

        if self.vision_dlg:
            try: self.vision_dlg.Destroy()
            except Exception: pass
            self.vision_dlg = None
            
        if not is_recall:
            tones.beep(1000, 100)

        def cb(atts, q, history, sz):
            lang = get_lang_name("ai_response_language")
            followup_suffix_template = get_prompt_text("vision_followup_suffix") or "Answer strictly in {response_lang}"
            followup_suffix = apply_prompt_template(followup_suffix_template, [("response_lang", lang)])
            
            if AIHandler.is_gemini():
                current_user_msg = {"role": "user", "parts": [{"text": f"{q} ({followup_suffix})"}]}
                messages = []
                initial_history = (not history) or (len(history) == 1 and history[0].get("role") == "model")
                if initial_history:
                    parts = []
                    for att in atts:
                        parts.append({"inline_data": {"mime_type": att['mime_type'], "data": att['data']}})
                    followup_context_template = get_prompt_text("vision_followup_context") or "Image Context. Target Language: {response_lang}"
                    followup_context = apply_prompt_template(followup_context_template, [("response_lang", lang)])
                    parts.append({"text": followup_context})
                    messages.append({"role": "user", "parts": parts})
                    if history and history[0].get("role") == "model":
                        messages.append(history[0])
                    else:
                        messages.append({"role": "model", "parts": [{"text": text}]})
                else:
                    messages.extend(history)
                messages.append(current_user_msg)
                return AIHandler.call(messages, attachments=atts), None
            else:
                messages = []
                followup_context_template = get_prompt_text("vision_followup_context") or "Image Context. Target Language: {response_lang}"
                followup_context = apply_prompt_template(followup_context_template, [("response_lang", lang)])
                
                initial_content = [{"type": "text", "text": followup_context}]
                for att in atts:
                    initial_content.append({"type": "image_url", "image_url": {"url": f"data:{att['mime_type']};base64,{att['data']}"}})
                
                messages.append({"role": "user", "content": initial_content})
                messages.append({"role": "assistant", "content": text})
                
                if history:
                    for h in history:
                        if h.get("role") == "model" and h["parts"][0]["text"] == text: continue
                        role = "assistant" if h["role"] == "model" else "user"
                        messages.append({"role": role, "content": h["parts"][0]["text"]})
                
                messages.append({"role": "user", "content": f"{q} ({followup_suffix})"})
                return AIHandler.call(messages, attachments=atts), None
            
        self.vision_dlg = VisionQADialog(
            gui.mainFrame, 
            # Translators: Dialog title for Image Analysis
            _("{name} - Image Analysis").format(name=ADDON_NAME), 
            text, 
            atts, 
            cb, 
            extra_info={'restore_history': getattr(self, "_last_chat_history", None) if is_recall else None},
            raw_content=text,
            status_callback=self.report_status
        )
        self.vision_dlg.Show()
        self.vision_dlg.Raise()


    def _pre_process_file_ocr_single(self, path):
        v_doc = VirtualDocument([path])
        v_doc.scan()
        self._process_file_ocr(v_doc, 0, 0)


    def _pre_process_smart_file(self, paths, resume=None):
        engine = config.conf["VisionAssistant"]["ocr_engine"]
        is_single_image = len(paths) == 1 and paths[0].lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.heic', '.heif'))

        if engine == 'none' and any(p.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.heic', '.heif')) for p in paths):
            # Translators: Message shown when a PDF has no text layer.
            msg = _("The 'None (Extract Text Layer)' engine cannot process image-based content. Please change the OCR Engine to 'Chrome' or 'AI (Advanced)' in settings.")
            # Translators: Title of the error dialog shown when the selected OCR engine cannot process the chosen image-based files.
            wx.CallAfter(gui.messageBox, msg, _("OCR Engine Error"), wx.OK | wx.ICON_ERROR)
            return

        if is_single_image and engine == 'gemini':
            time.sleep(0.5)
            wx.CallAfter(self._ask_file_action, paths[0])
            return
        try:
            if not fitz:
                # Translators: Error when PyMuPDF is missing
                wx.CallAfter(wx.MessageBox, _("PyMuPDF library is missing."), "Error", wx.ICON_ERROR)
                return
            v_doc = VirtualDocument(paths)
            v_doc.scan()
            if v_doc.total_pages == 0:
                # Translators: Error when no pages found
                wx.CallAfter(wx.MessageBox, _("No readable pages found."), "Error", wx.ICON_ERROR)
                return
            if resume is None:
                resume = self._maybe_resume_ocr("smartfile", list(paths))
            if resume:
                threading.Thread(target=self._process_file_ocr, args=(v_doc, resume["start"], resume["end"], resume["do_translate"], resume["target_lang"], resume), daemon=True).start()
            elif v_doc.total_pages == 1:
                threading.Thread(target=self._process_file_ocr, args=(v_doc, 0, 0), daemon=True).start()
            else:
                wx.CallAfter(self._show_ocr_range_dialog, v_doc)
        except Exception as e:
            log.error(f"Error preparing file: {e}")


    def _process_file_ocr(self, v_doc, start_page, end_page, do_translate=False, target_lang=None, resume=None):
        if target_lang is None:
            target_lang = get_lang_name("target_language")
        engine = config.conf["VisionAssistant"]["ocr_engine"]
        p = config.conf["VisionAssistant"]["active_provider"]
        progress_key = self._ocr_progress_key("smartfile", list(v_doc.file_paths))

        total_pages = end_page - start_page + 1
        done_pages = dict(resume.get("pages", {})) if resume else {}
        self._ocr_abort["smartfile"] = False
        self._ocr_task_running["smartfile"] = True

        def save_progress():
            OCRProgressStore.save(progress_key, {
                "paths": list(v_doc.file_paths),
                "start": start_page,
                "end": end_page,
                "do_translate": do_translate,
                "target_lang": target_lang,
                "pages": done_pages,
            })

        def finalize_running():
            self._ocr_task_running["smartfile"] = False

        if engine == 'none':
            def fast_worker(page_idx):
                try:
                    f_path, internal_idx = v_doc.get_page_info(page_idx)
                    doc = fitz.open(f_path)
                    page = doc.load_page(internal_idx)
                    txt = DocumentViewerDialog._extract_text_layer_from_page(page)
                    doc.close()
                    return page_idx, (f"--- Page {page_idx + 1} ---\n{txt}\n" if txt else "")
                except Exception: return page_idx, ""
            pending = [i for i in range(start_page, end_page + 1) if str(i) not in done_pages]
            if pending:
                # Translators: Status message showing page-by-page progress during file OCR.
                progress_msg = _("Processing page {current} of {total}...").format(current=len(done_pages)+1, total=total_pages)
                core.callLater(0, ui.message, progress_msg)
                self.current_status = progress_msg

            with ThreadPoolExecutor(max_workers=5) as executor:
                for page_idx, part in executor.map(fast_worker, pending):
                    if self._ocr_abort["smartfile"]:
                        break
                    done_pages[str(page_idx)] = part
                    save_progress()
                    
                    completed_count = len(done_pages)
                    progress_msg = _("Processing page {current} of {total}...").format(current=completed_count, total=total_pages)
                    self.current_status = progress_msg
            finalize_running()
            if self._ocr_abort["smartfile"]:
                return
            full_text = "\n".join(p for _dummy, p in sorted(((int(k), v) for k, v in done_pages.items())) if p).strip()
            if not full_text:
                OCRProgressStore.clear(progress_key)
                wx.CallAfter(show_error_dialog, _("The 'None (Extract Text Layer)' engine cannot process image-based content. Please change the OCR Engine to 'Chrome' or 'AI (Advanced)' in settings."))
                return
            if do_translate:
                full_text = AIHandler.translate(full_text, target_lang)
            OCRProgressStore.clear(progress_key)
            wx.CallAfter(self._open_doc_chat_dialog, full_text, [], full_text, full_text)
            return

        # Translators: Message reported when extracting text from a file
        msg = _("Extracting Text...")
        self.current_status = msg
        core.callLater(0, ui.message, msg)
        
        upload_supported = AIHandler.is_gemini() or p == "mistral"
        if p == "custom":
            upload_supported = config.conf["VisionAssistant"].get("custom_upload_support", False)

        if engine == 'chrome' or not upload_supported or total_pages == 1:
            errors_list = []
            errors_lock = threading.Lock()

            def page_worker(page_idx):
                try:
                    f_path, internal_idx = v_doc.get_page_info(page_idx)
                    doc = fitz.open(f_path)
                    page = doc.load_page(internal_idx)
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                    img_bytes = pix.tobytes("jpg")
                    doc.close()

                    if engine == 'chrome':
                        txt = ChromeOCREngine.recognize(img_bytes)
                    else:
                        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
                        txt = AIHandler.ocr(img_b64, "image/jpeg")

                    if not txt: 
                        return page_idx, ""
                    
                    if txt.startswith("ERROR:"):
                        with errors_lock:
                            errors_list.append(txt[6:])
                        log.error(f"SmartFile OCR page {page_idx + 1} failed: {txt}")
                        return page_idx, ""

                    if do_translate:
                        txt = AIHandler.translate(txt, target_lang)
                    return page_idx, f"--- Page {page_idx + 1} ---\n{txt}\n"
                except Exception as e:
                    log.error(f"Exception in page_worker for page {page_idx + 1}: {e}", exc_info=True)
                    return page_idx, ""

            pending = [i for i in range(start_page, end_page + 1) if str(i) not in done_pages]
            if pending:
                progress_msg = _("Processing page {current} of {total}...").format(current=len(done_pages)+1, total=total_pages)
                core.callLater(0, ui.message, progress_msg)
                self.current_status = progress_msg

            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = {executor.submit(page_worker, i): i for i in pending}
                for future in as_completed(futures):
                    if self._ocr_abort["smartfile"]:
                        break
                    try:
                        page_idx, part = future.result()
                        if not _is_failed_ocr_page(part):
                            done_pages[str(page_idx)] = part
                            save_progress()
                            
                            completed_count = len(done_pages)
                            progress_msg = _("Processing page {current} of {total}...").format(current=completed_count, total=total_pages)
                            core.callLater(0, ui.message, progress_msg)
                            self.current_status = progress_msg
                    except Exception as e:
                        log.error(f"Error retrieving future result: {e}", exc_info=True)

            finalize_running()
            # Translators: Error message shown when uploading a video file fails.
            self.current_status = _("Idle")
            if self._ocr_abort["smartfile"]:
                return
            full_text = "\n".join(p for _dummy, p in sorted(((int(k), v) for k, v in done_pages.items())) if p).strip()
            if not full_text:
                OCRProgressStore.clear(progress_key)
                if errors_list:
                    wx.CallAfter(show_error_dialog, errors_list[0])
                else:
                    # Translators: Error message shown when the OCR process fails to detect any text in the file or an unknown error occurs during extraction.
                    wx.CallAfter(show_error_dialog, _("No text detected or error occurred."))
                return
            OCRProgressStore.clear(progress_key)
            wx.CallAfter(self._open_doc_chat_dialog, full_text, [], full_text, full_text)

        else:
            raw_batch_size = config.conf["VisionAssistant"].get("ocr_batch_size", 20)
            batch_size = total_pages if raw_batch_size == 0 else raw_batch_size
            had_error = False

            for i in range(start_page, end_page + 1, batch_size):
                if self._ocr_abort["smartfile"]:
                    break
                b_end = min(i + batch_size - 1, end_page)
                if all(str(idx) in done_pages for idx in range(i, b_end + 1)):
                    continue

                # Translators: Status message showing the progress of document scanning. {start} and {end} are page numbers.
                progress_msg = _("Processing pages {start} to {end}...").format(start=i+1, end=b_end+1)
                self.current_status = progress_msg
                core.callLater(0, ui.message, progress_msg)
                time.sleep(0.1)

                upload_path = v_doc.create_merged_pdf(i, b_end)
                if not upload_path: continue
                
                mime_type = "application/pdf"
                res = None

                if p == "mistral":
                    res = AIHandler.ocr(upload_path, "application/pdf")
                else:
                    keys = GeminiHandler._get_api_keys(task="chat")
                    num_keys = len(keys)
                    keys_exhausted = 0
                    
                    while keys_exhausted < num_keys:
                        file_uri = None
                        for attempt in range(2):
                            file_uri = self._upload_file_to_gemini(upload_path, mime_type, silent=True)
                            if file_uri:
                                break
                            time.sleep(0.5)
                            
                        if not file_uri:
                            keys_exhausted += 1
                            GeminiHandler._working_key_idx = (GeminiHandler._working_key_idx + 1) % num_keys
                            continue
                            
                        p_text = apply_prompt_template(get_prompt_text("ocr_document_translate" if do_translate else "ocr_document_extract"), [("target_lang", target_lang), ("response_lang", config.conf["VisionAssistant"]["ai_response_language"])])
                        attachments = [{'mime_type': mime_type, 'file_uri': file_uri}]
                        
                        for attempt in range(2):
                            res = AIHandler.call(p_text, attachments=attachments)
                            if res and not res.startswith("ERROR:"):
                                break
                            time.sleep(0.5)
                            
                        if res and res.startswith("ERROR:"):
                            err_msg_lower = res.lower()
                            if "quota" in err_msg_lower or "exhausted" in err_msg_lower or "429" in err_msg_lower or "permission" in err_msg_lower or "403" in err_msg_lower:
                                keys_exhausted += 1
                                GeminiHandler._working_key_idx = (GeminiHandler._working_key_idx + 1) % num_keys
                                continue
                        break
                        
                    if not file_uri or (res and res.startswith("ERROR:")):
                        if os.path.exists(upload_path): os.remove(upload_path)
                        had_error = True
                        # Translators: Error message shown when the upload fails.
                        msg = _("Failed to process document batch {start}-{end} after multiple attempts.").format(start=i+1, end=b_end+1)
                        wx.CallAfter(show_error_dialog, msg)
                        continue

                if os.path.exists(upload_path): os.remove(upload_path)

                if res and not res.startswith("ERROR:"):
                    if p == "mistral":
                        results = res.split('[[[PAGE_SEP]]]')
                        for j, text_part in enumerate(results):
                            page_idx = i + j
                            if page_idx <= end_page:
                                page_text = text_part.strip()
                                if do_translate and page_text:
                                    page_text = AIHandler.translate(page_text, target_lang)
                                done_pages[str(page_idx)] = page_text
                    else:
                        done_pages[str(i)] = res
                    save_progress()
                else:
                    had_error = True
                    # Translators: Error message shown when the connection to the server times out
                    err_msg = res[6:] if res and res.startswith("ERROR:") else _("Connection Timeout")
                    msg = _("Failed to process document batch {start}-{end}: {error}").format(start=i+1, end=b_end+1, error=err_msg)
                    wx.CallAfter(show_error_dialog, msg)

            finalize_running()
            self.current_status = _("Idle")
            if self._ocr_abort["smartfile"]:
                return
            all_text_parts = [v for _dummy, v in sorted(((int(k), v) for k, v in done_pages.items()))]
            if all_text_parts:
                OCRProgressStore.clear(progress_key)
                final_combined = "\n\n".join(all_text_parts)
                wx.CallAfter(self._open_doc_chat_dialog, final_combined, [], final_combined, final_combined)


    def _scan_and_open(self, paths, resume=None):
        try:
            if not fitz:
                wx.CallAfter(wx.MessageBox, _("PyMuPDF library is missing."), "Error", wx.ICON_ERROR)
                return

            engine = config.conf["VisionAssistant"]["ocr_engine"]
            image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.heic', '.heif')
            has_images = any(p.lower().endswith(image_extensions) for p in paths)

            if engine == 'none' and has_images:
                msg = _("The 'None (Extract Text Layer)' engine cannot process image-based content. Please change the OCR Engine to 'Chrome' or 'AI (Advanced)' in settings.")
                wx.CallAfter(gui.messageBox, msg, _("OCR Engine Error"), wx.OK | wx.ICON_ERROR)
                return

            v_doc = VirtualDocument(paths)
            v_doc.scan()
            if v_doc.total_pages == 0:
                 wx.CallAfter(wx.MessageBox, _("No readable pages found."), "Error", wx.ICON_ERROR)
                 return
            if resume is None:
                resume = self._maybe_resume_ocr("document", list(paths))
            if resume:
                settings = {'start': resume['start'], 'end': resume['end'], 'translate': resume['do_translate'], 'lang': resume['target_lang']}
                wx.CallAfter(lambda: self._open_document_viewer(v_doc, settings, resume))
            elif v_doc.total_pages == 1:
                settings = {'start': 0, 'end': 0, 'translate': False, 'lang': TARGET_NAMES[0]}
                wx.CallAfter(lambda: self._open_document_viewer(v_doc, settings))
            else:
                wx.CallAfter(self._show_range_dialog, v_doc)
        except Exception as e:
            log.error(f"Error opening files: {e}", exc_info=True)


    def _show_live_window(self):
        if getattr(self, "live_dlg", None) and LiveAssistantDialog.instance is self.live_dlg:
            self.live_dlg.set_active(bool(self.live_session))
        else:
            self.live_dlg = LiveAssistantDialog(gui.mainFrame, self._start_live_session, self._end_live_session)
            self.live_dlg.set_active(bool(self.live_session))
            self.live_dlg.Show()
        self.live_dlg.Raise()
        self.live_dlg.history.SetFocus()


    def _show_ocr_range_dialog(self, v_doc):
        gui.mainFrame.prePopup()
        try:
            range_dlg = RangeDialog(gui.mainFrame, v_doc.total_pages)
            if range_dlg.ShowModal() == wx.ID_OK:
                settings = range_dlg.get_settings()
                threading.Thread(target=self._process_file_ocr, 
                                 args=(v_doc, settings['start'], settings['end'], settings['translate'], settings['lang']), 
                                 daemon=True).start()
            range_dlg.Destroy()
        finally:
            gui.mainFrame.postPopup()


    def _show_range_dialog(self, v_doc):
        gui.mainFrame.prePopup()
        try:
            range_dlg = RangeDialog(gui.mainFrame, v_doc.total_pages)
            if range_dlg.ShowModal() == wx.ID_OK:
                settings = range_dlg.get_settings()
                wx.CallAfter(lambda: self._open_document_viewer(v_doc, settings))
            range_dlg.Destroy()
        finally:
            gui.mainFrame.postPopup()


    def _start_live_session(self):
        if self.live_session or not AIHandler.is_gemini():
            return
        tones.beep(660, 120)
        direct = config.conf["VisionAssistant"]["live_direct_output"]
        self.live_session = LiveSession(
            on_text=lambda line: wx.CallAfter(self._live_append, line),
            on_status=lambda msg: wx.CallAfter(self._live_status, msg),
            on_closed=lambda: wx.CallAfter(self._live_on_closed),
            on_stream=lambda chunk: wx.CallAfter(self._live_stream, chunk),
        )
        if not direct:
            self._show_live_window()
        self._live_video_timer = wx.Timer(gui.mainFrame)
        gui.mainFrame.Bind(wx.EVT_TIMER, self._on_live_video_tick, self._live_video_timer)
        self._live_video_timer.Start(2000)
        threading.Thread(target=self._start_live_worker, daemon=True).start()


    def _start_live_worker(self):
        session = self.live_session
        if session and not session.start():
            wx.CallAfter(self._live_on_closed)


    def _start_vision(self, full):
        if full: d, w, h, m = self._capture_fullscreen()
        else: d, w, h, m = self._capture_navigator()
        if d:
            # Translators: Message reported when calling an image analysis command
            msg = _("Scanning...")
            self.report_status(msg)
            wx.CallLater(100, lambda: threading.Thread(target=self._thread_vision, args=(d, w, h, m, full), daemon=True).start())
        else: 
            msg = _("Capture failed.")
            self.report_status(msg)


    def _stop_ocr_task(self, context):
        self._ocr_abort[context] = True
        self._ocr_task_running[context] = False
        self.current_status = _("Idle")
        # Translators: Announcement when an in-progress OCR extraction is stopped by the user.
        ui.message(_("OCR operation stopped."))
        tones.beep(300, 150)


    def _thread_image_describe(self, path):
        try:
            mime_type = get_mime_type(path)
            with open(path, "rb") as f:
                img_data = base64.b64encode(f.read()).decode('utf-8')
            
            lang = get_lang_name("ai_response_language")
            vision_template = get_prompt_text("vision_navigator_object")
            p = apply_prompt_template(vision_template, [("response_lang", lang)])
            
            att = [{'mime_type': mime_type, 'data': img_data}]
            res = AIHandler.call(p, attachments=att)
            
            if res:
                if res.startswith("ERROR:"):
                    wx.CallAfter(show_error_dialog, res[6:])
                else:
                    wx.CallAfter(self._open_vision_dialog, res, att, None)
            
            self.current_status = _("Idle")
        except Exception as e:
            log.error(f"Image file analysis failed: {e}", exc_info=True)
            self.current_status = _("Idle")


    def _thread_refine(self, captured_text, custom_content, file_paths=None):
        target_lang = get_lang_name("target_language")
        source_lang = get_lang_name("source_language")
        smart_swap = config.conf["VisionAssistant"]["smart_swap"]
        resp_lang = get_lang_name("ai_response_language")
        
        if file_paths and isinstance(file_paths, str):
            file_paths = [file_paths]
        elif not file_paths:
            file_paths = []

        prompt_text = custom_content
        attachments =[]
        needs_screenshot = "[screen_obj]" in prompt_text or "[screen_full]" in prompt_text or "[screen_fg_obj]" in prompt_text
        if needs_screenshot:
            time.sleep(0.25)
            if check_screen_curtain_active():
                self.current_status = _("Idle")
                return
                                
        fallback = "English" if source_lang == "Auto-detect" else source_lang
        swap_instr = f" If text is in {target_lang}, translate to {fallback}." if smart_swap else ""
        prompt_text = apply_prompt_template(prompt_text,[
            ("target_lang", target_lang),
            ("source_lang", source_lang),
            ("response_lang", resp_lang),
            ("swap_target", fallback),
            ("swap_instruction", swap_instr),
        ])
        
        if "[fix_translate]" in prompt_text:
            prompt_text = prompt_text.replace("[fix_translate]", 
                f"Fix grammar and translate to {target_lang}.{swap_instr} Output ONLY the result.")
        
        prompt_text = prompt_text.replace("[summarize]", f"Summarize the text below in {resp_lang}.").replace("[fix_grammar]", "Fix grammar in the text below. Output ONLY the fixed text.").replace("[explain]", f"Explain the text below in {resp_lang}.")
        
        used_selection = False
        if "[selection]" in prompt_text: 
            prompt_text = prompt_text.replace("[selection]", captured_text)
            used_selection = True
            
        if "[clipboard]" in prompt_text:
            try:
                clipboard_text = api.getClipData()
            except Exception:
                clipboard_text = ""
            prompt_text = prompt_text.replace("[clipboard]", clipboard_text)
            
        if "[clipboard_image]" in prompt_text:
            clip_path = self._getClipboardImageFile()
            if clip_path:
                try:
                    with open(clip_path, "rb") as f:
                        d = base64.b64encode(f.read()).decode('utf-8')
                    attachments.append({'mime_type': 'image/png', 'data': d})
                    os.remove(clip_path)
                except Exception:
                    pass
            prompt_text = prompt_text.replace("[clipboard_image]", "")
        
        if "[screen_obj]" in prompt_text:
            d, w, h, m = self._capture_navigator()
            if d: attachments.append({'mime_type': m, 'data': d})
            prompt_text = prompt_text.replace("[screen_obj]", "")
            
        if "[screen_full]" in prompt_text:
            d, w, h, m = self._capture_fullscreen()
            if d: attachments.append({'mime_type': m, 'data': d})
            prompt_text = prompt_text.replace("[screen_full]", "")

        if "[screen_fg_obj]" in prompt_text:
            d, x_fg, y_fg, w, h, m = self._capture_foreground()
            if d: attachments.append({'mime_type': m, 'data': d})
            prompt_text = prompt_text.replace("[screen_fg_obj]", "")

        if file_paths:
            # Translators: Message reported when executing the refine command
            msg = _("Uploading file...")
            core.callLater(0, self.report_status, msg)
            
            if "[file_ocr]" in prompt_text:
                if AIHandler.is_gemini() and fitz:
                    v_doc = VirtualDocument(file_paths)
                    v_doc.scan()
                    if v_doc.total_pages > 0:
                        upload_path = v_doc.create_merged_pdf(0, v_doc.total_pages - 1)
                        if upload_path:
                            file_uri = self._upload_file_to_gemini(upload_path, "application/pdf")
                            if file_uri:
                                attachments.append({'mime_type': 'application/pdf', 'file_uri': file_uri})
                            try: os.remove(upload_path)
                            except Exception: pass
                else:
                    for f_path in file_paths:
                        mime_type = get_mime_type(f_path)
                        ext = os.path.splitext(f_path)[1].lower()
                        if ext in ['.pdf', '.tif', '.tiff'] and fitz:
                            try:
                                doc = fitz.open(f_path)
                                for i in range(len(doc)):
                                    page = doc.load_page(i)
                                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                                    data = base64.b64encode(pix.tobytes("jpg")).decode('utf-8')
                                    attachments.append({'mime_type': 'image/jpeg', 'data': data})
                                doc.close()
                            except Exception: pass
                        else:
                            if AIHandler.is_gemini():
                                file_uri = self._upload_file_to_gemini(f_path, mime_type)
                                if file_uri: attachments.append({'mime_type': mime_type, 'file_uri': file_uri})
                            else:
                                try:
                                    with open(f_path, "rb") as f: data = base64.b64encode(f.read()).decode('utf-8')
                                    attachments.append({'mime_type': mime_type, 'data': data})
                                except Exception: pass
                                
            elif "[file_read]" in prompt_text:
                for f_path in file_paths:
                    mime_type = get_mime_type(f_path)
                    if AIHandler.is_gemini():
                        file_uri = self._upload_file_to_gemini(f_path, mime_type)
                        if file_uri: attachments.append({'mime_type': mime_type, 'file_uri': file_uri})
                    else:
                        try:
                            with open(f_path, "rb") as f: raw = f.read()
                            txt = raw.decode('utf-8')
                            prompt_text += f"\n\nFile Content ({os.path.basename(f_path)}):\n{txt}\n"
                        except Exception: pass

            elif "[file_audio]" in prompt_text:
                for f_path in file_paths:
                    mime_type = get_mime_type(f_path)
                    if AIHandler.is_gemini():
                        file_uri = self._upload_file_to_gemini(f_path, mime_type)
                        if file_uri: attachments.append({'mime_type': mime_type, 'file_uri': file_uri})
                    else:
                        try:
                            with open(f_path, "rb") as f: data = base64.b64encode(f.read()).decode('utf-8')
                            attachments.append({'mime_type': mime_type, 'data': data})
                        except Exception: pass

            prompt_text = prompt_text.replace("[file_ocr]", "").replace("[file_read]", "").replace("[file_audio]", "")
            
            if not prompt_text.strip() and attachments:
                 prompt_text = get_prompt_text("refine_files_only") or "Analyze these files."
            
        if captured_text and not used_selection and not file_paths:
            prompt_text += f"\n\n---\nInput Text:\n{captured_text}\n---\n"
            
        # Translators: Progress message spoken when the add-on starts taking a screenshot of the current focused object.
        msg = _("Analyzing...")
        core.callLater(0, self.report_status, msg)
        res = AIHandler.call(prompt_text, attachments=attachments)
        
        if res:
             if res.startswith("ERROR:"):
                 log.error(f"Refine AI call returned error: {res}")
                 self.current_status = _("Idle")
                 wx.CallAfter(show_error_dialog, res[6:])
                 return
             self.current_status = _("Idle")
             wx.CallAfter(self._open_refine_result_dialog, res, attachments, captured_text, prompt_text)


    def _thread_translate(self, text):
        try:
            p_name = config.conf["VisionAssistant"]["active_provider"]
            t = get_lang_name("target_language")
            s = get_lang_name("source_language")
            swap = config.conf["VisionAssistant"]["smart_swap"]
            fallback = "English" if s == "Auto-detect" else s
            
            log.info(f"Smart translate requested: text_len={len(text or '')}, target={t}, provider={p_name}")

            current_params = f"{p_name}|{t}|{swap}"
            if text == self._last_source_text and current_params == self._last_params and self.last_translation:
                log.info("Translation returned from cache.")
                core.callLater(0, self._announce_translation, self.last_translation)
                return

            translation_template = get_prompt_text("translate_main")
            p = apply_prompt_template(translation_template,[("target_lang", t), ("swap_target", fallback), ("smart_swap", str(swap)), ("text_content", text)])
            
            res = AIHandler.call(p)
            if res:
                if res.startswith("ERROR:"):
                    log.error(f"Translation AI call error: {res}")
                    self.current_status = _("Idle")
                    wx.CallAfter(show_error_dialog, res[6:])
                    return
                
                clean_res = clean_markdown(res)
                log.info(f"Translation completed successfully: {clean_res[:100]}...")
                self._last_source_text = text
                self._last_params = current_params
                self.last_translation = clean_res
                core.callLater(0, self._announce_translation, clean_res)
            
            self.current_status = _("Idle")

        except Exception as e:
            log.error(f"Translation thread failed: {e}", exc_info=True)
            self.current_status = _("Idle")


    def _thread_vision(self, img, w, h, m, full=False):
        lang = get_lang_name("ai_response_language")
        vision_key = "vision_fullscreen" if full else "vision_navigator_object"
        vision_template = get_prompt_text(vision_key)
        p = apply_prompt_template(vision_template,[
            ("response_lang", lang),
            ("width", w),
            ("height", h),
        ])
        att = [{'mime_type': m, 'data': img}]
        res = AIHandler.call(p, attachments=att)
        if res:
            if res.startswith("ERROR:"):
                log.error(f"Vision analysis AI call failed: {res}")
                self.current_status = _("Idle")
                wx.CallAfter(show_error_dialog, res[6:])
                return
            self.current_status = _("Idle")
            wx.CallAfter(self._open_vision_dialog, res, att, None)
        else:
            log.error("Vision analysis: AI returned empty response")
            self.current_status = _("Idle")

    # Translators: Script description for 'Opens the Document Reader for detailed page-by-page analysis (PDF/Images).' in Input Gestures dialog.
    @scriptHandler.script(description=_("Opens the Document Reader for detailed page-by-page analysis (PDF/Images)."), category=ADDON_NAME)
    def script_analyzeDocument(self, gesture):
        if self.toggling: self.finish()
        if getattr(self, "_dialog_open", False):
            return

        if self._ocr_task_running["document"]:
            self._stop_ocr_task("document")
            viewer = getattr(self, "doc_viewer_dlg", None)
            if viewer:
                viewer.abort = True
            return

        focused_paths = get_focused_explorer_files()

        valid_exts = ('.pdf', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.heic', '.heif')
        valid_paths = [p for p in focused_paths if p.lower().endswith(valid_exts)]
        if valid_paths:
            threading.Thread(target=self._scan_and_open, args=(valid_paths,), daemon=True).start()
            return
        clip_path = self._getClipboardImageFile()
        if clip_path:
            # Translators: Status reported when an image found in the clipboard is being processed.
            self.report_status(_("Processing clipboard image..."))
            threading.Thread(target=self._scan_and_open, args=([clip_path],), daemon=True).start()
            return
        wx.CallAfter(self._open_document_reader)

    # Translators: Script description for 'Describes the current object (Navigator Object).' in Input Gestures dialog.
    @scriptHandler.script(description=_("Describes the current object (Navigator Object)."), category=ADDON_NAME)
    def script_describeObject(self, gesture):
        if self.toggling: self.finish()
        if check_screen_curtain_active():
            return
        self._start_vision(False)

    # Translators: Script description for 'Performs OCR and description on the entire screen.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Performs OCR and description on the entire screen."), category=ADDON_NAME)
    def script_ocrFullScreen(self, gesture):
        if self.toggling: self.finish()
        if check_screen_curtain_active():
            return
        self._start_vision(True)

    # Translators: Script description for 'Opens a chat dialog to directly prompt the AI with text or files.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Opens a chat dialog to directly prompt the AI with text or files."), category=ADDON_NAME)
    def script_openDirectChat(self, gesture):
        if self.toggling: self.finish()
        wx.CallAfter(self._open_direct_chat_dialog)

    # Translators: Script description for 'Opens a menu to Explain, Summarize, or Fix the selected text.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Opens a menu to Explain, Summarize, or Fix the selected text."), category=ADDON_NAME)
    def script_refineText(self, gesture):
        if self.toggling: self.finish()
        if self.refine_menu_dlg:
            self.refine_menu_dlg.Raise()
            self.refine_menu_dlg.SetFocus()
            return
        
        captured_text = self._get_text_smart()
        if not captured_text: captured_text = "" 
        
        wx.CallLater(100, self._open_refine_dialog, captured_text)

    # Translators: Script description for 'Shows the last AI response in a chat dialog for review or follow-up questions.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Shows the last AI response in a chat dialog for review or follow-up questions."), category=ADDON_NAME)
    def script_showLastResult(self, gesture):
        if self.toggling: self.finish()
        if self.live_session:
            self._show_live_window()
            return
        if not self._last_result_data:
            # Translators: Message reported when the user tries to show the last result but none is stored.
            ui.message(_("No previous result to show."))
            return
        
        func, args = self._last_result_data
        wx.CallAfter(func, *args, force_show=True, is_recall=True)

    # Translators: Script description for 'Performs smart actions (OCR or Description) on a selected image or PDF file.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Performs smart actions (OCR or Description) on a selected image or PDF file."), category=ADDON_NAME)
    def script_smartFileAction(self, gesture):
        if self.toggling: self.finish()
        if getattr(self, "_dialog_open", False):
            return

        if self._ocr_task_running["smartfile"]:
            self._stop_ocr_task("smartfile")
            return

        focused_paths = get_focused_explorer_files()

        valid_exts = ('.pdf', '.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.heic', '.heif')
        valid_paths = [p for p in focused_paths if p.lower().endswith(valid_exts)]
        if valid_paths:
            threading.Thread(target=self._pre_process_smart_file, args=(valid_paths,), daemon=True).start()
            return
            
        clip_path = self._getClipboardImageFile()
        if clip_path:
            self.report_status(_("Processing clipboard image..."))
            threading.Thread(target=self._pre_process_smart_file, args=([clip_path],), daemon=True).start()
            return
        wx.CallLater(100, self._open_smart_file_dialog)

    # Translators: Script description for 'Shows a list of available commands in the layer.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Translates the text currently in the clipboard."), category=ADDON_NAME)
    def script_translateClipboard(self, gesture):
        if self.toggling: self.finish()
        try:
            t = api.getClipData()
        except Exception:
            t = None
        if t:
            # Translators: Message when calling the command to translate from clipboard
            msg = _("Translating Clipboard...")
            self.report_status(msg)
            threading.Thread(target=self._thread_translate, args=(t,), daemon=True).start()
        else:
            # Translators: Message when the clipboard contains no text to translate
            msg = _("Clipboard empty.")
            self.report_status(msg)

    @scriptHandler.script(description=_("Translates the selected text or navigator object."), category=ADDON_NAME)
    def script_translateSmart(self, gesture):
        if self.toggling: self.finish()
        text = self._get_text_smart()
        
        if not text:
            # Translators: Message reported when calling translation command
            msg = _("No text found.")
            self.report_status(msg)
            return
            
        msg = _("Translating...")
        self.report_status(msg)
        threading.Thread(target=self._thread_translate, args=(text,), daemon=True).start()


