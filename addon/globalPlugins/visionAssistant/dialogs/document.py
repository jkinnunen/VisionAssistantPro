# -*- coding: utf-8 -*-
import os
import sys
import threading
import logging
import base64
import time
import subprocess
import wave
import wx

import addonHandler
import config
import ui
import core

from concurrent.futures import ThreadPoolExecutor

try:
    import fitz
except ImportError:
    fitz = None

from .. import vision_config
from .. import plugin_state
from ..ai.core import AIHandler
from ..ai.providers.gemini import GeminiHandler
from ..ai.ocr import ChromeOCREngine
from ..ai.translation import GoogleTranslator
from ..utils.system import (
    get_mime_type,
    show_error_dialog,
    get_file_path,
    markdown_to_html,
    _is_failed_ocr_page,
    OCRProgressStore,
)
from ..prompt_utils import get_prompt_text, apply_prompt_template

log = logging.getLogger(__name__)

addonHandler.initTranslation()


class ChatDialog(wx.Dialog):
    instance = None

    def __init__(self, parent, file_path):
        # Translators: Title of the chat dialog
        super().__init__(parent, title=_("Ask about Document"), size=(600, 500), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        ChatDialog.instance = self
        self.file_path = file_path
        self.file_uri = None
        self.mime_type = get_mime_type(file_path)
        self.history = []

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Translators: Label showing the analyzed file name
        lbl_info = wx.StaticText(self, label=_("File: {name}").format(name=os.path.basename(file_path)))
        sizer.Add(lbl_info, 0, wx.ALL, 5)
        self.display = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        sizer.Add(self.display, 1, wx.EXPAND | wx.ALL, 10)
        # Translators: Status message while uploading
        self.display.SetValue(_("Uploading to AI...\n"))

        input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for the chat input field
        input_sizer.Add(wx.StaticText(self, label=_("Your Question:")), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        self.input = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(-1, 30))
        self.input.Bind(wx.EVT_TEXT_ENTER, self.on_send)
        input_sizer.Add(self.input, 1, wx.EXPAND | wx.RIGHT, 5)

        # Translators: Button to send message in a chat dialog
        self.btn_send = wx.Button(self, label=_("Send"))
        self.btn_send.Bind(wx.EVT_BUTTON, self.on_send)
        self.btn_send.Disable()
        input_sizer.Add(self.btn_send, 0)
        sizer.Add(input_sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        threading.Thread(target=self.init_upload, daemon=True).start()

    def on_close(self, event):
        if getattr(self, "mistral_file_id", None):
            threading.Thread(target=AIHandler.delete_mistral_file, args=(self.mistral_file_id,), daemon=True).start()
        ChatDialog.instance = None
        self.Destroy()

    def init_upload(self):
        try:
            p = config.conf["VisionAssistant"]["active_provider"]
            if AIHandler.is_gemini():
                uri = GeminiHandler.upload_for_chat(self.file_path, self.mime_type)
                if uri and not str(uri).startswith("ERROR:"):
                    self.file_uri = uri
                    wx.CallAfter(self.on_ready)
                else:
                    # Translators: Error message shown when uploading a video file fails.
                    err_msg = str(uri)[6:] if uri else _("Upload failed.")
                    wx.CallAfter(show_error_dialog, err_msg)
                    wx.CallAfter(self.Close)
            elif p == "mistral" and "pdf" in self.mime_type.lower():
                file_id, url_or_err = AIHandler.upload_to_mistral_for_chat(self.file_path)
                if file_id:
                    self.mistral_file_id = file_id
                    self.file_uri = url_or_err
                    wx.CallAfter(self.on_ready)
                else:
                    err_msg = url_or_err[6:] if url_or_err and str(url_or_err).startswith("ERROR:") else _("Upload failed.")
                    wx.CallAfter(show_error_dialog, err_msg)
                    wx.CallAfter(self.Close)
            else:
                try:
                    with open(self.file_path, "rb") as f:
                        self.file_data = base64.b64encode(f.read()).decode('utf-8')
                    wx.CallAfter(self.on_ready)
                except Exception as e:
                    wx.CallAfter(show_error_dialog, str(e))
                    wx.CallAfter(self.Close)
        except Exception as e:
            wx.CallAfter(show_error_dialog, str(e))
            wx.CallAfter(self.Close)

    def on_ready(self):
        # Translators: Message shown in the chat area when the file is uploaded and the AI is ready to answer questions.
        self.display.AppendText(_("Ready! Ask your questions.\n"))
        self.btn_send.Enable()
        self.input.SetFocus()

    def on_send(self, event):
        msg = self.input.GetValue().strip()
        if not msg: return
        self.input.Clear()
        self.display.AppendText(f"You: {msg}\n")
        # Translators: Message shown while processing in a chat dialog
        ui.message(_("Thinking..."))
        threading.Thread(target=self.do_chat, args=(msg,), daemon=True).start()

    def do_chat(self, msg):
        p = config.conf["VisionAssistant"]["active_provider"]
        if AIHandler.is_gemini():
            f_data = getattr(self, "file_data", None) if not self.file_uri else None
            resp = GeminiHandler.chat(self.history, msg, self.file_uri, self.mime_type, f_data)
            if str(resp).startswith("ERROR:"):
                wx.CallAfter(show_error_dialog, resp[6:])
                if plugin_state.plugin_instance:
                    plugin_state.plugin_instance.current_status = _("Idle")
                return
            if not self.history:
                u_parts = []
                if self.file_uri: u_parts.append({"file_data": {"mime_type": self.mime_type, "file_uri": self.file_uri}})
                elif f_data: u_parts.append({"inline_data": {"mime_type": self.mime_type, "data": f_data}})
                u_parts.append({"text": msg})
                self.history.append({"role": "user", "parts": u_parts})
            else:
                self.history.append({"role": "user", "parts": [{"text": msg}]})
            self.history.append({"role": "model", "parts": [{"text": resp}]})
        else:
            messages = list(self.history)
            is_pdf = "pdf" in self.mime_type.lower()

            if is_pdf:
                if p == "mistral":
                    if not self.history and self.file_uri:
                        content = [
                            {"type": "text", "text": msg},
                            {"type": "document_url", "document_url": self.file_uri}
                        ]
                        messages.append({"role": "user", "content": content})
                    else:
                        messages.append({"role": "user", "content": msg})
                else:
                    doc_text = ""
                    parent_dlg = self.GetParent()
                    if hasattr(parent_dlg, "page_cache") and parent_dlg.page_cache:
                        cached_keys = sorted(parent_dlg.page_cache.keys())
                        doc_text = "\n\n".join(parent_dlg.page_cache[k] for k in cached_keys)
                    if not doc_text:
                        # Translators: Placeholder text used in document chat when the text is still being extracted or is empty.
                        doc_text = _("[Text extraction in progress or empty]")

                    system_template = get_prompt_text("document_chat_system")
                    system_instr = apply_prompt_template(system_template, [("response_lang", vision_config.get_lang_name("ai_response_language"))])

                    if not self.history:
                        messages.append({"role": "user", "content": f"{system_instr}\n\nContext content:\n{doc_text}"})
                        messages.append({"role": "assistant", "content": get_prompt_text("document_chat_ack") or "Context received."})
                    messages.append({"role": "user", "content": msg})
            else:
                if not self.history and getattr(self, "file_data", None):
                    content = [
                        {"type": "text", "text": msg},
                        {"type": "image_url", "image_url": {"url": f"data:{self.mime_type};base64,{self.file_data}"}}
                    ]
                    messages.append({"role": "user", "content": content})
                else:
                    messages.append({"role": "user", "content": msg})

            resp = AIHandler.call(messages)
            if resp and resp.startswith("ERROR:"):
                wx.CallAfter(show_error_dialog, resp[6:])
                if plugin_state.plugin_instance:
                    plugin_state.plugin_instance.current_status = _("Idle")
                return

            if is_pdf:
                if p == "mistral":
                    if not self.history and self.file_uri:
                        self.history.append({
                            "role": "user",
                            "content": [
                                {"type": "text", "text": msg},
                                {"type": "document_url", "document_url": self.file_uri}
                            ]
                        })
                    else:
                        self.history.append({"role": "user", "content": msg})
                else:
                    if not self.history:
                        self.history.append({"role": "user", "content": f"{system_instr}\n\nContext content:\n{doc_text}"})
                        self.history.append({"role": "assistant", "content": get_prompt_text("document_chat_ack") or "Context received."})
                    self.history.append({"role": "user", "content": msg})
            else:
                if not self.history and getattr(self, "file_data", None):
                     self.history.append({
                         "role": "user",
                         "content": [
                             {"type": "text", "text": msg},
                             {"type": "image_url", "image_url": {"url": f"data:{self.mime_type};base64,{self.file_data}"}}
                         ]
                     })
                else:
                     self.history.append({"role": "user", "content": msg})
            self.history.append({"role": "assistant", "content": resp})

        # Translators: Prefix for an AI message line in the Live Assistant history.
        ai_prefix = _("AI: ")
        wx.CallAfter(self.display.AppendText, f"{ai_prefix}{resp}\n\n")
        core.callLater(0, ui.message, ai_prefix + resp)
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = _("Idle")

class RangeDialog(wx.Dialog):
    def __init__(self, parent, total_pages):
        # Translators: Title of the PDF and document options dialog (range, translation, etc.)
        super().__init__(parent, title=_("Options"), size=(350, 320))
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Translators: Label showing total pages found
        sizer.Add(wx.StaticText(self, label=_("Total Pages (All Files): {count}").format(count=total_pages)), 0, wx.ALL, 10)

        # Translators: Box title for page range selection
        box_range = wx.StaticBoxSizer(wx.VERTICAL, self, _("Range"))
        g_sizer = wx.FlexGridSizer(2, 2, 10, 10)
        # Translators: Label for start page
        g_sizer.Add(wx.StaticText(self, label=_("From:")), 0, wx.ALIGN_CENTER_VERTICAL)
        self.spin_from = wx.SpinCtrl(self, min=1, max=total_pages, initial=1)
        g_sizer.Add(self.spin_from, 1, wx.EXPAND)
        # Translators: Label for end page
        g_sizer.Add(wx.StaticText(self, label=_("To:")), 0, wx.ALIGN_CENTER_VERTICAL)
        self.spin_to = wx.SpinCtrl(self, min=1, max=total_pages, initial=total_pages)
        g_sizer.Add(self.spin_to, 1, wx.EXPAND)
        box_range.Add(g_sizer, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(box_range, 0, wx.EXPAND | wx.ALL, 10)

        box_trans = wx.StaticBoxSizer(wx.VERTICAL, self, _("Translation"))
        # Translators: Checkbox to enable translation
        self.chk_trans = wx.CheckBox(self, label=_("Translate Output"))
        box_trans.Add(self.chk_trans, 0, wx.ALL, 5)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer.Add(wx.StaticText(self, label=_("Target:")), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        self.cmb_lang = wx.Choice(self, choices=vision_config.TARGET_NAMES)
        curr_t_code = config.conf["VisionAssistant"]["target_language"]
        t_idx = next((i for i, x in enumerate(vision_config.TARGET_LIST) if x[1] == curr_t_code), 0)
        self.cmb_lang.SetSelection(t_idx)
        h_sizer.Add(self.cmb_lang, 1)
        box_trans.Add(h_sizer, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(box_trans, 0, wx.EXPAND | wx.ALL, 10)

        # Translators: Label for the checkbox that enables image descriptions during OCR in the extraction dialog
        self.chk_describe_images = wx.CheckBox(self, label=_("Describe images inline during OCR"))
        self.chk_describe_images.SetValue(config.conf["VisionAssistant"].get("describe_images_ocr", True))
        sizer.Add(self.chk_describe_images, 0, wx.ALL | wx.EXPAND, 10)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to start processing
        btn_ok = wx.Button(self, wx.ID_OK, label=_("Start"))
        btn_ok.SetDefault()
        btn_cancel = wx.Button(self, wx.ID_CANCEL, label=_("Cancel"))
        btn_sizer.Add(btn_ok, 0, wx.RIGHT, 10)
        btn_sizer.Add(btn_cancel, 0)
        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.SetSizer(sizer)

        self.chk_trans.Bind(wx.EVT_CHECKBOX, self.on_check)
        self.cmb_lang.Disable()

    def on_check(self, event):
        self.cmb_lang.Enable(self.chk_trans.IsChecked())

    def get_settings(self):
        config.conf["VisionAssistant"]["describe_images_ocr"] = self.chk_describe_images.IsChecked()
        s_val = self.spin_from.GetValue()
        e_val = self.spin_to.GetValue()
        start = min(s_val, e_val) - 1
        end = max(s_val, e_val) - 1
        return {
            'start': start,
            'end': end,
            'translate': self.chk_trans.IsChecked(),
            'lang': vision_config.TARGET_LIST[self.cmb_lang.GetSelection()][1]
        }
        
class DocumentViewerDialog(wx.Dialog):
    def __init__(self, parent, virtual_doc, settings, resume=None):
        # Translators: Title of settings group for Document Reader features
        title_text = f"{vision_config.ADDON_NAME} - {_('Document Reader')}"
        super().__init__(parent, title=title_text, size=(800, 600), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        self.v_doc = virtual_doc
        self.start_page = settings['start']
        self.end_page = settings['end']
        self.do_translate = settings['translate']
        self.target_lang = settings['lang']
        self.range_count = self.end_page - self.start_page + 1
        self.page_cache = {}
        if resume:
            for k, v in resume.get("pages", {}).items():
                self.page_cache[int(k)] = v
        self.current_page = self.start_page
        self.thread_pool = ThreadPoolExecutor(max_workers=5)
        self.abort = False
        self._progress_key = "document|" + "|".join(sorted(list(virtual_doc.file_paths)))

        self.init_ui()
        self.Centre()
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance._ocr_task_running["document"] = True
            plugin_state.plugin_instance._ocr_abort["document"] = False
            plugin_state.plugin_instance.doc_viewer_dlg = self
        threading.Thread(target=self.start_auto_processing, daemon=True).start()

    def _save_doc_progress(self):
        if self.abort:
            return
        OCRProgressStore.save(self._progress_key, {
            "paths": list(self.v_doc.file_paths),
            "start": self.start_page,
            "end": self.end_page,
            "do_translate": self.do_translate,
            "target_lang": self.target_lang if self.do_translate else "",
            "pages": {str(k): v for k, v in self.page_cache.items() if not _is_failed_ocr_page(v)},
        })

    def _on_extraction_complete(self):
        if len(self.page_cache) >= self.range_count:
            OCRProgressStore.clear(self._progress_key)
            if plugin_state.plugin_instance:
                plugin_state.plugin_instance._ocr_task_running["document"] = False
                plugin_state.plugin_instance.current_status = _("Idle")

    def init_ui(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        # Translators: Initial status message
        self.lbl_status = wx.StaticText(panel, label=_("Initializing..."))
        vbox.Add(self.lbl_status, 0, wx.ALL, 5)
        self.txt_content = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        vbox.Add(self.txt_content, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        hbox_nav = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to go to previous page
        self.btn_prev = wx.Button(panel, label=_("Previous (Ctrl+PageUp)"))
        self.btn_prev.Bind(wx.EVT_BUTTON, self.on_prev)
        hbox_nav.Add(self.btn_prev, 0, wx.RIGHT, 5)
        # Translators: Button to go to next page
        self.btn_next = wx.Button(panel, label=_("Next (Ctrl+PageDown)"))
        self.btn_next.Bind(wx.EVT_BUTTON, self.on_next)
        hbox_nav.Add(self.btn_next, 0, wx.RIGHT, 15)
        # Translators: Label for Go To Page
        hbox_nav.Add(wx.StaticText(panel, label=_("Go to:")), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        choices = [str(i+1) for i in range(self.start_page, self.end_page + 1)]
        self.cmb_pages = wx.Choice(panel, choices=choices)
        self.cmb_pages.Bind(wx.EVT_CHOICE, self.on_page_select)
        hbox_nav.Add(self.cmb_pages, 0, wx.RIGHT, 15)
        vbox.Add(hbox_nav, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        show_tts = AIHandler.is_tts_supported()

        hbox_actions = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to Ask questions about the document
        self.btn_ask = wx.Button(panel, label=_("Ask AI (Alt+A)"))
        self.btn_ask.Bind(wx.EVT_BUTTON, self.on_ask)
        hbox_actions.Add(self.btn_ask, 0, wx.RIGHT, 5)

        # Translators: Button to force re-scan
        self.btn_gemini = wx.Button(panel, label=_("Re-scan with AI (Alt+R)"))
        self.btn_gemini.Bind(wx.EVT_BUTTON, self.on_gemini_scan)
        hbox_actions.Add(self.btn_gemini, 0, wx.RIGHT, 5)

        # Translators: Button to generate audio
        self.btn_tts = wx.Button(panel, label=_("Generate Audio (Alt+G)"))
        self.btn_tts.Bind(wx.EVT_BUTTON, self.on_tts)
        hbox_actions.Add(self.btn_tts, 0, wx.RIGHT, 5)
        self.btn_tts.Show(show_tts)

        self.btn_view = wx.Button(panel, label=_("View Formatted"))
        self.btn_view.Bind(wx.EVT_BUTTON, self.on_view)
        hbox_actions.Add(self.btn_view, 0, wx.RIGHT, 5)

        # Translators: Button to save text
        self.btn_save = wx.Button(panel, label=_("Save (Alt+S)"))
        self.btn_save.Bind(wx.EVT_BUTTON, self.on_save_all)
        hbox_actions.Add(self.btn_save, 0)

        vbox.Add(hbox_actions, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        if show_tts:
            hbox_tts = wx.BoxSizer(wx.HORIZONTAL)
            self.lbl_voice = wx.StaticText(panel, label=_("TTS Voice:"))
            hbox_tts.Add(self.lbl_voice, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

            p_name = config.conf["VisionAssistant"]["active_provider"]
            voices = AIHandler.get_voices(p_name) or (vision_config.OPENAI_VOICES if p_name in ["openai", "custom"] else vision_config.GEMINI_VOICES)
            self.voice_sel = wx.Choice(panel)
            for v in voices:
                self.voice_sel.Append(f"{v[0]} - {v[1]}", v[0])
            curr_voice = config.conf["VisionAssistant"]["tts_voice"]
            try:
                v_idx = next(i for i, v in enumerate(voices) if v[0] == curr_voice)
                self.voice_sel.SetSelection(v_idx)
            except Exception: self.voice_sel.SetSelection(0)
            if p_name == "minimax":
                threading.Thread(target=self._refresh_minimax_voices_in_format_dialog, daemon=True).start()

            hbox_tts.Add(self.voice_sel, 1, wx.EXPAND)
            vbox.Add(hbox_tts, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        # Translators: Button to close chat dialog
        btn_close = wx.Button(panel, wx.ID_CLOSE, label=_("Close"))
        btn_close.Bind(wx.EVT_BUTTON, self.on_close)
        vbox.Add(btn_close, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        panel.SetSizer(vbox)
        accel_list = [
            (wx.ACCEL_CTRL, wx.WXK_PAGEDOWN, self.btn_next.GetId()),
            (wx.ACCEL_CTRL, wx.WXK_PAGEUP, self.btn_prev.GetId()),
            (wx.ACCEL_CTRL, ord('S'), self.btn_save.GetId()),
            (wx.ACCEL_ALT, ord('S'), self.btn_save.GetId()),
            (wx.ACCEL_ALT, ord('A'), self.btn_ask.GetId()),
            (wx.ACCEL_ALT, ord('R'), self.btn_gemini.GetId())
        ]
        if show_tts:
            accel_list.append((wx.ACCEL_ALT, ord('G'), self.btn_tts.GetId()))

        self.SetAcceleratorTable(wx.AcceleratorTable(accel_list))
        self.cmb_pages.SetSelection(0)

        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.update_view()
        self.txt_content.SetFocus()

    def on_close(self, event):
        self.abort = True
        self.thread_pool.shutdown(wait=False)
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance._ocr_task_running["document"] = False
            plugin_state.plugin_instance.current_status = _("Idle")
            if getattr(plugin_state.plugin_instance, "doc_viewer_dlg", None) is self:
                plugin_state.plugin_instance.doc_viewer_dlg = None
        self.Destroy()

    def start_auto_processing(self):
        self._save_doc_progress()
        if plugin_state.plugin_instance:
            # Translators: Message reported when extracting text from a file
            plugin_state.plugin_instance.current_status = _("Extracting Text...")
            core.callLater(0, ui.message, plugin_state.plugin_instance.current_status)

        p = config.conf["VisionAssistant"]["active_provider"]
        engine = config.conf["VisionAssistant"]["ocr_engine"]

        if engine == 'gemini' and AIHandler.is_gemini():
            threading.Thread(target=self.gemini_scan_batch_thread, daemon=True).start()
        elif engine == 'gemini' and p == "mistral":
            threading.Thread(target=self.mistral_scan_batch_thread, daemon=True).start()
        else:
            for i in range(self.start_page, self.end_page + 1):
                if i in self.page_cache:
                    continue
                self.thread_pool.submit(self.process_page_worker, i)

    @staticmethod
    def _extract_text_layer_from_page(page):
        blocks = page.get_text("blocks", sort=True)
        processed_blocks = []

        for b in blocks:
            lines = [l.strip() for l in b[4].splitlines() if l.strip()]
            if not lines:
                continue

            if lines[0] == ':' and len(lines) > 1:
                lines[1] = lines[1] + ':'
                lines.pop(0)

            block_text = " ".join(lines)

            if block_text.startswith(':') and any('؀' <= c <= 'ۿ' for c in block_text):
                parts = block_text[1:].strip().split(' ', 1)
                if len(parts) > 1:
                    block_text = parts[0] + ': ' + parts[1]
                else:
                    block_text = parts[0] + ':'

            processed_blocks.append(block_text)

        return "\n".join(processed_blocks)

    def process_page_worker(self, page_num):
        if page_num in self.page_cache: return
        if self.abort: return
        text = self._get_page_text_logic(page_num)
        if self.abort: return
        self.page_cache[page_num] = text
        self._save_doc_progress()

        is_complete = len(self.page_cache) >= self.range_count
        if not is_complete and plugin_state.plugin_instance:
            completed = len(self.page_cache)
            # Translators: Status message showing page-by-page progress during file OCR.
            progress_msg = _("Processing page {current} of {total}...").format(current=completed, total=self.range_count)
            plugin_state.plugin_instance.current_status = progress_msg

        self._on_extraction_complete()

        if page_num == self.current_page:
            wx.CallAfter(self.update_view)
            # Translators: Spoken message when the current page is ready
            core.callLater(0, ui.message, _("Page {num} ready").format(num=page_num + 1))

    def _get_page_text_logic(self, page_num):
        file_path, page_idx = self.v_doc.get_page_info(page_num)
        if not file_path: return ""
        doc = None
        try:
            doc = fitz.open(file_path)
            page = doc.load_page(page_idx)

            engine = config.conf["VisionAssistant"]["ocr_engine"]
            text = None

            if engine == 'none':
                text = self._extract_text_layer_from_page(page)
                if not text:
                    # Translators: Message shown when a PDF has no text layer.
                    text = _("The 'None (Extract Text Layer)' engine cannot process image-based content. Please change the OCR Engine to 'Chrome' or 'AI (Advanced)' in settings.")
            else:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_bytes = pix.tobytes("jpg")

                if engine == 'gemini':
                    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
                    text = AIHandler.ocr(img_b64, "image/jpeg")
                elif engine == 'chrome':
                    text = ChromeOCREngine.recognize(img_bytes)

                if not text or not text.strip():
                    # Translators: Placeholder text when OCR fails
                    text = _("[OCR failed. Try a different AI model or provider.]")

            final_text = str(text) if text else ""
            doc.close()

            if self.do_translate and final_text and not final_text.startswith("["):
                if engine == 'chrome':
                    final_text = GoogleTranslator.translate(final_text, self.target_lang)
                else:
                    final_text = AIHandler.translate(final_text, self.target_lang)

            return final_text
        except Exception as e:
            if doc:
                try: doc.close()
                except Exception: pass
            log.error(f"Page processing failed: {str(e)}")
            # Translators: Error message for page processing failure
            return _("Error processing page.")

    def update_view(self):
        rel_page = self.current_page - self.start_page + 1
        # Translators: Status label format
        self.lbl_status.SetLabel(_("Page {current} of {total}").format(current=rel_page, total=self.range_count))
        if self.current_page in self.page_cache:
            self.txt_content.SetValue(self.page_cache[self.current_page])
            self.txt_content.SetInsertionPoint(0)
            self.txt_content.SetFocus()
        else:
            # Translators: Status when page is loading
            self.txt_content.SetValue(_("Processing in background..."))
            self.txt_content.SetInsertionPoint(0)
            self.txt_content.SetFocus()
        self.btn_prev.Enable(self.current_page > self.start_page)
        self.btn_next.Enable(self.current_page < self.end_page)

    def load_page(self, page_num):
        if page_num < self.start_page or page_num > self.end_page: return
        self.current_page = page_num
        self.cmb_pages.SetSelection(page_num - self.start_page)
        # Translators: Spoken message when switching pages
        ui.message(_("Page {num}").format(num=page_num + 1))
        self.update_view()

    def on_prev(self, event):
        if self.current_page > self.start_page: self.load_page(self.current_page - 1)

    def on_next(self, event):
        if self.current_page < self.end_page: self.load_page(self.current_page + 1)

    def on_page_select(self, event):
        self.load_page(self.start_page + self.cmb_pages.GetSelection())

    def on_view(self, event):
        include_page_nums = config.conf["VisionAssistant"].get("document_export_page_numbers", True)
        full_html = []
        for i in range(self.start_page, self.end_page + 1):
            if i in self.page_cache:
                page_text = self.page_cache[i]
                page_content = markdown_to_html(page_text, full_page=False)
                if include_page_nums:
                    page_label = _("Page {num}").format(num=i+1)
                    full_html.append(f"<h2>{page_label}</h2>")
                full_html.append(page_content)
                if include_page_nums:
                    full_html.append("<hr>")
                elif i != self.end_page:
                    full_html.append("<br><br>")

        if not full_html:
            text = self.txt_content.GetValue()
            if not text: return
            full_html.append(markdown_to_html(text, full_page=False))

        combined_html = "".join(full_html)
        try:
            # Translators: Title of the formatted result window
            ui.browseableMessage(combined_html, _("Formatted Content"), isHtml=True)
        except Exception as e:
            show_error_dialog(str(e))

    def on_gemini_scan(self, event):
        p = config.conf["VisionAssistant"]["active_provider"]
        keys = AIHandler.get_keys(p)
        if not keys:
            # Translators: Message box content for successful save
            wx.MessageBox(_("No API Keys configured."), _("Error"), wx.ICON_ERROR)
            return
        menu = wx.Menu()
        # Translators: Menu option for current page
        item_curr = menu.Append(wx.ID_ANY, _("Current Page"))
        # Translators: Menu option for all pages
        item_all = menu.Append(wx.ID_ANY, _("All Pages (In Range)"))
        self.Bind(wx.EVT_MENU, self.do_rescan_current, item_curr)
        self.Bind(wx.EVT_MENU, self.do_rescan_all, item_all)
        self.PopupMenu(menu)
        menu.Destroy()

    def do_rescan_current(self, event):
        if self.current_page in self.page_cache: del self.page_cache[self.current_page]
        self.update_view()
        # Translators: Message during manual scan
        ui.message(_("Scanning with AI..."))
        threading.Thread(target=self.gemini_scan_single_thread, args=(self.current_page,), daemon=True).start()

    def gemini_scan_single_thread(self, page_num):
        def _run():
            try:
                file_path, page_idx = self.v_doc.get_page_info(page_num)
                doc = fitz.open(file_path); page = doc.load_page(page_idx)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_bytes = pix.tobytes("jpg"); doc.close()

                img_b64 = base64.b64encode(img_bytes).decode('utf-8')
                text = AIHandler.ocr(img_b64, "image/jpeg")

                if text and text.startswith("ERROR:"):
                    # Translators: Error shown when a specific page scan fails.
                    self.page_cache[page_num] = _("[Scan failed: {err}]").format(err=text[6:])
                else:
                    if self.do_translate:
                        text = AIHandler.translate(text, self.target_lang)
                    # Translators: Message shown when OCR returns no text for a page.
                    self.page_cache[page_num] = text if text else _("[No text detected]")

                if self.current_page == page_num:
                    wx.CallAfter(self.update_view)
                    # Translators: Message when scan is complete
                    core.callLater(0, ui.message, _("Scan complete"))
            except Exception as e:
                # Translators: Generic system error message inside the document viewer.
                self.page_cache[page_num] = _("[Error: {msg}]").format(msg=str(e))
                wx.CallAfter(self.update_view)

        self.thread_pool.submit(_run)

    def do_rescan_all(self, event):
        threading.Thread(target=self.gemini_scan_batch_thread, daemon=True).start()

    def gemini_scan_batch_thread(self):
        engine = config.conf["VisionAssistant"]["ocr_engine"]

        if engine == 'none':
            # Translators: Status message for local text extraction
            msg = _("Extracting text layer...")
            core.callLater(0, ui.message, msg)
            for i in range(self.start_page, self.end_page + 1):
                self.thread_pool.submit(self.process_page_worker, i)
            return

        # Translators: Message when batch scan starts
        msg = _("Batch Processing Started")
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = msg
        core.callLater(0, ui.message, msg)

        raw_batch_size = config.conf["VisionAssistant"].get("ocr_batch_size", 20)
        total_pages = self.end_page - self.start_page + 1

        batch_size = total_pages if raw_batch_size == 0 else raw_batch_size

        for i in range(self.start_page, self.end_page + 1, batch_size):
            if self.abort:
                break
            batch_end = min(i + batch_size - 1, self.end_page)
            if all((idx in self.page_cache) for idx in range(i, batch_end + 1)):
                continue
            current_batch_count = batch_end - i + 1

            # Translators: Status message showing the progress of document scanning. {start} and {end} are page numbers.
            progress_msg = _("Processing pages {start} to {end}...").format(start=i+1, end=batch_end+1)
            if plugin_state.plugin_instance:
                plugin_state.plugin_instance.current_status = progress_msg
            core.callLater(0, ui.message, progress_msg)
            time.sleep(0.1)

            upload_path = self.v_doc.create_merged_pdf(i, batch_end)
            if not upload_path: continue

            try:
                p_text = apply_prompt_template(
                    get_prompt_text("ocr_document_translate" if self.do_translate else "ocr_document_extract"),
                    [("target_lang", self.target_lang), ("response_lang", config.conf["VisionAssistant"]["ai_response_language"])]
                )
                range_str = f"{i+1}-{batch_end+1}"
                results = GeminiHandler.upload_and_process_batch(upload_path, "application/pdf", current_batch_count, prompt=p_text, page_range_text=range_str, abort_checker=lambda: self.abort)
                if self.abort:
                    break
                if results and not str(results[0]).startswith("ERROR:"):
                    for j, text_part in enumerate(results):
                        page_idx = i + j
                        if page_idx <= self.end_page:
                            self.page_cache[page_idx] = text_part.strip()
                    self._save_doc_progress()
                    self._on_extraction_complete()
                    wx.CallAfter(self.update_view)
                else:
                    err_msg = results[0][6:] if results else "Unknown"
                    for j in range(i, batch_end + 1):
                        # Translators: Error shown in the document reader when a page is dropped because the AI output exceeded its limit during batch processing.
                        self.page_cache[j] = _("[Scan failed: {err}]").format(err=err_msg)
                    wx.CallAfter(self.update_view)
            finally:
                if upload_path and os.path.exists(upload_path):
                    try: os.remove(upload_path)
                    except Exception: pass

        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = _("Idle")
        if self.abort:
            return
        self._on_extraction_complete()
        # Translators: Success message shown when all batches of the document have been processed.
        core.callLater(0, ui.message, _("All document pages have been processed."))

    def mistral_scan_batch_thread(self):
        msg = _("Batch Processing Started")
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = msg
        core.callLater(0, ui.message, msg)

        raw_batch_size = config.conf["VisionAssistant"].get("ocr_batch_size", 20)
        total_pages = self.end_page - self.start_page + 1
        batch_size = total_pages if raw_batch_size == 0 else raw_batch_size

        for i in range(self.start_page, self.end_page + 1, batch_size):
            if self.abort:
                break
            batch_end = min(i + batch_size - 1, self.end_page)
            if all((idx in self.page_cache) for idx in range(i, batch_end + 1)):
                continue
            current_batch_count = batch_end - i + 1

            progress_msg = _("Processing pages {start} to {end}...").format(start=i+1, end=batch_end+1)
            if plugin_state.plugin_instance:
                plugin_state.plugin_instance.current_status = progress_msg
            core.callLater(0, ui.message, progress_msg)
            time.sleep(0.1)

            upload_path = self.v_doc.create_merged_pdf(i, batch_end)
            if not upload_path: continue

            try:
                res = AIHandler.ocr(upload_path, "application/pdf")
                if self.abort:
                    break

                if res and not res.startswith("ERROR:"):
                    results = res.split('[[[PAGE_SEP]]]')
                    is_empty_response = len(results) == 1 and not results[0].strip()

                    for j in range(current_batch_count):
                        page_idx = i + j
                        if page_idx <= self.end_page:
                            if is_empty_response:
                                # Translators: Error shown in the document reader when the AI returns an empty response for a batch of pages.
                                self.page_cache[page_idx] = _("[Error: Empty response received from AI. Try reducing the batch size in settings or scanning page-by-page.]")
                            elif j < len(results):
                                page_text = results[j].strip()
                                if self.do_translate and page_text:
                                    page_text = AIHandler.translate(page_text, self.target_lang)
                                self.page_cache[page_idx] = page_text
                            else:
                                self.page_cache[page_idx] = _("[Error: Page skipped during batch processing due to model output limits. Try a smaller batch size in settings.]")

                    self._save_doc_progress()
                    self._on_extraction_complete()
                    wx.CallAfter(self.update_view)
                else:
                    err_msg = res[6:] if res else "Unknown"
                    for j in range(i, batch_end + 1):
                        self.page_cache[j] = _("[Scan failed: {err}]").format(err=err_msg)
                    wx.CallAfter(self.update_view)

            except Exception as e:
                log.error(f"Error in Mistral batch scan: {e}", exc_info=True)
                err_msg = str(e)
                for j in range(i, batch_end + 1):
                    self.page_cache[j] = _("[Scan failed: {err}]").format(err=err_msg)
                wx.CallAfter(self.update_view)

            finally:
                if upload_path and os.path.exists(upload_path):
                    try: os.remove(upload_path)
                    except Exception: pass

        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = _("Idle")
        if self.abort:
            return
        self._on_extraction_complete()
        core.callLater(0, ui.message, _("All document pages have been processed."))

    def on_tts(self, event):
        if not AIHandler.is_tts_supported():
            # Translators: Error message when trying to use TTS with an unsupported provider
            wx.MessageBox(_("TTS is not supported by the current provider or configuration."), _("Error"), wx.ICON_ERROR)
            return

        p = config.conf["VisionAssistant"]["active_provider"]
        keys = AIHandler.get_keys(p)
        if not keys and p != "custom":
            wx.MessageBox(_("No API Keys configured."), _("Error"), wx.ICON_ERROR)
            return

        menu = wx.Menu()
        # Translators: Menu option for TTS current page
        item_curr = menu.Append(wx.ID_ANY, _("Generate for Current Page"))
        # Translators: Menu option for TTS all pages
        item_all = menu.Append(wx.ID_ANY, _("Generate for All Pages (In Range)"))
        self.Bind(wx.EVT_MENU, self.do_tts_current, item_curr)
        self.Bind(wx.EVT_MENU, self.do_tts_all, item_all)
        self.PopupMenu(menu)
        menu.Destroy()

    def do_tts_current(self, event):
        text = self.txt_content.GetValue().strip()
        if not text:
            # Translators: Error message when text field is empty
            wx.MessageBox(_("No text to read."), "Error")
            return
        self._save_tts(text)

    def do_tts_all(self, event):
        threading.Thread(target=self.tts_batch_thread, daemon=True).start()

    def tts_batch_thread(self):
        full_text = []
        # Translators: Message while gathering text
        core.callLater(0, ui.message, _("Gathering text for audio..."))
        for i in range(self.start_page, self.end_page + 1):
            wait_count = 0
            while i not in self.page_cache and wait_count < 600:
                time.sleep(0.1)
                wait_count += 1
            # Translators: Placeholder text shown in the document reader when processing takes too long
            full_text.append(self.page_cache.get(i, _("[Processing timeout]")))
        final_text = "\n".join(full_text).strip()
        if not final_text: return
        wx.CallAfter(self._save_tts, final_text)

    def _save_tts(self, text):
        # Translators: File dialog title for saving audio
        path = get_file_path(_("Save Audio"), "MP3 Files (*.mp3)|*.mp3|WAV Files (*.wav)|*.wav", mode="save")
        if path:
            voice = config.conf["VisionAssistant"]["tts_voice"]
            if hasattr(self, "voice_sel") and self.voice_sel:
                sel = self.voice_sel.GetSelection()
                if sel != wx.NOT_FOUND:
                    voice = self.voice_sel.GetClientData(sel)
            threading.Thread(target=self.tts_worker, args=(text, voice, path), daemon=True).start()

    def tts_worker(self, text, voice, path):
        # Translators: Message while generating audio
        msg = _("Generating Audio...")
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = msg
        core.callLater(0, ui.message, msg)
        try:
            audio_b64, is_raw_pcm = AIHandler.generate_speech(text, voice)
            if not audio_b64 or audio_b64.startswith("ERROR:"):
                 # Translators: Fallback error message during text-to-speech generation.
                 err_msg = audio_b64[6:] if audio_b64 else _("Unknown Error")
                 wx.CallAfter(wx.MessageBox, _("TTS Error: {error}").format(error=err_msg), _("Error"), wx.ICON_ERROR)
                 if plugin_state.plugin_instance:
                     plugin_state.plugin_instance.current_status = _("Idle")
                 return

            missing_padding = len(audio_b64) % 4
            if missing_padding: audio_b64 += '=' * (4 - missing_padding)
            audio_data = base64.b64decode(audio_b64)

            if not is_raw_pcm:
                with open(path, "wb") as f:
                    f.write(audio_data)
            else:
                if path.lower().endswith(".mp3"):
                    lame_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib", "lame.exe")
                    if not os.path.exists(lame_path):
                        # Translators: Error message when the MP3 encoder (LAME) is missing.
                        wx.CallAfter(wx.MessageBox, _("lame.exe not found in lib folder."), "Error", wx.ICON_ERROR)
                        if plugin_state.plugin_instance:
                            plugin_state.plugin_instance.current_status = _("Idle")
                        return
                    process = subprocess.Popen([lame_path, "-r", "-s", "24", "-m", "m", "-b", "128", "--bitwidth", "16", "--resample", "24", "-q", "0", "-", path],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
                    )
                    process.communicate(input=audio_data)
                else:
                    with wave.open(path, "wb") as wf:
                        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(24000); wf.writeframes(audio_data)

            # Translators: Spoken message when audio is saved
            res_msg = _("Audio Saved")
            if plugin_state.plugin_instance:
                plugin_state.plugin_instance.current_status = _("Idle")
            core.callLater(0, ui.message, res_msg)
            # Translators: Success message shown when narration generation is successfully completed with silence detection.
            wx.CallAfter(wx.MessageBox, _("Audio file generated and saved successfully."), _("Success"), wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            if plugin_state.plugin_instance:
                plugin_state.plugin_instance.current_status = _("Idle")
            # Translators: Success message after generating TTS audio.
            wx.CallAfter(wx.MessageBox, _("TTS Error: {error}").format(error=e), _("Error"), wx.ICON_ERROR)

    def on_ask(self, event):
        p = config.conf["VisionAssistant"]["active_provider"]
        keys = AIHandler.get_keys(p)
        if not keys and p != "custom":
            wx.MessageBox(_("No API Keys configured."), _("Error"), wx.ICON_ERROR)
            return
        if ChatDialog.instance:
            ChatDialog.instance.Raise()
            ChatDialog.instance.SetFocus()
            return
        file_path, _unused = self.v_doc.get_page_info(self.current_page)
        if file_path:
            dlg = ChatDialog(self, file_path)
            dlg.Show()

    def on_save_all(self, event):
        wildcard = "Text File (*.txt)|*.txt|HTML File (*.html)|*.html"
        default_name = ""
        if self.v_doc and self.v_doc.file_paths:
            base = os.path.basename(self.v_doc.file_paths[0])
            name, _ext = os.path.splitext(base)
            default_name = name + ".txt"
        # Translators: File dialog title for saving
        path = get_file_path(_("Save"), wildcard, mode="save", default_name=default_name)
        if path:
            is_html = path.lower().endswith('.html')
            self.btn_save.Disable()
            threading.Thread(target=self.save_thread, args=(path, is_html), daemon=True).start()

    def save_thread(self, path, is_html):
        full_content = []
        try:
            for i in range(self.start_page, self.end_page + 1):
                if i not in self.page_cache:
                    # Translators: Message showing save progress
                    wx.CallAfter(self.lbl_status.SetLabel, _("Saving Page {num}...").format(num=i+1))

                wait_count = 0
                while i not in self.page_cache and wait_count < 600:
                    time.sleep(0.1)
                    wait_count += 1
                txt = self.page_cache.get(i, _("[Processing timeout]"))

                include_page_nums = config.conf["VisionAssistant"].get("document_export_page_numbers", True)

                if is_html:
                    h = markdown_to_html(txt)
                    if "<body>" in h: h = h.split("<body>")[1].split("</body>")[0]
                    sep = "" if i == self.start_page else '<br clear="all" style="page-break-before:always" />'
                    if include_page_nums:
                        page_label = _("Page {num}").format(num=i+1)
                        full_content.append(f'{sep}<div dir="auto"><h2>{page_label}</h2>{h}</div>')
                    else:
                        full_content.append(f'{sep}<div dir="auto">{h}</div>')
                else:
                    if include_page_nums:
                        sep = "" if i == self.start_page else "\n"
                        full_content.append(f"{sep}--- Page {i+1} ---\n{txt}\n")
                    else:
                        sep = "" if i == self.start_page else "\n"
                        full_content.append(f"{sep}{txt}\n")
            with open(path, "w", encoding="utf-8-sig") as f:
                if is_html: f.write(f'<!DOCTYPE html><html dir="auto"><head><meta charset="UTF-8"></head><body>{"".join(full_content)}</body></html>')
                else: f.write("\n".join(full_content))
            # Translators: Status label when save is complete
            wx.CallAfter(self.lbl_status.SetLabel, _("Saved"))
            wx.CallAfter(wx.MessageBox, _("File saved successfully."), _("Success"), wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.CallAfter(wx.MessageBox, _("Save Error: {error}").format(error=e), _("Error"), wx.ICON_ERROR)
        finally: wx.CallAfter(self.btn_save.Enable)

    def _refresh_minimax_voices_in_format_dialog(self):
        try:
            config.conf["VisionAssistant"]["minimax_voices_cache"] = ""
            config.conf["VisionAssistant"]["minimax_voices_cache_time"] = 0
            voices = AIHandler.get_voices("minimax")
            if voices and hasattr(self, 'voice_sel') and self.voice_sel:
                wx.CallAfter(self._populate_format_voice_sel, voices)
        except Exception as e:
            log.warning(f"Background MiniMax voice refresh (format dialog) failed: {e}")

    def _populate_format_voice_sel(self, voices):
        try:
            if not hasattr(self, 'voice_sel') or not self.voice_sel:
                return
            self.voice_sel.Clear()
            for v in voices:
                self.voice_sel.Append(f"{v[0]} - {v[1]}", v[0])
            curr_voice = config.conf["VisionAssistant"].get("tts_voice", "English_expressive_narrator")
            for i in range(self.voice_sel.GetCount()):
                if self.voice_sel.GetClientData(i) == curr_voice:
                    self.voice_sel.SetSelection(i)
                    return
            if self.voice_sel.GetCount() > 0:
                self.voice_sel.SetSelection(0)
        except Exception as e:
            log.warning(f"Failed to populate format voice_sel: {e}")
