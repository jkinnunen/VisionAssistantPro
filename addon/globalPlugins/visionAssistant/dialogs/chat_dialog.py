# -*- coding: utf-8 -*-
import os
import logging
import threading

import wx
import addonHandler
import config
import api
import ui

from .. import plugin_state
from ..prompt_utils import clean_markdown, markdown_to_html
from ..utils.system import show_error_dialog, get_file_path

log = logging.getLogger(__name__)
addonHandler.initTranslation()


class VisionQADialog(wx.Dialog):
    def __init__(self, parent, title, initial_text, context_data, callback_fn, extra_info=None, raw_content=None, status_callback=None, announce_on_open=True, allow_questions=True, allow_attachments=False):
        super(VisionQADialog, self).__init__(parent, title=title, size=(550, 500), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.context_data = context_data
        self.callback_fn = callback_fn
        self.extra_info = extra_info or {}
        self.chat_history = []
        self.raw_content = raw_content
        self.status_callback = status_callback
        self.announce_on_open = announce_on_open
        self.allow_questions = allow_questions
        self.allow_attachments = allow_attachments
        self.attached_files = []

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        # Translators: Label for the AI response text area in a chat dialog
        lbl_text = _("AI Response:")
        lbl = wx.StaticText(self, label=lbl_text)
        mainSizer.Add(lbl, 0, wx.ALL, 5)
        self.outputArea = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        mainSizer.Add(self.outputArea, 1, wx.EXPAND | wx.ALL, 5)

        self.should_clean = config.conf["VisionAssistant"]["clean_markdown_chat"]

        display_text = None
        history_to_restore = extra_info.get('restore_history') if extra_info else None
        if history_to_restore:
            self.chat_history = history_to_restore[:]
            for h in self.chat_history:
                role = "user" if h.get("role") == "user" else "model"
                text = h.get("parts", [{}])[0].get("text", "")
                if role == "user":
                    # Translators: Format for displaying User message in a chat dialog
                    msg = _("\nYou: {text}\n").format(text=text)
                else:
                    disp = clean_markdown(text) if self.should_clean else text
                    # Translators: Format for displaying AI message in a chat dialog
                    msg = _("AI: {text}\n").format(text=disp)
                    display_text = disp
                self.outputArea.AppendText(msg)
        else:
            display_text = clean_markdown(initial_text) if self.should_clean else initial_text
            if display_text:
                init_msg = _("AI: {text}\n").format(text=display_text)
                self.outputArea.AppendText(init_msg)
                if config.conf["VisionAssistant"]["copy_to_clipboard"]:
                    api.copyToClip(raw_content if raw_content else display_text)

            if not (extra_info and extra_info.get('skip_init_history')):
                 self.chat_history.append({"role": "model", "parts": [{"text": initial_text}]})

            if plugin_state.plugin_instance:
                plugin_state.plugin_instance._last_chat_history = self.chat_history[:]

        self.inputArea = None
        if allow_questions:
            # Translators: Label for user input field in a chat dialog
            ask_text = _("Ask:")
            inputLbl = wx.StaticText(self, label=ask_text)
            mainSizer.Add(inputLbl, 0, wx.ALL, 5)
            self.inputArea = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB, size=(-1, 60))
            mainSizer.Add(self.inputArea, 0, wx.EXPAND | wx.ALL, 5)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.askBtn = None
        self.attachBtn = None
        if allow_questions:
            if self.allow_attachments:
                # Translators: Button to attach files in a chat dialog
                self.attachBtn = wx.Button(self, label=_("&Attach File"))
                self.attachBtn.Bind(wx.EVT_BUTTON, self.on_attach_file)
            # Translators: Button to send message in a chat dialog
            self.askBtn = wx.Button(self, label=_("Send"))
        # Translators: Button to view the content in a formatted HTML window
        self.viewBtn = wx.Button(self, label=_("View Formatted"))
        self.viewBtn.Bind(wx.EVT_BUTTON, self.onView)
        # Translators: Button to save only the result content without chat history
        self.saveContentBtn = wx.Button(self, label=_("Save Content"))
        self.saveContentBtn.Bind(wx.EVT_BUTTON, self.onSaveContent)
        # Translators: Button to save chat in a chat dialog
        self.saveBtn = wx.Button(self, label=_("Save Chat"))
        # Translators: Button to close chat dialog
        self.closeBtn = wx.Button(self, wx.ID_CANCEL, label=_("Close"))

        self.saveBtn.Enable(bool(initial_text.strip()))
        self.viewBtn.Enable(bool(self.raw_content))
        self.saveContentBtn.Enable(bool(self.raw_content))

        if self.askBtn:
            if self.attachBtn:
                btnSizer.Add(self.attachBtn, 0, wx.ALL, 5)
            btnSizer.Add(self.askBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.viewBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.saveContentBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.saveBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.closeBtn, 0, wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(mainSizer)
        if self.inputArea:
            self.inputArea.SetFocus()
        else:
            self.outputArea.SetFocus()
        if self.askBtn:
            self.askBtn.Bind(wx.EVT_BUTTON, self.onAsk)
        self.saveBtn.Bind(wx.EVT_BUTTON, self.onSave)
        if self.inputArea:
            self.inputArea.Bind(wx.EVT_KEY_DOWN, self.onInputKeyDown)
        if display_text and self.announce_on_open:
            wx.CallLater(300, ui.message, display_text)
            
    def onInputKeyDown(self, event):

        if event.GetKeyCode() == wx.WXK_RETURN and not event.ShiftDown():
            self.onAsk(None)
        
        else:
            event.Skip()
            
    def onAsk(self, event):
        if not self.inputArea:
            return
        question = self.inputArea.Value
        if not (question.strip() or self.attached_files): return
        user_msg = _("\nYou: {text}\n").format(text=question)
        self.outputArea.AppendText(user_msg)
        self.inputArea.Clear()
        # Translators: Message shown while processing in a chat dialog
        msg = _("Thinking...")
        ui.message(msg)
        if question.strip() or self.attached_files:
            # Translators: Text appended to the chat window while waiting for the AI to respond.
            wx.CallAfter(self.outputArea.AppendText, _("\nProcessing...\n"))
            self.askBtn.Enable(False)
            if self.attachBtn: self.attachBtn.Enable(False)
            self.saveBtn.Enable(False)
            self.viewBtn.Enable(False)
            self.saveContentBtn.Enable(False)
            if plugin_state.plugin_instance:
                # Translators: Status when the AI is thinking in chat dialog
                plugin_state.plugin_instance.current_status = _("Processing response...")
            threading.Thread(target=self.process_question, args=(question, list(self.attached_files)), daemon=True).start()

    def on_attach_file(self, event):
        wildcard = "All files (*.*)|*.*"
        # Translators: Title of the file selection dialog when attaching a file to a chat.
        with wx.FileDialog(self, _("Select a file to attach"), wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_OK:
                path = fileDialog.GetPath()
                self.attached_files.append(path)
                # Translators: Label for attach button when files are attached
                self.attachBtn.SetLabel(_("Attach File ({count})").format(count=len(self.attached_files)))
                ui.message(_("File attached: {name}").format(name=os.path.basename(path)))

    def process_question(self, question, attachments):
        try:
            self.extra_info['attachments'] = attachments
            result_tuple = self.callback_fn(self.context_data, question, self.chat_history, self.extra_info)

            response_text, _unused = result_tuple if result_tuple else (None, None)
            if response_text:
                if response_text.startswith("ERROR:"):
                    wx.CallAfter(show_error_dialog, response_text[6:])
                    if plugin_state.plugin_instance:
                        # Translators: Error message shown when uploading a video file fails.
                        plugin_state.plugin_instance.current_status = _("Idle")
                    return

                self.chat_history.append({"role": "user", "parts": [{"text": question}]})
                self.chat_history.append({"role": "model", "parts": [{"text": response_text}]})
                if plugin_state.plugin_instance:
                    plugin_state.plugin_instance._last_chat_history = self.chat_history[:]
                
                final_text = clean_markdown(response_text) if self.should_clean else response_text
                wx.CallAfter(self.update_response, final_text, response_text)
        except Exception as e:
            log.error(f"Process question failed: {e}", exc_info=True)
            wx.CallAfter(show_error_dialog, str(e))
        finally:
            self.extra_info.pop('attachments', None)
            self.attached_files = []
            if self.attachBtn:
                wx.CallAfter(self.attachBtn.SetLabel, _("&Attach File"))
            wx.CallAfter(self.askBtn.Enable, True)
            if self.attachBtn: wx.CallAfter(self.attachBtn.Enable, True)
            wx.CallAfter(self.saveBtn.Enable, True)
            wx.CallAfter(self.viewBtn.Enable, True)
            wx.CallAfter(self.saveContentBtn.Enable, True)

    def update_response(self, display_text, raw_text=None):
        if raw_text:
            self.raw_content = raw_text
            self.viewBtn.Enable(True)
            self.saveContentBtn.Enable(True)
        ai_msg = _("AI: {text}\n").format(text=display_text)
        self.outputArea.AppendText(ai_msg)
        self.saveBtn.Enable(True)
        if config.conf["VisionAssistant"]["copy_to_clipboard"]:
            api.copyToClip(raw_text if raw_text else display_text)
        self.outputArea.ShowPosition(self.outputArea.GetLastPosition())
        ui.message(display_text)

    def report_save(self, msg):
        if self.status_callback: self.status_callback(msg)
        else: ui.message(msg)

    def onView(self, event):
        full_html = ""
        user_label = _("\nYou: {text}\n").format(text="").strip()
        ai_label = _("AI: {text}\n").format(text="").strip()

        if self.chat_history:
            for item in self.chat_history:
                role = item.get("role", "")
                text = item.get("parts", [{}])[0].get("text", "")
                if role == "user":
                    safe_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    full_html += f"<h2>{user_label}</h2><p>{safe_text}</p>"
                elif role == "model":
                    formatted_text = markdown_to_html(text, full_page=False)
                    full_html += f"<h2>{ai_label}</h2>{formatted_text}<hr>"

        if not full_html and self.raw_content:
             formatted_text = markdown_to_html(self.raw_content, full_page=False)
             full_html += f"<h2>{ai_label}</h2>{formatted_text}"

        if not full_html: return
        try:
            # Translators: Title of the formatted result window
            ui.browseableMessage(full_html, _("Formatted Conversation"), isHtml=True)
        except Exception as e:
            # Translators: Error message if viewing fails
            msg = _("Error displaying content: {error}").format(error=e)
            show_error_dialog(msg)

    def onSave(self, event):
        # Translators: Save dialog title
        path = get_file_path(_("Save Chat Log"), "Text files (*.txt)|*.txt", mode="save")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f: f.write(self.outputArea.GetValue())
                # Translators: Message shown on successful save of a file.
                self.report_save(_("Saved."))
            except Exception as e:
                # Translators: Message in the error dialog when saving fails.
                msg = _("Save failed: {error}").format(error=e)
                show_error_dialog(msg)

    def onSaveContent(self, event):
        path = get_file_path(_("Save Result"), "HTML files (*.html)|*.html", mode="save")
        if path:
            try:
                full_html = markdown_to_html(self.raw_content, full_page=True)
                with open(path, "w", encoding="utf-8-sig") as f: f.write(full_html)
                self.report_save(_("Saved."))
            except Exception as e:
                msg = _("Save failed: {error}").format(error=e)
                show_error_dialog(msg)
