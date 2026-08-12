# -*- coding: utf-8 -*-
import os
import sys
import threading
import logging
import base64
import json
import re
import time
import subprocess
import wave
import shutil
import tempfile
import zipfile

import wx

import addonHandler
import config
import ui
import core
import gui
import tones
import synthDriverHandler

import comtypes.client

from .. import vision_config
from .. import plugin_state
from ..ai.core import AIHandler
from ..ai.providers.gemini import GeminiHandler
from ..utils.system import show_error_dialog
from ..utils.media_capture import get_proxy_opener, _MinimalWebSocket, ensure_ffmpeg

log = logging.getLogger(__name__)

addonHandler.initTranslation()

lib_dir = os.path.join(os.path.dirname(__file__), "..", "lib")


class LiveAssistantDialog(wx.Dialog):
    instance = None

    def __init__(self, parent, start_callback, end_callback):
        # Translators: Title of the Live Assistant conversation window.
        title_text = _("{name} - Live Assistant").format(name=vision_config.ADDON_NAME)
        super().__init__(parent, title=title_text, size=(500, 500), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.start_callback = start_callback
        self.end_callback = end_callback
        self.is_active = True
        LiveAssistantDialog.instance = self

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label for the conversation history area in the Live Assistant window.
        sizer.Add(wx.StaticText(panel, label=_("Conversation:")), 0, wx.ALL, 5)
        self.history = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        sizer.Add(self.history, 1, wx.EXPAND | wx.ALL, 5)

        hbox_voice = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for TTS Voice selection in the Live Assistant window.
        hbox_voice.Add(wx.StaticText(panel, label=_("&TTS Voice:")), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        self.voice_sel = wx.Choice(panel, choices=[f"{v[0]} - {v[1]}" for v in vision_config.GEMINI_VOICES])
        curr_voice = config.conf["VisionAssistant"].get("tts_voice", "Puck")
        for i, v in enumerate(vision_config.GEMINI_VOICES):
            if v[0] == curr_voice:
                self.voice_sel.SetSelection(i)
                break
        else:
            if self.voice_sel.GetCount() > 0:
                self.voice_sel.SetSelection(0)

        self.voice_sel.Bind(wx.EVT_CHOICE, self.on_voice_change)
        hbox_voice.Add(self.voice_sel, 1, wx.EXPAND)
        sizer.Add(hbox_voice, 0, wx.EXPAND | wx.ALL, 5)

        hbox_thinking = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for Thinking Depth selection in the Live Assistant window.
        hbox_thinking.Add(wx.StaticText(panel, label=_("Thinking &Depth:")), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        self.thinking_choices = [
            # Translators: Thinking level option for no reasoning (lowest latency)
            (_("Minimal (Fastest)"), "minimal"),
            # Translators: Thinking level option for slight reasoning
            (_("Low (Agentic)"), "low"),
            # Translators: Thinking level option for standard reasoning (balanced)
            (_("Medium (Balanced)"), "medium"),
            # Translators: Thinking level option for deep reasoning
            (_("High (Deep)"), "high")
        ]
        self.thinking_sel = wx.Choice(panel, choices=[x[0] for x in self.thinking_choices])
        curr_thinking = config.conf["VisionAssistant"].get("live_thinking_level", "medium")
        for i, x in enumerate(self.thinking_choices):
            if x[1] == curr_thinking:
                self.thinking_sel.SetSelection(i)
                break
        else:
            self.thinking_sel.SetSelection(2)

        self.thinking_sel.Bind(wx.EVT_CHOICE, self.on_thinking_change)
        hbox_thinking.Add(self.thinking_sel, 1, wx.EXPAND)
        sizer.Add(hbox_thinking, 0, wx.EXPAND | wx.ALL, 5)

        # Translators: Button that ends the live voice conversation.
        self.toggle_btn = wx.Button(panel, label=_("&End"))
        self.toggle_btn.Bind(wx.EVT_BUTTON, self.on_toggle)
        sizer.Add(self.toggle_btn, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        panel.SetSizer(sizer)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(main_sizer)

        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.history.SetFocus()

    def on_voice_change(self, event):
        sel = self.voice_sel.GetSelection()
        if sel != wx.NOT_FOUND:
            config.conf["VisionAssistant"]["tts_voice"] = vision_config.GEMINI_VOICES[sel][0]
            if self.is_active:
                # Translators: Message shown in conversation log when voice is changed
                self.append_line(_("--- Changing voice, reconnecting... ---"))
                self._restart_session()

    def on_thinking_change(self, event):
        sel = self.thinking_sel.GetSelection()
        if sel != wx.NOT_FOUND:
            config.conf["VisionAssistant"]["live_thinking_level"] = self.thinking_choices[sel][1]
            if self.is_active:
                # Translators: Message shown in conversation log when thinking depth is changed
                self.append_line(_("--- Changing thinking depth, reconnecting... ---"))
                self._restart_session()

    def _restart_session(self):
        if self.end_callback:
            self.end_callback()

        def restart():
            if self.start_callback:
                self.start_callback()

        wx.CallLater(1200, restart)

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()

    def append_line(self, line):
        self.history.AppendText(line + "\n")

    def append_raw(self, text):
        self.history.AppendText(text)

    def set_active(self, active):
        self.is_active = active
        # Translators: Button that ends the live voice conversation.
        self.toggle_btn.SetLabel(_("&End") if active else _("&Start"))

    def on_toggle(self, event):
        if self.is_active:
            if self.end_callback:
                self.end_callback()
        else:
            if self.start_callback:
                self.start_callback()

    def on_close(self, event):
        if self.is_active and self.end_callback:
            self.end_callback()
        LiveAssistantDialog.instance = None
        self.Destroy()


class DubbingDialog(wx.Dialog):
    def __init__(self, parent, is_dubbing=True):
        self.is_dubbing = is_dubbing
        if is_dubbing:
            # Translators: Title of the dubbing options dialog
            title = _("Dubbing Options")
        else:
            # Translators: Title of the translation options dialog
            title = _("Translation Options")
        super().__init__(parent, title=title, size=(350, 200) if not is_dubbing else (350, 150))
        sizer = wx.BoxSizer(wx.VERTICAL)

        g_sizer = wx.FlexGridSizer(2, 2, 10, 10)

        if not is_dubbing:
            g_sizer.Add(wx.StaticText(self, label=_("Source:")), 0, wx.ALIGN_CENTER_VERTICAL)
            self.cmb_source = wx.Choice(self, choices=vision_config.SOURCE_NAMES)
            curr_s_code = config.conf["VisionAssistant"]["source_language"]
            s_idx = next((i for i, x in enumerate(vision_config.SOURCE_LIST) if x[1] == curr_s_code), 0)
            self.cmb_source.SetSelection(s_idx)
            g_sizer.Add(self.cmb_source, 1, wx.EXPAND)

        g_sizer.Add(wx.StaticText(self, label=_("Target:")), 0, wx.ALIGN_CENTER_VERTICAL)
        self.cmb_target = wx.Choice(self, choices=vision_config.TARGET_NAMES)
        curr_t_code = config.conf["VisionAssistant"]["target_language"]
        t_idx = next((i for i, x in enumerate(vision_config.TARGET_LIST) if x[1] == curr_t_code), 0)
        self.cmb_target.SetSelection(t_idx)
        g_sizer.Add(self.cmb_target, 1, wx.EXPAND)

        sizer.Add(g_sizer, 1, wx.EXPAND | wx.ALL, 15)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(self, wx.ID_OK, label=_("Start"))
        btn_ok.SetDefault()
        # Translators: Button to add a label for the selected element
        btn_cancel = wx.Button(self, wx.ID_CANCEL, label=_("Cancel"))
        btn_sizer.Add(btn_ok, 0, wx.RIGHT, 10)
        btn_sizer.Add(btn_cancel, 0)
        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.SetSizer(sizer)

    def get_settings(self):
        if not getattr(self, "is_dubbing", True):
            s_idx = self.cmb_source.GetSelection()
            source_lang = vision_config.SOURCE_NAMES[s_idx]
        else:
            source_lang = "Auto-detect"

        t_idx = self.cmb_target.GetSelection()
        return source_lang, vision_config.TARGET_NAMES[t_idx]


class VideoSourceDialog(wx.Dialog):
    def __init__(self, parent):
        # Translators: Title of the video analysis dialog
        title = _("{name} - Analyze Video").format(name=vision_config.ADDON_NAME)
        super().__init__(parent, title=title, size=(550, 290))
        self.local_path = None

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Translators: Label instructing the user to enter a URL or browse for a local video
        lbl = wx.StaticText(self, label=_("Enter Video URL (YouTube, Instagram, Twitter, TikTok) or Browse for a local video:"))
        sizer.Add(lbl, 0, wx.ALL, 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.url_input = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        hbox.Add(self.url_input, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        # Translators: Button to browse for a local video file
        btn_browse = wx.Button(self, label=_("&Browse..."))
        btn_browse.Bind(wx.EVT_BUTTON, self.on_browse)
        hbox.Add(btn_browse, 0, wx.ALIGN_CENTER_VERTICAL)

        sizer.Add(hbox, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Translators: Option to generate an Audio Description SRT file.
        choices = [_("General Video Analysis"), _("Generate Audio Description (SRT File)")]
        self.action_choice = wx.RadioBox(
            self,
            # Translators: Label for the video action radio box
            label=_("Action"),
            choices=choices,
            majorDimension=1,
            style=wx.RA_SPECIFY_COLS
        )
        sizer.Add(self.action_choice, 0, wx.EXPAND | wx.ALL, 10)

        self.action_choice.Bind(wx.EVT_RADIOBOX, self.on_action_change)

        # Translators: Checkbox label to add character list as the first subtitle in video SRT output.
        self.chars_as_sub_check = wx.CheckBox(self, label=_("Add character list as first subtitle"))
        self.chars_as_sub_check.SetValue(config.conf["VisionAssistant"].get("video_chars_as_subtitle", True))
        sizer.Add(self.chars_as_sub_check, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        self.chars_as_sub_check.Show(False)

        # Translators: Checkbox label to add an AI warning disclaimer at the beginning of the video SRT output.
        self.disclaimer_check = wx.CheckBox(self, label=_("Add AI disclaimer at the beginning"))
        self.disclaimer_check.SetValue(config.conf["VisionAssistant"].get("video_add_disclaimer", True))
        sizer.Add(self.disclaimer_check, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        self.disclaimer_check.Show(False)

        btn_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer.Add(btn_sizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(sizer)
        self.url_input.SetFocus()

    def on_browse(self, event):
        # Translators: Filter for video files in the file dialog
        wildcard = _("Video Files") + " (*.mp4;*.avi;*.mkv;*.mov;*.wmv;*.flv;*.webm)|*.mp4;*.avi;*.mkv;*.mov;*.wmv;*.flv;*.webm"
        # Translators: Title of the file dialog for selecting a video
        with wx.FileDialog(self, _("Select Local Video"), wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.local_path = dlg.GetPath()
                self.url_input.SetValue(self.local_path)

    def on_action_change(self, event):
        is_srt = (self.action_choice.GetSelection() == 1)
        self.chars_as_sub_check.Show(is_srt)
        self.disclaimer_check.Show(is_srt)
        self.Layout()


class VideoSRTProgressDialog(wx.Dialog):
    def __init__(self, parent, regenerate_cb=None, original_path=None):
        # Translators: Title of the progress dialog when generating SRT
        title = _("{name} - Generating Audio Description").format(name=vision_config.ADDON_NAME)
        super().__init__(parent, title=title, size=(550, 480), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.srt_content = None
        self.abort = False
        self.regenerate_cb = regenerate_cb
        self.original_path = original_path
        self.file_uri = None
        self.is_srt_done = False
        self.cache_dir = tempfile.mkdtemp(prefix="nvda_va_cache_")
        self._gemini_tts_cache = {}

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label for the status log text box
        lbl = wx.StaticText(self, label=_("Process Status / Subtitle Content:"))
        sizer.Add(lbl, 0, wx.ALL, 10)
        self.txt_status = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        sizer.Add(self.txt_status, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        hbox_voice = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for selecting the Windows TTS voice
        self.lbl_voice = wx.StaticText(self, label=_("Narration Voice:"))
        hbox_voice.Add(self.lbl_voice, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        self.voice_sel = wx.Choice(self, choices=[])
        self.voice_sel.Bind(wx.EVT_CHOICE, self.on_voice_change)
        hbox_voice.Add(self.voice_sel, 1, wx.EXPAND)
        self.voice_sel.Disable()
        sizer.Add(hbox_voice, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.hbox_variant = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for selecting the eSpeak voice variant
        self.lbl_variant = wx.StaticText(self, label=_("eSpeak Voice Variant:"))
        self.hbox_variant.Add(self.lbl_variant, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        self.espeak_variant_sel = wx.ComboBox(self, style=wx.TE_PROCESS_ENTER)
        self.espeak_variant_sel.Bind(wx.EVT_TEXT, self.onModelFilter)
        for vname, vid in self._get_espeak_variants():
            self.espeak_variant_sel.Append(vname, vid)
        if self.espeak_variant_sel.GetCount() > 0:
            self.espeak_variant_sel.SetSelection(0)

        self.hbox_variant.Add(self.espeak_variant_sel, 1, wx.EXPAND)

        # Translators: Button to download missing eSpeak-NG
        self.btn_download_espeak = wx.Button(self, label=_("Download eSpeak-NG"))
        self.btn_download_espeak.Bind(wx.EVT_BUTTON, self.on_download_espeak)
        self.hbox_variant.Add(self.btn_download_espeak, 1, wx.EXPAND)

        sizer.Add(self.hbox_variant, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.lbl_variant.Show(False)
        self.espeak_variant_sel.Show(False)
        self.btn_download_espeak.Show(False)
        self.espeak_variant_sel.Disable()
        self.btn_download_espeak.Disable()

        self.hbox_gemini_voice = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for selecting the Gemini Live TTS voice
        self.lbl_gemini_voice = wx.StaticText(self, label=_("Gemini Voice:"))
        self.hbox_gemini_voice.Add(self.lbl_gemini_voice, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        gemini_choices = [f"{v[0]} ({v[1]})" for v in vision_config.GEMINI_VOICES]
        self.gemini_voice_sel = wx.Choice(self, choices=gemini_choices)
        self.hbox_gemini_voice.Add(self.gemini_voice_sel, 1, wx.EXPAND)

        curr_g_voice = config.conf["VisionAssistant"].get("tts_voice", "Puck")
        g_idx = next((i for i, v in enumerate(vision_config.GEMINI_VOICES) if v[0] == curr_g_voice), 0)
        if self.gemini_voice_sel.GetCount() > 0:
            self.gemini_voice_sel.SetSelection(g_idx)

        sizer.Add(self.hbox_gemini_voice, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.lbl_gemini_voice.Show(False)
        self.gemini_voice_sel.Show(False)
        self.gemini_voice_sel.Disable()

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to save the generated SRT file
        self.btn_save = wx.Button(self, label=_("&Save SRT"))
        self.btn_save.Disable()
        self.btn_save.Bind(wx.EVT_BUTTON, self.on_save)

        # Translators: Button to generate a synced MP3 narration using offline TTS
        self.btn_generate_mp3 = wx.Button(self, label=_("&Generate Synced Narration (MP3)"))
        self.btn_generate_mp3.Disable()
        self.btn_generate_mp3.Bind(wx.EVT_BUTTON, self.on_generate_mp3)

        # Translators: Button to regenerate the audio description
        self.btn_regenerate = wx.Button(self, label=_("&Regenerate"))
        self.btn_regenerate.Disable()
        self.btn_regenerate.Bind(wx.EVT_BUTTON, self.on_regenerate)

        # Translators: Button to close the dialog
        self.btn_close = wx.Button(self, wx.ID_CANCEL, label=_("&Close / Cancel"))
        self.btn_close.Bind(wx.EVT_BUTTON, self.on_close)

        btn_sizer.Add(self.btn_save, 0, wx.RIGHT, 5)
        btn_sizer.Add(self.btn_generate_mp3, 0, wx.RIGHT, 5)
        btn_sizer.Add(self.btn_regenerate, 0, wx.RIGHT, 5)
        btn_sizer.Add(self.btn_close, 0)
        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(sizer)
        self.CenterOnParent()
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Translators: Initial status message
        self.update_status(_("Initializing..."))
        self.txt_status.SetFocus()

        threading.Thread(target=self._load_offline_voices, daemon=True).start()

    def _get_espeak_variants(self):
        espeak_dir = os.path.join(lib_dir, "espeak-ng", "espeak-ng-data", "voices", "!v")
        variants = []

        if os.path.exists(espeak_dir):
            try:
                for f in sorted(os.listdir(espeak_dir)):
                    file_path = os.path.join(espeak_dir, f)
                    if os.path.isfile(file_path) and not f.startswith('.'):
                        vid = f
                        vname = vid.capitalize()

                        try:
                            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                                for line in file:
                                    line_clean = line.strip()
                                    if line_clean.lower().startswith("name "):
                                        extracted_name = line_clean[5:].strip()
                                        if extracted_name:
                                            vname = extracted_name.capitalize()
                                            break
                        except Exception:
                            pass

                        variants.append((vname, vid))
            except Exception as e:
                log.error(f"Failed to dynamically parse espeak variants: {e}")

        return variants

    def _update_variant_visibility(self):
        try:
            if not getattr(self, "voice_sel", None): return
            sel = self.voice_sel.GetSelection()
        except Exception: return
        if sel != wx.NOT_FOUND:
            voice_id = self.voice_sel.GetClientData(sel)
            is_espeak = str(voice_id).startswith("espeak")
            is_gemini = str(voice_id) == "gemini_tts"

            self.lbl_gemini_voice.Show(is_gemini)
            self.gemini_voice_sel.Show(is_gemini)
            if is_gemini:
                self.gemini_voice_sel.Enable()
            else:
                self.gemini_voice_sel.Disable()

            if is_espeak:
                exe_path = os.path.join(lib_dir, "espeak-ng", "espeak-ng.exe")
                if os.path.exists(exe_path):
                    self.lbl_variant.Show(True)
                    self.btn_download_espeak.Show(False)
                    self.espeak_variant_sel.Show(True)

                    current_vid = None
                    variants = self._get_espeak_variants()

                    if self.espeak_variant_sel.GetCount() == 0:
                        for vname, vid in variants:
                            self.espeak_variant_sel.Append(vname, vid)

                    is_first_run = not hasattr(self, "_first_variant_run")
                    if is_first_run:
                        self._first_variant_run = False

                    if not is_first_run:
                        v_sel = self.espeak_variant_sel.GetSelection()
                        if v_sel != wx.NOT_FOUND and v_sel < len(variants):
                            current_vid = variants[v_sel][1]

                    if not current_vid:
                        try:
                            synth = synthDriverHandler.getSynth()
                            if synth.name == "espeak":
                                current_vid = getattr(synth, "variant", "max")
                            else:
                                current_vid = "max"
                        except Exception:
                            current_vid = "max"

                    match_idx = 0
                    for i, (vname, vid) in enumerate(variants):
                        if vid == current_vid:
                            match_idx = i
                            break

                    if self.espeak_variant_sel.GetCount() > 0:
                        self.espeak_variant_sel.SetSelection(match_idx)

                    if self.is_srt_done:
                        self.espeak_variant_sel.Enable()
                        self.btn_generate_mp3.Enable()
                    else:
                        self.espeak_variant_sel.Disable()
                        self.btn_generate_mp3.Disable()
                else:
                    self.lbl_variant.Show(False)
                    self.espeak_variant_sel.Show(False)
                    self.btn_download_espeak.Show(True)
                    self.btn_generate_mp3.Disable()
                    if self.is_srt_done:
                        self.btn_download_espeak.Enable()
                    else:
                        self.btn_download_espeak.Disable()
            else:
                self.lbl_variant.Show(False)
                self.espeak_variant_sel.Show(False)
                self.btn_download_espeak.Show(False)
                if self.is_srt_done:
                    self.btn_generate_mp3.Enable()
                else:
                    self.btn_generate_mp3.Disable()
            self.Layout()

    def onModelFilter(self, event):
        cb = event.GetEventObject()
        if cb.IsFrozen(): return

        sel = cb.GetSelection()
        if sel != wx.NOT_FOUND: return

        query = cb.GetValue()
        query_low = query.lower()

        if not hasattr(cb, '_all_models_backup') and cb.GetCount() > 0:
            cb._all_models_backup = [(cb.GetString(i), cb.GetClientData(i)) for i in range(cb.GetCount())]

        backup = getattr(cb, '_all_models_backup', [])

        if not query_low:
            if cb.GetCount() != len(backup):
                cb.Freeze()
                cb.Clear()
                for name, data in backup:
                    cb.Append(name, data)
                cb.SetValue("")
                cb.Thaw()
            return

        filtered = [(name, data) for name, data in backup if query_low in name.lower()]

        cb.Freeze()
        cb.Clear()
        for name, data in filtered:
            cb.Append(name, data)

        cb.ChangeValue(query)
        cb.SetInsertionPointEnd()
        cb.Thaw()

        if filtered:
            cb.Popup()

    def _generate_espeak_wav(self, text, voice_id, espeak_variant, output_wav):
        espeak_exe = os.path.join(lib_dir, "espeak-ng", "espeak-ng.exe")
        if not os.path.exists(espeak_exe):
            return False

        espeak_voice = "en"
        if voice_id.startswith("espeak_") and voice_id != "espeak_current":
            espeak_voice = voice_id.split("_")[1]

        espeak_speed = "175"
        espeak_pitch = "50"
        espeak_volume = "100"
        espeak_inflection = "75"

        if voice_id == "espeak_current":
            try:
                synth = synthDriverHandler.getSynth()
                if synth.name == "espeak":
                    v = getattr(synth, "voice", "en")
                    if '\\' in v:
                        v = v.split('\\')[-1]
                    espeak_voice = v

                    nvda_rate = getattr(synth, "rate", 50)
                    espeak_speed = str(int(80 + (nvda_rate / 100.0) * 370))

                    nvda_pitch = getattr(synth, "pitch", 50)
                    espeak_pitch = str(int(nvda_pitch))

                    nvda_volume = getattr(synth, "volume", 100)
                    espeak_volume = str(int((nvda_volume / 100.0) * 200))
                    nvda_inflection = getattr(synth, "inflection", 75)
                    espeak_inflection = str(int(nvda_inflection))
            except Exception:
                pass

        ssml_text = f'<speak><prosody range="{espeak_inflection}">{text}</prosody></speak>'

        if espeak_variant:
            espeak_voice = espeak_voice.split('+')[0]
            espeak_voice += f"+{espeak_variant}"

        try:
            subprocess.run(
                [
                    espeak_exe,
                    "-v", espeak_voice,
                    "-s", espeak_speed,
                    "-p", espeak_pitch,
                    "-a", espeak_volume,
                    "-m",
                    "--stdin",
                    "-w", output_wav,
                ],
                input=ssml_text.encode('utf-8'),
                capture_output=True,
                creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
            )
            return os.path.exists(output_wav) and os.path.getsize(output_wav) > 44
        except Exception as e:
            log.error(f"eSpeak generation failed: {e}")
            return False

    def on_voice_change(self, event):
        self._update_variant_visibility()

    def on_download_espeak(self, event):
        threading.Thread(target=self._download_espeak_worker, daemon=True).start()

    def _download_espeak_worker(self):
        espeak_dir = os.path.join(lib_dir, "espeak-ng")
        exe_path = os.path.join(espeak_dir, "espeak-ng.exe")
        wx.CallAfter(self.btn_download_espeak.Disable)
        try:
            # Translators: Status message when downloading eSpeak-NG
            core.callLater(0, self.update_status, _("Downloading eSpeak-NG, please wait..."))
            download_url = "https://raw.githubusercontent.com/mahmoodhozhabri/VisionAssistantPro/main/eSpeak-NG-portable.zip"

            opener = get_proxy_opener(download_url)
            from urllib import request
            req = request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
            zip_path = os.path.join(lib_dir, "espeak-temp.zip")

            with opener.open(req, timeout=300) as response:
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                with open(zip_path, 'wb') as f:
                    while True:
                        chunk = response.read(1024 * 1024)
                        if not chunk: break
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            percent = int((downloaded / total_size) * 100)
                            # Translators: Progress message during eSpeak-NG download
                            status_msg = _("Downloading eSpeak-NG: {percent}%").format(percent=percent)
                            wx.CallAfter(self.txt_status.SetValue, status_msg)
                            if downloaded % (2 * 1024 * 1024) < 1024 * 1024:
                                core.callLater(0, ui.message, status_msg)

            # Translators: Status message when extracting eSpeak-NG
            core.callLater(0, self.update_status, _("Extracting eSpeak-NG..."))
            os.makedirs(espeak_dir, exist_ok=True)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(espeak_dir)
            try: os.remove(zip_path)
            except Exception: pass

            if os.path.exists(exe_path):
                # Translators: Success message after eSpeak-NG download completes
                core.callLater(0, self.update_status, _("eSpeak-NG downloaded successfully!"))
                if self.is_srt_done:
                    core.callLater(0, self.update_status, self.srt_content)
                wx.CallAfter(self._update_variant_visibility)
        except Exception as e:
            log.error(f"eSpeak download failed: {e}", exc_info=True)
            # Translators: Error message when eSpeak-NG download fails
            wx.CallAfter(show_error_dialog, _("Failed to download eSpeak-NG: {error}").format(error=str(e)))
            wx.CallAfter(self.btn_download_espeak.Enable)

    def _load_offline_voices(self):
        try:
            voice_list = []
            target_selection = None

            try:
                synth = synthDriverHandler.getSynth()
                synth_name = getattr(synth, "name", "")
                current_nvda_voice = getattr(synth, "voice", "")
            except Exception:
                synth_name = ""
                current_nvda_voice = ""

            current_voice_item = None

            if synth_name == "espeak":
                # Translators: Option for eSpeak voice matching the user's current NVDA voice settings
                current_voice_item = ("espeak_current", _("eSpeak (Current NVDA Language)"))
                target_selection = "espeak_current"

            sapi5_voices = []
            try:
                engine = comtypes.client.CreateObject("SAPI.SpVoice")
                voices = engine.GetVoices()
                for i in range(voices.Count):
                    voice = voices.Item(i)
                    desc = voice.GetDescription()
                    vid = f"sapi5_{voice.Id}"

                    if synth_name == "sapi5" and current_nvda_voice == voice.Id:
                        current_voice_item = (vid, f"SAPI5 - {desc} (Current)")
                        target_selection = vid
                    else:
                        sapi5_voices.append((vid, f"SAPI5 - {desc}"))
            except Exception as e:
                log.error(f"SAPI5 load failed: {e}")

            if current_voice_item:
                voice_list.append(current_voice_item)

            # Translators: Option to use Gemini Live API for highly realistic text-to-speech
            voice_list.append(("gemini_tts", _("Gemini Live TTS (Online, High Quality)")))

            if synth_name != "espeak":
                # Translators: Option for default English eSpeak voice
                voice_list.append(("espeak_en", _("eSpeak (English Default)")))

            voice_list.extend(sapi5_voices)

            if not target_selection:
                target_selection = "gemini_tts"

            wx.CallAfter(self._populate_voices, voice_list, target_selection)
        except Exception as e:
            log.error(f"Failed to load offline voices: {e}", exc_info=True)

    def _populate_voices(self, voice_list, target_selection):
        try:
            self.voice_sel.Clear()
            for vid, vname in voice_list:
                self.voice_sel.Append(vname, vid)

            if target_selection:
                for i in range(self.voice_sel.GetCount()):
                    if self.voice_sel.GetClientData(i) == target_selection:
                        self.voice_sel.SetSelection(i)
                        self._update_variant_visibility()
                        return

            if self.voice_sel.GetCount() > 0:
                self.voice_sel.SetSelection(0)
                self._update_variant_visibility()
        except Exception:
            pass
        finally:
            if self.is_srt_done:
                self.voice_sel.Enable()

    def update_status(self, msg):
        if self.abort: return
        self.txt_status.SetValue(msg)
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = msg
        ui.message(msg)

    def on_finished(self, srt_content):
        if self.abort: return
        self.srt_content = srt_content
        self.is_srt_done = True
        # Translators: Title of the dialog when generation is successfully finished
        success_title = _("{name} - Audio Description Ready").format(name=vision_config.ADDON_NAME)
        self.SetTitle(success_title)
        self.txt_status.SetValue(srt_content)
        self.btn_save.Enable()
        self.btn_regenerate.Enable()
        self.btn_generate_mp3.Enable()
        self.voice_sel.Enable()
        self._update_variant_visibility()
        self.txt_status.SetFocus()
        tones.beep(1000, 100)
        # Translators: Success announcement when generation is complete
        core.callLater(0, ui.message, _("Audio description generated successfully! You can read the subtitle content in the text box."))

    def on_error(self, err_msg):
        if self.abort: return
        self.is_srt_done = True
        # Translators: Status message when an error occurs during SRT generation
        self.update_status(_("Error: {err}").format(err=err_msg))
        self.btn_regenerate.Enable()
        self.btn_generate_mp3.Disable()
        self.voice_sel.Enable()
        self._update_variant_visibility()

    def on_regenerate(self, event):
        self.srt_content = None
        self.abort = False
        self.is_srt_done = False
        generating_title = _("{name} - Generating Audio Description").format(name=vision_config.ADDON_NAME)
        self.SetTitle(generating_title)
        self.btn_save.Disable()
        self.btn_regenerate.Disable()
        self.btn_generate_mp3.Disable()
        self.voice_sel.Disable()
        self.espeak_variant_sel.Disable()
        self.btn_download_espeak.Disable()
        # Translators: Status message when restarting generation
        self.update_status(_("Re-initializing..."))
        if self.regenerate_cb:
            self.regenerate_cb(self)

    def on_save(self, event):
        if not self.srt_content: return

        default_name = "Audio_Description.srt"
        if getattr(self, "original_path", None):
            if str(self.original_path).startswith("http"):
                default_name = "Online_Video_Description.srt"
            else:
                default_name = os.path.splitext(os.path.basename(self.original_path))[0] + ".srt"

        gui.mainFrame.prePopup()
        try:
            # Translators: File dialog title for saving the generated SRT file
            with wx.FileDialog(gui.mainFrame, _("Save Audio Description"), wildcard="SRT Files (*.srt)|*.srt", defaultFile=default_name, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    path = dlg.GetPath()
                else:
                    path = None
        finally:
            gui.mainFrame.postPopup()
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.srt_content)
                # Translators: Success message when SRT file is saved
                ui.message(_("SRT file saved successfully."))
            except Exception as e:
                show_error_dialog(str(e))

    def _parse_srt(self, srt_text):
        blocks = []
        parts = re.split(r'\n\s*\n', srt_text.strip())
        for part in parts:
            lines = [l.strip() for l in part.strip().split('\n') if l.strip()]
            if len(lines) < 3:
                continue
            time_line = lines[1]
            if '-->' not in time_line:
                continue
            try:
                start_str, end_str = [t.strip() for t in time_line.split('-->')]
                start_ms = self._time_to_ms(start_str)
                end_ms = self._time_to_ms(end_str)
                text = ' '.join(lines[2:])
                blocks.append({'start_ms': start_ms, 'end_ms': end_ms, 'text': text})
            except Exception:
                continue
        return blocks

    def _time_to_ms(self, t):
        h, m, rest = t.replace(',', '.').split(':')
        s, ms = rest.split('.')
        return int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(ms.ljust(3, '0')[:3])

    def _get_wav_duration(self, wav_path):
        try:
            with wave.open(wav_path, 'rb') as wf:
                return wf.getnframes() / wf.getframerate()
        except Exception:
            return 0.0

    def _generate_sapi5_wav(self, text, real_voice_id, output_wav):
        try:
            engine = comtypes.client.CreateObject("SAPI.SpVoice")
            voices = engine.GetVoices()
            for i in range(voices.Count):
                if voices.Item(i).Id == real_voice_id:
                    engine.Voice = voices.Item(i)
                    break

            stream = comtypes.client.CreateObject("SAPI.SpFileStream")
            stream.Open(output_wav, 3)
            engine.AudioOutputStream = stream
            engine.Speak(text)
            stream.Close()
            return os.path.exists(output_wav) and os.path.getsize(output_wav) > 44
        except Exception as e:
            log.error(f"SAPI5 TTS to WAV failed: {e}")
            return False

    def on_generate_mp3(self, event):
        if not self.srt_content:
            return
        blocks = self._parse_srt(self.srt_content)
        if not blocks:
            # Translators: Error when SRT parsing finds no valid subtitle blocks
            show_error_dialog(_("No valid subtitle blocks found in the SRT content."))
            return

        ffmpeg_path = ensure_ffmpeg()
        if not ffmpeg_path:
            return

        sel = self.voice_sel.GetSelection()
        if sel == wx.NOT_FOUND:
            # Translators: Error when no voice is selected
            show_error_dialog(_("Please select an offline voice from the list."))
            return

        voice_id = self.voice_sel.GetClientData(sel)

        gemini_voice = ""
        if voice_id == "gemini_tts":
            g_sel = self.gemini_voice_sel.GetSelection()
            if g_sel != wx.NOT_FOUND:
                gemini_voice = vision_config.GEMINI_VOICES[g_sel][0]
                config.conf["VisionAssistant"]["tts_voice"] = gemini_voice

        espeak_variant = ""
        if str(voice_id).startswith("espeak"):
            v_sel = self.espeak_variant_sel.GetSelection()
            if v_sel != wx.NOT_FOUND:
                espeak_variant = self.espeak_variant_sel.GetClientData(v_sel)

        default_name = "Audio_Narration.mp3"
        video_path = None

        if hasattr(self, "local_path") and self.local_path and os.path.exists(self.local_path):
            video_path = self.local_path
        elif hasattr(self, "original_path") and self.original_path and os.path.exists(self.original_path):
            video_path = self.original_path

        has_video = bool(video_path)

        if not has_video:
            default_name = "Online_Video_Narration.mp3"
            is_online = True
        else:
            if getattr(self, "original_path", None) and not str(self.original_path).startswith("http"):
                default_name = os.path.splitext(os.path.basename(self.original_path))[0] + "_narration.mp3"
            else:
                default_name = "Audio_Narration.mp3"
            is_online = False

        mode_selection = 0
        apply_ducking = False

        if is_online:
            gui.mainFrame.prePopup()
            try:
                # Translators: Warning prompt for online videos indicating that the output will only contain narration.
                warn_msg = _("Because the source is an online video, the final file will ONLY contain the AI voice narration (synced to the timestamps) and will NOT include the original background audio of the video. Do you want to proceed?")
                # Translators: Title of the warning dialog when opening an online video link.
                with wx.MessageDialog(self, warn_msg, _("Online Video Mode"), wx.YES_NO | wx.ICON_WARNING) as dlg:
                    if dlg.ShowModal() != wx.ID_YES:
                        return
            finally:
                gui.mainFrame.postPopup()
        else:
            # Translators: Title of the narration mode selection dialog.
            title_dlg = _("Select Narration Mode")
            # Translators: Instruction prompt for narration mode selection.
            msg_dlg = _("Choose how the narration should be mixed with the video audio:")
            choices_dlg = [
                # Translators: Option for mixing voice directly over the video without pausing.
                _("Standard AD (Mix voice directly over audio - No Pausing)"),
                # Translators: Option for pausing the background video audio during descriptions.
                _("Extended AD (Pause background audio during descriptions)")
            ]

            gui.mainFrame.prePopup()
            try:
                with wx.SingleChoiceDialog(self, msg_dlg, title_dlg, choices_dlg) as dlg:
                    if dlg.ShowModal() != wx.ID_OK:
                        return
                    mode_selection = dlg.GetSelection()
            finally:
                gui.mainFrame.postPopup()

            if mode_selection == 0:
                gui.mainFrame.prePopup()
                try:
                    # Translators: Prompt asking whether to lower the background video audio during the descriptions.
                    duck_msg = _("Do you want to fade/duck the background video audio during the descriptions?")
                    # Translators: Title for the audio ducking prompt.
                    duck_title = _("Audio Ducking")
                    with wx.MessageDialog(self, duck_msg, duck_title, wx.YES_NO | wx.ICON_QUESTION) as dlg:
                        if dlg.ShowModal() == wx.ID_YES:
                            apply_ducking = True
                finally:
                    gui.mainFrame.postPopup()

        gui.mainFrame.prePopup()
        try:
            with wx.FileDialog(
                gui.mainFrame,
                # Translators: Button label or menu item to save the generated AI audio narration synced to the video.
                _("Save Synced Narration"),
                wildcard="MP3 Files (*.mp3)|*.mp3",
                defaultFile=default_name,
                style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
            ) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    output_path = dlg.GetPath()
                else:
                    output_path = None
        finally:
            gui.mainFrame.postPopup()

        if not output_path:
            return
        if not output_path.lower().endswith('.mp3'):
            output_path += '.mp3'

        self.btn_generate_mp3.Disable()
        self.btn_regenerate.Disable()
        self.btn_save.Disable()
        self.voice_sel.Disable()
        self.espeak_variant_sel.Disable()
        self.btn_download_espeak.Disable()

        # Translators: Status message when narration generation starts
        ui.message(_("Generating offline synced narration. This may take a few moments..."))
        threading.Thread(target=self._offline_tts_worker, args=(blocks, output_path, voice_id, espeak_variant, ffmpeg_path, video_path, mode_selection, apply_ducking, gemini_voice), daemon=True).start()

    def _detect_silences(self, ffmpeg_path, video_path, noise_db=-32, duration_sec=0.3):
        startupinfo = None
        creationflags = 0
        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            creationflags = 0x08000000

        vol_cmd = [
            ffmpeg_path, "-y", "-i", video_path, "-vn",
            "-af", "volumedetect", "-f", "null", "-"
        ]
        vol_res = subprocess.run(vol_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, creationflags=creationflags)
        vol_stderr = vol_res.stderr.decode('utf-8', errors='ignore')

        mean_volume = -20.0
        for line in vol_stderr.splitlines():
            if "mean_volume:" in line:
                try:
                    mean_volume = float(line.split("mean_volume:")[1].strip().split()[0])
                except Exception:
                    pass
                break

        dynamic_noise_db = max(-50.0, min(-20.0, mean_volume - 15.0))

        cmd = [
            ffmpeg_path, "-y", "-i", video_path, "-vn",
            "-af", f"highpass=f=200,lowpass=f=3000,afftdn,silencedetect=noise={dynamic_noise_db:.1f}dB:d={duration_sec}",
            "-f", "null", "-"
        ]

        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, creationflags=creationflags)
        stderr_data = res.stderr.decode('utf-8', errors='ignore')

        silences = []
        current_start = None

        for line in stderr_data.splitlines():
            if "silence_start:" in line:
                try:
                    val = line.split("silence_start:")[1].strip().split()[0]
                    current_start = int(float(val) * 1000)
                except Exception:
                    pass
            elif "silence_end:" in line:
                if current_start is not None:
                    try:
                        val = line.split("silence_end:")[1].strip().split("|")[0].strip().split()[0]
                        end_ms = int(float(val) * 1000)
                        silences.append((current_start, end_ms))
                    except Exception:
                        pass
                    current_start = None
        return silences

    def _find_best_pause_time(self, target_ms, silences, max_shift_ms=3000):
        if not silences:
            return target_ms

        for start, end in silences:
            if start <= target_ms <= end:
                return (start + end) // 2

        best_time = target_ms
        min_diff = float('inf')

        for start, end in silences:
            midpoint = (start + end) // 2

            if target_ms < start:
                dist = start - target_ms
            elif target_ms > end:
                dist = target_ms - end
            else:
                dist = 0

            if dist < min_diff and dist <= max_shift_ms:
                min_diff = dist
                best_time = midpoint

        return best_time

    def _offline_tts_worker(self, blocks, output_path, voice_id, espeak_variant, ffmpeg_path, video_path, mode_selection, apply_ducking=False, gemini_voice=""):
        temp_dir = tempfile.mkdtemp()
        try:
            try:
                comtypes.CoInitialize()
            except Exception:
                pass
        except ImportError:
            pass

        try:
            has_video = False
            if video_path and os.path.exists(video_path):
                has_video = True
            else:
                video_path = None
                mode_selection = 0

            orig_audio_wav = os.path.join(temp_dir, "original_audio.wav")
            orig_bytes = None
            total_orig_ms = 0
            silences = []

            if has_video:
                # Translators: Status message shown when extracting the original video audio tracks.
                core.callLater(0, self.update_status, _("Extracting original video audio..."))

                subprocess.run(
                    [
                        ffmpeg_path, "-y",
                        "-i", video_path,
                        "-vn",
                        "-acodec", "pcm_s16le",
                        "-ar", "24000",
                        "-ac", "1",
                        orig_audio_wav
                    ],
                    capture_output=True,
                    creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
                )

                if not os.path.exists(orig_audio_wav):
                    # Translators: Error message shown when extraction of the video's original audio fails.
                    wx.CallAfter(show_error_dialog, _("Failed to extract video audio."))
                    return

                with wave.open(orig_audio_wav, "rb") as wf:
                    orig_bytes = wf.readframes(wf.getnframes())
                    total_orig_ms = int((len(orig_bytes) / 48))

                if mode_selection == 1:
                    # Translators: Status message shown when analyzing the video's audio to detect periods of silence.
                    core.callLater(0, self.update_status, _("Analyzing video for natural silences..."))
                    silences = self._detect_silences(ffmpeg_path, video_path, noise_db=-32, duration_sec=0.3)
            else:
                total_orig_ms = blocks[-1]['end_ms'] + 2000

            gemini_ws_state = {"ws": None}

            def ensure_gemini_connection():
                if gemini_ws_state["ws"] and not getattr(gemini_ws_state["ws"], "closed", True):
                    return True

                if gemini_ws_state["ws"]:
                    try: gemini_ws_state["ws"].close()
                    except: pass
                    gemini_ws_state["ws"] = None

                ws_url = "wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent"
                conf = config.conf["VisionAssistant"]
                default_live = "gemini-3.1-flash-live-preview"
                provider = conf.get("active_provider", "gemini")
                live_model = ""
                if conf.get("advanced_model_routing", False):
                    live_model = conf.get(f"{provider}_live_model", "").strip()
                if not live_model:
                    live_model = conf.get("live_model", default_live).strip()
                if not live_model:
                    live_model = default_live
                if "live" not in live_model.lower():
                    live_model = default_live

                api_keys = AIHandler.get_keys("gemini")
                if not api_keys:
                    return False

                num_keys = len(api_keys)
                start_idx = getattr(GeminiHandler, '_working_key_idx', 0)

                for k_i in range(num_keys):
                    idx = (start_idx + k_i) % num_keys
                    api_key = api_keys[idx]
                    base_host = vision_config.DEFAULT_API_URLS["gemini"].replace("https://", "")
                    try:
                        base = AIHandler.get_base_url("gemini")
                        from urllib.parse import urlparse as _urlparse
                        host = _urlparse(base).hostname
                        if host: base_host = host
                    except: pass

                    ws_path = f"/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={api_key}"

                    max_retries = getattr(GeminiHandler, '_max_retries', 3)
                    attempt = 0
                    while attempt < max_retries:
                        try:
                            ws_candidate = _MinimalWebSocket(base_host, ws_path)
                            ws_candidate.connect()

                            setup_msg = {
                                "setup": {
                                    "model": f"models/{live_model}",
                                    "generationConfig": {
                                        "responseModalities": ["AUDIO"],
                                        "speechConfig": {
                                            "voiceConfig": {
                                                "prebuiltVoiceConfig": {
                                                    "voiceName": gemini_voice or "Puck"
                                                }
                                            }
                                        }
                                    },
                                    "systemInstruction": {
                                        "parts": [{"text": "You are a strict Text-to-Speech engine. You will receive text segments. Your ONLY job is to read them out loud exactly as written. Do not add any conversational fillers, greetings, or extra words. Do not acknowledge instructions. Just speak the text provided. Speak at a very fast and urgent pace."}]
                                    }
                                }
                            }
                            ws_candidate.send_text(json.dumps(setup_msg))

                            start_wait = time.time()
                            setup_success = False
                            while time.time() - start_wait < 10:
                                setup_res = ws_candidate.recv()
                                if setup_res:
                                    op, pay = setup_res
                                    if op is None:
                                        break
                                    if op in (0x1, 0x2):
                                        try:
                                            setup_data = json.loads(pay.decode('utf-8', 'replace'))
                                            if "setupComplete" in setup_data:
                                                setup_success = True
                                                break
                                        except: pass
                                    elif op == 0x9:
                                        try: ws_candidate._send_frame(0xA, pay or b"")
                                        except: pass
                                time.sleep(0.05)

                            if setup_success:
                                gemini_ws_state["ws"] = ws_candidate
                                setattr(GeminiHandler, '_working_key_idx', idx)
                                return True
                            else:
                                ws_candidate.close()

                        except Exception as e:
                            log.error(f"VisionAssistant Offline TTS WebSocket exception: {e}")

                        attempt += 1
                        time.sleep(1)

                return False

            if voice_id == "gemini_tts":
                # Translators: Status message shown when starting connection to Gemini Live API
                core.callLater(0, self.update_status, _("Connecting to Gemini Live API..."))
                if not ensure_gemini_connection():
                    # Translators: Error message shown when connection to Gemini Live API fails
                    wx.CallAfter(show_error_dialog, _("Failed to connect to Gemini Live API."))
                    return

            for i, block in enumerate(blocks):
                if self.abort: return
                text = block['text'].replace('*', '').replace('_', '')
                if not text.strip(): continue

                cache_key = (voice_id, gemini_voice if voice_id=="gemini_tts" else espeak_variant if str(voice_id).startswith("espeak") else "", text)

                wav_path = os.path.join(temp_dir, f"block_{i:04d}.wav")
                success = False

                if cache_key in self._gemini_tts_cache and os.path.exists(self._gemini_tts_cache[cache_key]):
                    wav_path = self._gemini_tts_cache[cache_key]
                    success = True

                if not success:
                    # Translators: Progress message during narration generation. {current} is the current block number, {total} is total blocks.
                    progress_msg = _("Generating narration: part {current} of {total}...").format(current=i + 1, total=len(blocks))
                    core.callLater(0, self.update_status, progress_msg)

                    if str(voice_id).startswith("espeak_"):
                        success = self._generate_espeak_wav(text, voice_id, espeak_variant, wav_path)
                    elif str(voice_id).startswith("sapi5_"):
                        real_id = voice_id[6:]
                        success = self._generate_sapi5_wav(text, real_id, wav_path)
                    elif voice_id == "gemini_tts":
                        pcm_path = os.path.join(temp_dir, f"block_{i:04d}.pcm")
                        req = {
                            "clientContent": {
                                "turns": [
                                    {
                                        "role": "user",
                                        "parts": [{"text": text}]
                                    }
                                ],
                                "turnComplete": True
                            }
                        }

                        for tts_attempt in range(3):
                            if not ensure_gemini_connection():
                                break

                            current_ws = gemini_ws_state["ws"]
                            try:
                                current_ws.send_text(json.dumps(req))
                                with open(pcm_path, "wb") as pf:
                                    start_wait = time.time()
                                    while time.time() - start_wait < 30:
                                        opcode, payload = current_ws.recv()
                                        if opcode is None:
                                            raise ConnectionError("WebSocket dropped during receive.")
                                        if opcode in (0x1, 0x2) and payload:
                                            try:
                                                resp = json.loads(payload.decode('utf-8', 'replace'))
                                                if "serverContent" in resp:
                                                    turn = resp["serverContent"].get("modelTurn") or resp["serverContent"].get("model_turn")
                                                    if turn:
                                                        for part in turn.get("parts", []):
                                                            inline = part.get("inlineData") or part.get("inline_data")
                                                            if inline and inline.get("data"):
                                                                chunk = base64.b64decode(inline["data"])
                                                                pf.write(chunk)
                                                    if resp["serverContent"].get("turnComplete") or resp["serverContent"].get("turn_complete"):
                                                        break
                                            except Exception:
                                                pass
                                        elif opcode == 0x9:
                                            try: current_ws._send_frame(0xA, payload or b"")
                                            except Exception: pass
                                        time.sleep(0.01)

                                if os.path.exists(pcm_path) and os.path.getsize(pcm_path) > 0:
                                    subprocess.run([
                                        ffmpeg_path, "-y",
                                        "-f", "s16le", "-ar", "24000", "-ac", "1",
                                        "-i", pcm_path,
                                        wav_path
                                    ], capture_output=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
                                    if os.path.exists(wav_path):
                                        success = True
                                        break
                            except Exception as e:
                                log.warning(f"Gemini TTS generation failed on attempt {tts_attempt+1}: {e}")
                                if gemini_ws_state["ws"]:
                                    try: gemini_ws_state["ws"].close()
                                    except: pass
                                    gemini_ws_state["ws"] = None
                                time.sleep(1)

                    if success:
                        cache_path = os.path.join(self.cache_dir, f"cache_{hash(cache_key)}.wav")
                        if os.path.abspath(wav_path) != os.path.abspath(cache_path):
                            shutil.copy2(wav_path, cache_path)
                        self._gemini_tts_cache[cache_key] = cache_path

                if success:
                    resampled_wav = os.path.join(temp_dir, f"block_{i:04d}_r.wav")

                    available_ms = block['end_ms'] - block['start_ms']
                    if i + 1 < len(blocks):
                        gap = blocks[i+1]['start_ms'] - block['end_ms']
                        if gap > 0:
                            available_ms += gap

                    target_dur_sec = available_ms / 1000.0
                    actual_dur_sec = self._get_wav_duration(wav_path)

                    af_filter = []
                    if mode_selection == 0 and voice_id == "gemini_tts":
                        if actual_dur_sec > target_dur_sec and target_dur_sec > 0:
                            ratio = actual_dur_sec / target_dur_sec
                            ratio = min(ratio, 2.5)
                            af_filter = ["-af", f"atempo={ratio:.3f}"]

                    cmd = [
                        ffmpeg_path, "-y",
                        "-i", wav_path
                    ] + af_filter + [
                        "-ar", "24000",
                        "-ac", "1",
                        "-c:a", "pcm_s16le",
                        resampled_wav
                    ]

                    subprocess.run(
                        cmd,
                        capture_output=True,
                        creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
                    )

                    if os.path.exists(resampled_wav):
                        block['wav_path'] = resampled_wav
                    else:
                        block['wav_path'] = wav_path
                else:
                    block['wav_path'] = None

            final_wav_path = os.path.join(temp_dir, "final_mix.wav")

            if mode_selection == 0:
                # Translators: Status message when combining audio blocks
                core.callLater(0, self.update_status, _("Arranging audio track... Please wait."))

                tts_base_path = os.path.join(temp_dir, "tts_base.wav")
                final_end_s = total_orig_ms / 1000.0
                subprocess.run(
                    [
                        ffmpeg_path, "-y", "-f", "lavfi", "-t", str(final_end_s),
                        "-i", "anullsrc=r=24000:cl=mono", "-ar", "24000", "-ac", "1", tts_base_path
                    ],
                    capture_output=True,
                    creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
                )

                wav_entries = []
                last_end_ms = 0
                for i, block in enumerate(blocks):
                    w_path = block.get('wav_path')
                    if w_path and os.path.exists(w_path):
                        try:
                            with wave.open(w_path, 'rb') as wf:
                                dur_ms = int((wf.getnframes() / wf.getframerate()) * 1000)
                        except Exception:
                            dur_ms = 0

                        start_ms = int(block['start_ms'])
                        if start_ms < last_end_ms:
                            start_ms = last_end_ms + 150

                        wav_entries.append({
                            'path': w_path,
                            'start_ms': start_ms
                        })
                        last_end_ms = start_ms + dur_ms

                current_tts_mix = tts_base_path
                batch_size = 40
                for batch_start in range(0, len(wav_entries), batch_size):
                    batch = wav_entries[batch_start:batch_start + batch_size]
                    batch_out = os.path.join(temp_dir, f"tts_mix_{batch_start}.wav")

                    cmd = [ffmpeg_path, "-y", "-i", current_tts_mix]
                    filter_parts = []

                    for idx, entry in enumerate(batch):
                        cmd.extend(["-i", entry['path']])
                        delay_ms = int(entry['start_ms'])
                        filter_parts.append(f"[{idx+1}:a]adelay={delay_ms}|{delay_ms}[a{idx+1}]")

                    mix_inputs = "[0:a]" + "".join(f"[a{i+1}]" for i in range(len(batch)))
                    filter_parts.append(f"{mix_inputs}amix=inputs={len(batch)+1}:duration=longest:normalize=0[out]")

                    cmd.extend(["-filter_complex", ";".join(filter_parts), "-map", "[out]", "-ar", "24000", "-ac", "1", batch_out])
                    subprocess.run(cmd, capture_output=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
                    current_tts_mix = batch_out

                if has_video:
                    # Translators: Status message when mixing generated narration with original video audio
                    core.callLater(0, self.update_status, _("Mixing narration with original video audio..."))

                    filter_complex = "[0:a][1:a]amix=inputs=2:duration=longest:normalize=0"
                    if apply_ducking:
                        filter_complex = "[1:a]asplit=2[sc][tts];[0:a][sc]sidechaincompress=threshold=0.05:ratio=5:attack=50:release=1000[bg];[bg][tts]amix=inputs=2:duration=longest:normalize=0"

                    subprocess.run(
                        [
                            ffmpeg_path, "-y",
                            "-i", orig_audio_wav,
                            "-i", current_tts_mix,
                            "-filter_complex", filter_complex,
                            "-ar", "24000", "-ac", "1",
                            final_wav_path
                        ],
                        capture_output=True,
                        creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
                    )
                else:
                    final_wav_path = current_tts_mix

            else:
                # Translators: Status message when slicing and splicing the audio file with natural pauses.
                core.callLater(0, self.update_status, _("Splicing audio based on natural pauses..."))
                output_bytes = bytearray()
                last_copied_ms = 0

                for block in blocks:
                    if self.abort: return
                    if not block.get('wav_path') or not os.path.exists(block['wav_path']):
                        continue

                    raw_start_ms = block['start_ms']
                    
                    tts_dur_ms = 2000
                    try:
                        with wave.open(block['wav_path'], 'rb') as wf_b:
                            tts_dur_ms = int((wf_b.getnframes() / wf_b.getframerate()) * 1000)
                    except Exception:
                        pass

                    smart_start_ms = self._find_best_pause_time(raw_start_ms, silences, req_duration_ms=tts_dur_ms, max_shift_ms=3000)

                    if smart_start_ms > total_orig_ms:
                        smart_start_ms = total_orig_ms

                    if smart_start_ms < last_copied_ms:
                        smart_start_ms = last_copied_ms

                    if smart_start_ms > last_copied_ms:
                        chunk_bytes = orig_bytes[last_copied_ms * 48 : smart_start_ms * 48]
                        output_bytes.extend(chunk_bytes)
                        last_copied_ms = smart_start_ms

                    with wave.open(block['wav_path'], 'rb') as wf_block:
                        tts_frames = wf_block.readframes(wf_block.getnframes())
                        output_bytes.extend(tts_frames)

                if last_copied_ms < total_orig_ms:
                    remaining_bytes = orig_bytes[last_copied_ms * 48 :]
                    output_bytes.extend(remaining_bytes)

                with wave.open(final_wav_path, "wb") as wf_out:
                    wf_out.setnchannels(1)
                    wf_out.setsampwidth(2)
                    wf_out.setframerate(24000)
                    wf_out.writeframes(output_bytes)

            # Translators: Status message shown when converting the final raw WAV mix to MP3 format.
            core.callLater(0, self.update_status, _("Converting final audio to MP3..."))
            subprocess.run(
                [
                    ffmpeg_path, "-y",
                    "-i", final_wav_path,
                    "-ac", "2",
                    "-codec:a", "libmp3lame",
                    "-q:a", "2",
                    output_path
                ],
                capture_output=True,
                creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)
            )

            if os.path.exists(output_path):
                core.callLater(0, self.update_status, self.srt_content)
                # Translators: Message spoken on successful save of the synced narration.
                ui.message(_("Synced extended narration with silence detection saved successfully."))
                wx.CallAfter(wx.MessageBox, _("Synced extended audio narration file generated successfully with smart silence matching."), _("Success"), wx.OK | wx.ICON_INFORMATION)
            else:
                # Translators: Error message shown when the final MP3 conversion fails.
                wx.CallAfter(show_error_dialog, _("Failed to generate the final MP3 file."))

        except Exception as e:
            log.error(f"Synced narration insertion failed: {e}", exc_info=True)
            # Translators: Error message shown when narration generation fails.
            wx.CallAfter(show_error_dialog, _("Narration Error: {error}").format(error=e))
        finally:
            if 'gemini_ws_state' in locals() and gemini_ws_state.get("ws"):
                try: gemini_ws_state["ws"].close()
                except: pass
            try:
                comtypes.CoUninitialize()
            except Exception:
                pass
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except Exception:
                pass
            wx.CallAfter(self.btn_generate_mp3.Enable)
            wx.CallAfter(self.btn_regenerate.Enable)
            wx.CallAfter(self.btn_save.Enable)
            wx.CallAfter(self.voice_sel.Enable)
            wx.CallAfter(self._update_variant_visibility)

    def on_close(self, event):
        self.abort = True
        if plugin_state.plugin_instance:
            # Translators: Error message shown when uploading a video file fails.
            plugin_state.plugin_instance.current_status = _("Idle")
        # Translators: Message announced when user cancels the process
        ui.message(_("Process cancelled."))
        shutil.rmtree(getattr(self, "cache_dir", ""), ignore_errors=True)
        self.Destroy()
