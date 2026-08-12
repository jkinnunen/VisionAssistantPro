# -*- coding: utf-8 -*-
import sys
import os
import json
import ast
import base64
import threading
import logging
import tempfile
import time
import datetime
import gc
import ctypes
import shutil
import wx

import addonHandler
import globalPluginHandler
import globalVars
import config
import gui
import ui
import core
import api
import tones
import scriptHandler
import controlTypes
import NVDAObjects

lib_dir = os.path.join(os.path.dirname(__file__), "lib")
if lib_dir not in sys.path:
    sys.path.append(lib_dir)

arch_lib_dir = os.path.join(lib_dir, "x64" if sys.maxsize > 2**32 else "x86")
if arch_lib_dir not in sys.path:
    sys.path.insert(0, arch_lib_dir)

log = logging.getLogger(__name__)
addonHandler.initTranslation()

from . import plugin_state
from . import vision_config
from .ai.core import AIHandler
from .utils.system import show_error_dialog, _generate_object_signature, get_file_path, OCRProgressStore, get_mime_type, check_screen_curtain_active, clean_markdown, VirtualDocument
from .utils.media_capture import LiveSession, get_proxy_opener
from .vision_config import LABELS_FILE, ADDON_NAME, GITHUB_REPO, get_lang_name, TARGET_NAMES
from .utils.updater import UpdateManager
from .dialogs.ui_elements import LabelManagerDialog, UIExplorerDialog
from .features.vision import VisionMixin
from .features.screen_capture import ScreenCaptureMixin
from .features.audio import AudioMixin
from .features.video import VideoMixin
from .features.operator_captcha import OperatorCaptchaMixin
from .features.quick_settings import QuickSettingsMixin
from .features.upload import UploadMixin
from .dialogs.settings import SettingsPanel
from .prompt_utils import get_prompt_text, apply_prompt_template, finally_

try:
    import fitz
except ImportError:
    fitz = None
from .dialogs.media import LiveAssistantDialog
from .dialogs.chat_dialog import VisionQADialog
from .dialogs.document import DocumentViewerDialog, RangeDialog
from .dialogs import donate

from urllib import request, error


def check_and_restore_lib_backup():
    def _restore_worker():
        time.sleep(10.0)
        try:
            backup_dir = os.path.join(tempfile.gettempdir(), "VisionAssistant_Lib_Backup")
            manifest_file = os.path.join(backup_dir, "backup_manifest.json")
            if not os.path.exists(manifest_file):
                return

            target_lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
            os.makedirs(target_lib_dir, exist_ok=True)

            for item in os.listdir(backup_dir):
                if item == "backup_manifest.json":
                    continue
                src = os.path.join(backup_dir, item)
                dst = os.path.join(target_lib_dir, item)
                if not os.path.exists(dst):
                    try:
                        if os.path.isdir(src):
                            shutil.copytree(src, dst, dirs_exist_ok=True)
                        else:
                            shutil.copy2(src, dst)
                    except Exception:
                        pass

            shutil.rmtree(backup_dir, ignore_errors=True)
        except Exception:
            pass

    def _start():
        threading.Thread(target=_restore_worker, daemon=True).start()

    wx.CallLater(5000, _start)
    
class CustomLabelOverlay(NVDAObjects.NVDAObject):
    @property
    def name(self):
        instance = plugin_state.plugin_instance
        uniqueId = instance._getAppId(self) if instance else self.appModule.appName

        key = _generate_object_signature(self)
        cache = getattr(instance, "labels_cache", {})
        if uniqueId in cache:
            if key and key in cache[uniqueId]:
                return cache[uniqueId][key]

        return super().name


class GlobalPlugin(globalPluginHandler.GlobalPlugin, VisionMixin, ScreenCaptureMixin,
                   AudioMixin, VideoMixin, OperatorCaptchaMixin, QuickSettingsMixin, UploadMixin):

    scriptCategory = ADDON_NAME

    last_translation = ""
    is_recording = False
    temp_audio_file = os.path.join(tempfile.gettempdir(), "vision_dictate.wav")

    translation_cache = {}
    _last_source_text = None
    _last_params = None
    update_timer = None

    is_ui_explorer_active = False

    _operator_history = []
    _operator_context = {}

    # Translators: Error message shown when uploading a video file fails.
    current_status = _("Idle")

    def __init__(self):
        super(GlobalPlugin, self).__init__()

        plugin_state.plugin_instance = self
        
        try:
            check_and_restore_lib_backup()
        except Exception as be:
            log.warning(f"Lib restore schedule skipped: {be}")


        try:
            from .utils.logging_utils import setup_file_logging
            setup_file_logging()
        except Exception as le:
            log.warning(f"Failed to initialize file logging: {le}")

        if not globalVars.appArgs.secure:
            gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(SettingsPanel)
            self.updater = UpdateManager(GITHUB_REPO)
            self._is_operator_running = False
            self._abort_operator = False
            self._operator_thread_token = 0
            self._dialog_open = False
            self.va_menu = wx.Menu()

            # Translators: Menu item for Document Reader
            item_doc = self.va_menu.Append(wx.ID_ANY, _("&Document Reader..."))
            self.va_menu.Bind(wx.EVT_MENU, lambda e: wx.CallAfter(self._open_document_reader), item_doc)

            # Translators: Menu item for media transcription and dubbing
            item_audio = self.va_menu.Append(wx.ID_ANY, _("Media Transcription and &Dubbing..."))
            self.va_menu.Bind(wx.EVT_MENU, lambda e: wx.CallAfter(self._open_audio), item_audio)

            # Translators: Menu item for Video Analysis
            item_video = self.va_menu.Append(wx.ID_ANY, _("Analyze &Video..."))
            self.va_menu.Bind(wx.EVT_MENU, lambda e: wx.CallAfter(self._open_video_dialog), item_video)

            self.va_menu.AppendSeparator()

            # Translators: Menu item to open settings
            item_settings = self.va_menu.Append(wx.ID_ANY, _("&Settings..."))
            self.va_menu.Bind(wx.EVT_MENU, self.on_settings_click, item_settings)

            # Translators: Menu item to check for updates
            item_update = self.va_menu.Append(wx.ID_ANY, _("Check for &Update"))
            self.va_menu.Bind(wx.EVT_MENU, lambda e: self.updater.check_for_updates(silent=False), item_update)

            # Translators: Menu item to open documentation
            item_help = self.va_menu.Append(wx.ID_ANY, _("Docu&mentation"))
            self.va_menu.Bind(wx.EVT_MENU, self.on_help_click, item_help)

            # Translators: Menu item for donations
            item_donate = self.va_menu.Append(wx.ID_ANY, _("D&onate"))
            self.va_menu.Bind(wx.EVT_MENU, self.on_donate_click, item_donate)

            # Translators: Menu item to open the Telegram channel
            item_telegram = self.va_menu.Append(wx.ID_ANY, _("Telegram &Channel"))
            self.va_menu.Bind(wx.EVT_MENU, self.on_telegram_click, item_telegram)

            self.tools_menu = gui.mainFrame.sysTrayIcon.toolsMenu
            # Translators: The name of the addon's sub-menu in the NVDA Tools menu.
            self.va_submenu_item = self.tools_menu.AppendSubMenu(self.va_menu, _("Vision Assistant"))

            if config.conf["VisionAssistant"]["check_update_startup"]:
                self.update_timer = wx.CallLater(10000, self.updater.check_for_updates, True)

        self.refine_dlg = None
        self.refine_menu_dlg = None
        self.vision_dlg = None
        self.doc_dlg = None
        self.doc_viewer_dlg = None
        self.translation_dlg = None
        self.toggling = False
        self._last_result_data = None
        self.live_session = None
        self.live_dlg = None

        self.is_video_recording = False
        self.recording_process = None
        self.recording_output_path = None
        self.recording_start_time = None

        self.labels_cache = {}
        if os.path.exists(LABELS_FILE):
            try:
                with open(LABELS_FILE, "r", encoding="utf-8") as f:
                    self.labels_cache = json.load(f)
            except Exception: pass

        self._ocr_task_running = {"smartfile": False, "document": False}
        self._ocr_abort = {"smartfile": False, "document": False}

    def _capture_fullscreen_sync(self):
        res = [None, 0, 0, ""]
        evt = threading.Event()
        def do_cap():
            try:
                res[0], res[1], res[2], res[3] = self._capture_fullscreen()
            except Exception: pass
            finally: evt.set()
        core.callLater(0, do_cap)
        evt.wait()
        return res[0], res[1], res[2], res[3]

    def _get_fg_app_name_sync(self):
        res = [""]
        evt = threading.Event()
        def do_get():
            try: res[0] = api.getForegroundObject().appModule.appName
            except Exception: pass
            finally: evt.set()
        core.callLater(0, do_get)
        evt.wait()
        return res[0]

    @staticmethod
    def _ocr_progress_key(context, paths):
        return context + "|" + "|".join(sorted(paths))

    def _stop_ocr_task(self, context):
        self._ocr_abort[context] = True
        self._ocr_task_running[context] = False
        self.current_status = _("Idle")
        # Translators: Announcement when an in-progress OCR extraction is stopped by the user.
        ui.message(_("OCR operation stopped."))
        tones.beep(300, 150)

    def _maybe_resume_ocr(self, context, paths):
        key = self._ocr_progress_key(context, paths)
        record = OCRProgressStore.load(key)
        if not record:
            return None

        total_pages = record.get("end", 0) - record.get("start", 0) + 1
        done_pages = min(len(record.get("pages", {})), total_pages)
        file_count = len(record.get("paths", paths))

        # Translators: Title of the dialog asking whether to resume an OCR operation
        title = _("Unfinished Operation")
        # Translators: Message asking whether to continue an interrupted OCR extraction.
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

    def _open_document_reader(self):
        self._dialog_open = True
        # Translators: File dialog filter for supported files
        wc = _("Supported Files") + "|*.pdf;*.jpg;*.jpeg;*.png;*.tif;*.tiff;*.heic;*.heif"
        self._browse_and_run(self._scan_and_open, wc, multiple=True)
        self._dialog_open = False

    def _scan_and_open(self, paths, resume=None):
        try:
            if not fitz:
                # Translators: Error when PyMuPDF is missing
                wx.CallAfter(wx.MessageBox, _("PyMuPDF library is missing."), "Error", wx.ICON_ERROR)
                return

            engine = config.conf["VisionAssistant"]["ocr_engine"]
            image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.heic', '.heif')
            has_images = any(p.lower().endswith(image_extensions) for p in paths)

            if engine == 'none' and has_images:
                # Translators: Message shown when a PDF has no text layer.
                msg = _("The 'None (Extract Text Layer)' engine cannot process image-based content. Please change the OCR Engine to 'Chrome' or 'AI (Advanced)' in settings.")
                # Translators: Title of the error dialog shown when the selected OCR engine cannot process the chosen image-based files.
                wx.CallAfter(gui.messageBox, msg, _("OCR Engine Error"), wx.OK | wx.ICON_ERROR)
                return

            v_doc = VirtualDocument(paths)
            v_doc.scan()
            if v_doc.total_pages == 0:
                 # Translators: Error when no pages found
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

    def _open_document_viewer(self, v_doc, settings, resume=None):
        self.doc_viewer_dlg = DocumentViewerDialog(gui.mainFrame, v_doc, settings, resume=resume)
        self.doc_viewer_dlg.Show()

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

    def getScript(self, gesture):
        if not self.toggling:
            return super(GlobalPlugin, self).getScript(gesture)

        script = super(GlobalPlugin, self).getScript(gesture)
        if getattr(script, "keep_layer_alive", False):
            return script
        if not script:
            script = finally_(self.script_error, self.finish)
        return finally_(script, self.finish)

    def finish(self):
        self.toggling = False
        self._quick_settings_idx = 0
        self.clearGestureBindings()
        self.bindGestures(self.__gestures)

    def script_error(self, gesture):
        tones.beep(120, 100)
        
    # Translators: Script description for 'Shows a list of available commands in the layer.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Shows a list of available commands in the layer."), category=ADDON_NAME)
    def script_showHelp(self, gesture):
        if self.toggling: self.finish()
        help_msg = (
            "Shift+A: " + _("Asks the AI Operator to perform an action or describe the screen.") + "\n" +
            "E: " + _("Toggles the interactive UI elements explorer.") + "\n" +
            "T: " + _("Translates the selected text or navigator object.") + "\n" +
            "Shift+T: " + _("Translates the text currently in the clipboard.") + "\n" +
            "Control+T: " + _("Records voice, transcribes and translates it using AI, and types the result.") + "\n" +
            # Translators: Script description for 'Opens a menu to Explain, Summarize, or Fix the selected text.' in Input Gestures dialog.
            "R: " + _("Opens a menu to Explain, Summarize, or Fix the selected text.") + "\n" +
            # Translators: Script description for 'Performs OCR and description on the entire screen.' in Input Gestures dialog.
            "O: " + _("Performs OCR and description on the entire screen.") + "\n" +
            # Translators: Script description for 'Describes the current object (Navigator Object).' in Input Gestures dialog.
            "V: " + _("Describes the current object (Navigator Object).") + "\n" +
            # Translators: Script description for 'Opens the Document Reader for detailed page-by-page analysis (PDF/Images).' in Input Gestures dialog.
            "D: " + _("Opens the Document Reader for detailed page-by-page analysis (PDF/Images).") + "\n" +
            # Translators: Script description for 'Performs smart actions (OCR or Description) on a selected image or PDF file.' in Input Gestures dialog.
            "F: " + _("Performs smart actions (OCR or Description) on a selected image or PDF file.") + "\n" +
            # Translators: Script description for 'Transcribes or dubs a selected media file.' in Input Gestures dialog.
            "M: " + _("Transcribes or dubs a selected media file.") + "\n" +
            # Translators: Script description for 'Analyzes a local video file or an online video URL.' in Input Gestures dialog.
            "Shift+V: " + _("Analyzes a local video file or an online video URL.") + "\n" +
            # Translators: Script description for 'Starts or stops local video recording of the screen.' in Input Gestures dialog.
            "Control+V: " + _("Starts or stops local video recording of the screen.") + "\n" +
            # Translators: Script description for 'Attempts to solve a CAPTCHA on the screen or navigator object.' in Input Gestures dialog.
            "C: " + _("Attempts to solve a CAPTCHA on the screen or navigator object.") + "\n" +
            "Shift+C: " + _("Opens a chat dialog to directly prompt the AI with text or files.") + "\n" +
            # Translators: Script description for 'Records voice, transcribes it using AI, and types the result.' in Input Gestures dialog.
            "S: " + _("Records voice, transcribes it using AI, and types the result.") + "\n" +
            "I: " + _("Announces the current status of the add-on.") + "\n" +
            "L: " + _("Labels the current navigator object using AI.") + "\n" +
            "Shift+L: " + _("Manages existing labels or scans the entire app to label unnamed elements.") + "\n" +
            "U: " + _("Checks for updates manually.") + "\n" +
            # Translators: Script description for 'Shows the last AI response in a chat dialog for review or follow-up questions.' in Input Gestures dialog.
            "Space: " + _("Shows the last AI response in a chat dialog for review or follow-up questions.") + "\n" +
            "H: " + _("Shows a list of available commands in the layer.") + "\n" +
            # Translators: Script description for 'Starts or ends a live voice conversation with the AI assistant.' in Input Gestures dialog.
            "Control+L: " + _("Starts or ends a live voice conversation with the AI assistant.") + "\n" +
            # Translators: Script description for 'Opens the Vision Assistant settings dialog.' in Input Gestures dialog.
            "Alt+S: " + _("Opens the Vision Assistant settings dialog.") + "\n" +
            # Translators: Script description for 'Reports the number of Gemini API keys that have exceeded their daily quota and their reset time.' in Input Gestures dialog.
            "Alt+Q: " + _("Reports the number of Gemini API keys that have exceeded their daily quota and their reset time.") + "\n" +
            # Translators: Script description for 'Reports the AI models selected in advanced routing.' in Input Gestures dialog.
            "Alt+M: " + _("Reports the AI models selected in advanced routing.")
        )
        # Translators: Title of the help dialog
        ui.browseableMessage(help_msg, _("{name} Help").format(name=ADDON_NAME))

    @scriptHandler.script(description=_("Announces the current status of the add-on."), category=ADDON_NAME)
    def script_announceStatus(self, gesture):
        if self.toggling: self.finish()
        idle_msg = _("Idle")
        msg = self.current_status if self.current_status else idle_msg
        ui.message(msg)

    @scriptHandler.script(description=_("Starts or ends a live voice conversation with the AI assistant."), category=ADDON_NAME)
    def script_toggleLiveAssistant(self, gesture):
        if self.toggling: self.finish()
        if self.live_session:
            self._end_live_session()
            return
        if not AIHandler.is_gemini():
            # Translators: Error shown when the Live Assistant is used with a non-Gemini provider.
            show_error_dialog(_("The Live Assistant is only supported with the Gemini provider (or a Custom provider with API type set to Gemini)."))
            return
        self._start_live_session()

    @scriptHandler.script(description=_("Opens the Vision Assistant settings dialog."), category=ADDON_NAME)
    def script_openSettings(self, gesture):
        if self.toggling: self.finish()
        wx.CallAfter(self.on_settings_click, None)

    # Translators: Script description for 'Checks for updates manually.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Checks for updates manually."), category=ADDON_NAME)
    def script_checkUpdate(self, gesture):
        if self.toggling: self.finish()
        # Translators: Message reported when calling the update command
        msg = _("Checking for updates...")
        self.report_status(msg)
        self.updater.check_for_updates(silent=False)

    @scriptHandler.script(description=_("Reports the number of Gemini API keys that have exceeded their daily quota and their reset time."), category=ADDON_NAME)
    def script_reportQuotaExhaustedKeys(self, gesture):
        if self.toggling: self.finish()
        if not AIHandler.is_gemini():
            # Translators: Message shown when a user tries to check Gemini API quotas but another provider is active.
            core.callLater(0, ui.message, _("This feature is only available for Google Gemini."))
            return
        try:
            banned_str = config.conf["VisionAssistant"].get("banned_gemini_keys", "{}")
            banned = json.loads(banned_str)
        except Exception:
            banned = {}

        now = time.time()
        unique_keys = {}
        max_time_per_key = {}

        for k_m, ban_time in list(banned.items()):
            if now < ban_time:
                parts = k_m.split("::")
                k = parts[0]
                m = parts[1] if len(parts) > 1 else "Unknown"
                if k not in unique_keys:
                    unique_keys[k] = []
                unique_keys[k].append(m)
                max_time_per_key[k] = max(max_time_per_key.get(k, 0), ban_time)
            else:
                del banned[k_m]

        config.conf["VisionAssistant"]["banned_gemini_keys"] = json.dumps(banned)

        if not unique_keys:
            # Translators: Message when no API keys are out of quota
            ui.message(_("No API keys have exceeded their daily quota."))
            return

        today = datetime.date.today()
        msg_parts = []
        for k, models in unique_keys.items():
            models.sort()
            max_time = max_time_per_key[k]
            model_str = ", ".join(models)
            ban_date = datetime.datetime.fromtimestamp(max_time).date()
            time_str = time.strftime("%H:%M", time.localtime(max_time))
            if ban_date > today:
                # Translators: Prefix for time when the daily quota resets on the next day
                time_str = _("tomorrow at {time}").format(time=time_str)
            # Translators: Shows detailed information for a banned API key. {key} is the API key, {model} is the model name, {time_str} is the reset time.
            key_info = _("Key: {key}\nModel: {model}\nResets around: {time_str}\n").format(key=k, model=model_str, time_str=time_str)
            msg_parts.append(key_info)

        model_counts = {}
        for models in unique_keys.values():
            for m in models:
                model_counts[m] = model_counts.get(m, 0) + 1

        summary_parts = []
        for m, count in model_counts.items():
            # Translators: Shows how many API keys have exceeded their quota for a specific model. {count} is the number of keys, {model} is the model name.
            summary_parts.append(_("{count} keys for model {model}").format(count=count, model=m))

        # Translators: Message shown when API keys run out of quota.
        summary_msg = ", ".join(summary_parts) + " " + _("have exceeded their daily quota.")
        final_msg = summary_msg + "\n\n" + "\n".join(msg_parts).strip()
        # Translators: Title of the browseable message dialog showing exhausted API keys
        ui.browseableMessage(final_msg, _("Exhausted API Keys"))

    @scriptHandler.script(description=_("Reports the AI models selected in advanced routing."), category=ADDON_NAME)
    def script_reportSelectedModels(self, gesture):
        if self.toggling: self.finish()
        models = []
        conf = config.conf["VisionAssistant"]
        p = conf.get("active_provider", "gemini")

        m_key = "model_name" if p == "gemini" else f"{p}_model_name"
        main_m = conf.get(m_key, "")
        if main_m:
            # Translators: Prefix for main model status
            models.append(_("Main: {model}").format(model=main_m))

        def add_adv(task, name):
            m = conf.get(f"{p}_{task}_model", "")
            if m and "Default" not in m and "Auto" not in m:
                models.append(f"{name}: {m}")

        add_adv("ocr", _("OCR"))
        # Translators: Abbreviation for Speech-to-Text.
        add_adv("stt", _("STT"))
        # Translators: Abbreviation for Text-to-Speech.
        add_adv("tts", _("TTS"))
        # Translators: Labels for the AI and User in chat history
        add_adv("operator", _("Operator"))
        add_adv("video", _("Video"))
        add_adv("live", _("Live"))

        if not models:
            # Translators: Message when no specific AI models are selected in advanced routing
            ui.message(_("No specific models selected."))
        else:
            ui.message(". ".join(models))

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

    def _show_live_window(self):
        if getattr(self, "live_dlg", None) and LiveAssistantDialog.instance is self.live_dlg:
            self.live_dlg.set_active(bool(self.live_session))
        else:
            self.live_dlg = LiveAssistantDialog(gui.mainFrame, self._start_live_session, self._end_live_session)
            self.live_dlg.set_active(bool(self.live_session))
            self.live_dlg.Show()
        self.live_dlg.Raise()
        self.live_dlg.history.SetFocus()

    def _on_live_video_tick(self, event):
        session = self.live_session
        if not session:
            return
        jpeg_b64, w, h, m = self._capture_fullscreen()
        if jpeg_b64:
            threading.Thread(target=session.send_video_frame, args=(jpeg_b64,), daemon=True).start()

    def _start_live_worker(self):
        session = self.live_session
        if session and not session.start():
            wx.CallAfter(self._live_on_closed)

    def _live_append(self, line):
        if getattr(self, "live_dlg", None):
            try: self.live_dlg.append_line(line)
            except Exception: pass

    def _live_stream(self, chunk):
        if getattr(self, "live_dlg", None):
            try: self.live_dlg.append_raw(chunk)
            except Exception: pass

    def _live_status(self, msg):
        if msg.startswith("ERROR:"):
            show_error_dialog(msg[6:])
            self._end_live_session()
        elif msg.startswith("STATUS:"):
            self.report_status(msg[7:])

    def _end_live_session(self):
        if self.live_session:
            try: self.live_session.stop()
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
        # Translators: Message announced by NVDA when the live voice conversation ends.
        self.report_status(_("Live conversation ended."))

    def _browse_file(self, wildcard):
        return get_file_path(_("Open"), wildcard)

    def _upload_file_to_gemini(self, file_path, mime_type, silent=False, abort_checker=None, api_key=None):
        p = config.conf["VisionAssistant"]["active_provider"]
        keys = AIHandler.get_keys(p)
        if not keys: return None

        if not AIHandler.is_gemini():
            url = AIHandler.get_endpoint("upload")
            boundary = "Boundary-" + __import__('uuid').uuid4().hex
            with open(file_path, "rb") as f:
                data = f.read()
            body = []
            body.append(f"--{boundary}".encode())
            body.append(f'Content-Disposition: form-data; name="purpose"'.encode())
            body.append(b'')
            body.append(b'ocr')
            body.append(f"--{boundary}".encode())
            body.append(f'Content-Disposition: form-data; name="file"; filename="{os.path.basename(file_path)}"'.encode())
            body.append(f'Content-Type: {mime_type}'.encode())
            body.append(b'')
            body.append(data)
            body.append(f"--{boundary}--".encode())
            body.append(b'')

            for key in keys:
                if abort_checker and abort_checker(): return None
                try:
                    req = request.Request(url, data=b'\r\n'.join(body), headers={"Authorization": f"Bearer {key}", "Content-Type": f"multipart/form-data; boundary={boundary}"}, method="POST")
                    with get_proxy_opener().open(req, timeout=3600) as r:
                        res = json.loads(r.read().decode())
                        return res.get("id") or res.get("name")
                except Exception: continue
            return None

        from .ai.providers.gemini import GeminiHandler
        if not api_key:
            g_keys = GeminiHandler._get_api_keys()
            if not g_keys: return None
            api_key = g_keys[GeminiHandler._working_key_idx % len(g_keys)]

        try:
            uri, _dur = GeminiHandler._upload_file_common(file_path, mime_type, api_key, abort_checker=abort_checker)
            return uri
        except Exception as e:
            err_msg = GeminiHandler._handle_error(e) if isinstance(e, error.HTTPError) else str(e)
            # Translators: Message of a dialog which may pop up while performing an AI call
            msg = _("File Upload Error: {error}").format(error=err_msg)
            self.report_status(msg)
            if not silent:
                wx.CallAfter(show_error_dialog, msg)
            return None

    def terminate(self):
        try:
            if not globalVars.appArgs.secure:
                if hasattr(self, 'va_submenu_item') and self.va_submenu_item:
                    self.tools_menu.Remove(self.va_submenu_item.GetId())

            gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(SettingsPanel)

        except Exception: pass

        if hasattr(self, 'update_timer') and self.update_timer and self.update_timer.IsRunning():
            self.update_timer.Stop()

        self._abort_operator = True
        self._is_operator_running = False
        self._operator_thread_token = getattr(self, "_operator_thread_token", 0) + 1

        if self.live_session:
            try: self.live_session.stop()
            except Exception: pass
            self.live_session = None

        for dlg in [self.refine_dlg, self.refine_menu_dlg, self.vision_dlg, self.doc_dlg, self.doc_viewer_dlg, self.translation_dlg]:
            if dlg:
                try:
                    if getattr(dlg, "abort", None) is not None:
                        dlg.abort = True
                    dlg.Destroy()
                except Exception: pass

        if self.is_recording:
            try:
                ctypes.windll.winmm.mciSendStringW('close all', None, 0, 0)
            except Exception: pass

        self.translation_cache = {}
        self._last_source_text = None
        plugin_state.plugin_instance = None
        for fpath in getattr(self, "_temp_files_to_cleanup", []):
            try:
                if os.path.exists(fpath):
                    os.remove(fpath)
            except Exception: pass
        self._temp_files_to_cleanup = []
        gc.collect()

    def report_status(self, msg):
        self.current_status = msg
        ui.message(msg)

    def script_layerDown(self, gesture):
        self._quick_settings_idx = (getattr(self, '_quick_settings_idx', 0) + 1) % 17
        self._announce_current_quick_setting()
    script_layerDown.keep_layer_alive = True

    def script_layerUp(self, gesture):
        self._quick_settings_idx = (getattr(self, '_quick_settings_idx', 0) - 1) % 17
        self._announce_current_quick_setting()
    script_layerUp.keep_layer_alive = True

    def script_layerRight(self, gesture):
        self._change_quick_setting(1)
    script_layerRight.keep_layer_alive = True

    def script_layerLeft(self, gesture):
        self._change_quick_setting(-1)
    script_layerLeft.keep_layer_alive = True
    
    # Translators: Script description for 'Activates the Command Layer for quick access to all features.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Activates the Command Layer for quick access to all features."), category=ADDON_NAME)
    def script_activateLayer(self, gesture):
        if globalVars.appArgs.secure:
            return

        if self.toggling:
            self.script_error(gesture)
            return

        self.bindGestures(self.__VisionGestures)
        self.toggling = True
        tones.beep(500, 100)

    def _open_direct_chat_dialog(self, force_show=True, is_recall=False):
        self._last_result_data = (self._open_direct_chat_dialog, ())

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

            from .ai.providers.gemini import GeminiHandler
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
            extra_info={'skip_init_history': False, 'restore_history': getattr(self, "_last_chat_history", None) if is_recall else None},
            raw_content=init_msg,
            status_callback=self.report_status,
            allow_attachments=True
        )
        self.vision_dlg.Show()
        self.vision_dlg.Raise()

    # Translators: Script description for 'Opens a chat dialog to directly prompt the AI with text or files.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Opens a chat dialog to directly prompt the AI with text or files."), category=ADDON_NAME)
    def script_openDirectChat(self, gesture):
        if self.toggling: self.finish()
        wx.CallAfter(self._open_direct_chat_dialog)

    @scriptHandler.script(description=_("Shows the last AI response in a chat dialog for review or follow-up questions."), category=ADDON_NAME)
    def script_showLastResult(self, gesture):
        if self.toggling: self.finish()
        if self._last_result_data:
            func, args = self._last_result_data
            wx.CallAfter(func, *args, force_show=True, is_recall=True)

    def on_settings_click(self, event):
        instance = getattr(gui.settingsDialogs.NVDASettingsDialog, "instance", None)
        if instance:
            try:
                instance.Show(True)
                instance.Raise()
                instance.SetFocus()
                if hasattr(instance, "setPanel"):
                    instance.setPanel(SettingsPanel)
                return
            except Exception:
                gui.settingsDialogs.NVDASettingsDialog.instance = None

        def _force_open():
            gui.settingsDialogs.NVDASettingsDialog.instance = None
            try:
                gui.mainFrame.prePopup()
                new_inst = gui.settingsDialogs.NVDASettingsDialog(gui.mainFrame, SettingsPanel)
                new_inst.Show()
                new_inst.Raise()
                gui.mainFrame.postPopup()
            except Exception:
                gui.settingsDialogs.NVDASettingsDialog.instance = None
                try:
                    gui.mainFrame.postPopup()
                except Exception:
                    pass

        wx.CallLater(100, _force_open)

    def on_help_click(self, event):
        try:
            help_url = "https://github.com/mahmoodhozhabri/VisionAssistantPro"
            os.startfile(help_url)
        except Exception as e:
            show_error_dialog(str(e))

    def on_donate_click(self, event):
        try:
            wx.CallAfter(donate.requestDonations, gui.mainFrame)
        except Exception as e:
            show_error_dialog(str(e))

    def on_telegram_click(self, event):
        try:
            os.startfile("https://t.me/VisionAssistantPro")
        except Exception as e:
            show_error_dialog(str(e))

    def chooseNVDAObjectOverlayClasses(self, obj, clsList):
        if not hasattr(self, "labels_cache"):
            return
        app_module = getattr(obj, "appModule", None)
        if not app_module:
            return
        app_name = app_module.appName.lower()
        if app_name in ["chrome", "msedge", "firefox", "opera", "brave"]:
            return

        class_name = getattr(obj, "windowClassName", None)
        if class_name == "Internet Explorer_Server":
            return

        uniqueId = self._getAppId(obj)
        if uniqueId not in self.labels_cache:
            return

        key = _generate_object_signature(obj)
        if key and key in self.labels_cache[uniqueId]:
            clsList.insert(0, CustomLabelOverlay)
            return

    # Translators: Script description for 'Labels the current navigator object using AI.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Labels the current navigator object using AI."), category=ADDON_NAME)
    def script_labelObject(self, gesture):
        if self.toggling: self.finish()
        obj = api.getNavigatorObject()
        if not obj or not obj.location: return

        if check_screen_curtain_active():
            return

        uniqueId = self._getAppId(obj)
        if uniqueId in ["chrome", "msedge", "firefox", "opera", "brave"]:
            # Translators: Message shown when a user tries to use AI labeling in a web browser.
            ui.message(_("AI Labeling is currently not supported in web browsers."))
            return

        loc = obj.location
        sig_key = _generate_object_signature(obj)

        is_labeled = False
        found_label = ""
        if uniqueId in self.labels_cache:
            if sig_key and sig_key in self.labels_cache[uniqueId]:
                is_labeled = True
                found_label = self.labels_cache[uniqueId][sig_key]

        if is_labeled:
            # Translators: Message spoken by NVDA when the current object already has a custom or AI-generated label. {name} is replaced with the existing label text.
            ui.message(_("Already labeled as: {name}").format(name=found_label))
            return

        tones.beep(800, 100)
        # Translators: Progress message spoken when the add-on starts taking a screenshot of the current focused object.
        self.current_status = _("Identifying object...")
        ui.message(self.current_status)

        img, w, h, m = self._capture_navigator()
        def worker():
            if not img:
                self.current_status = _("Idle")
                return
            self.current_status = _("Analyzing...")
            core.callLater(0, ui.message, self.current_status)

            resp_lang = get_lang_name("ai_response_language")
            prompt_template = get_prompt_text("label_single_system")
            prompt = apply_prompt_template(prompt_template, [
                ("app_name", uniqueId),
                ("response_lang", resp_lang)
            ])

            res = AIHandler.call(prompt, attachments=[{'mime_type': m, 'data': img}], task="operator")
            self.current_status = _("Idle")

            if res and not res.startswith("ERROR:"):
                clean_name = clean_markdown(res)

                def save_ui_thread():
                    if uniqueId not in self.labels_cache: self.labels_cache[uniqueId] = {}
                    sig_key = _generate_object_signature(obj)
                    if sig_key:
                        self.labels_cache[uniqueId][sig_key] = clean_name
                        self._save_all_labels()
                        tones.beep(1000, 100)
                        # Translators: Success message spoken when the AI successfully assigns a new label to the object. {name} is replaced with the AI-generated label.
                        ui.message(_("Labeled as: {name}").format(name=clean_name))

                wx.CallAfter(save_ui_thread)
            elif res and res.startswith("ERROR:"):
                wx.CallAfter(show_error_dialog, res[6:])

        threading.Thread(target=worker, daemon=True).start()

    # Translators: Script description for 'Manages existing labels or scans the entire app to label unnamed elements.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Manages existing labels or scans the entire app to label unnamed elements."), category=ADDON_NAME)
    def script_manageOrScanApp(self, gesture):
        if self.toggling: self.finish()
        obj = api.getFocusObject()
        app_name = obj.appModule.appName.lower()
        if app_name in ["chrome", "msedge", "firefox", "opera", "brave"]:
            ui.message(_("AI Labeling is currently not supported in web browsers."))
            return
        uniqueId = self._getAppId(obj)

        if uniqueId in self.labels_cache and self.labels_cache[uniqueId]:
            def show_manager():
                gui.mainFrame.prePopup()
                dlg = LabelManagerDialog(gui.mainFrame, uniqueId, self.labels_cache[uniqueId])
                if dlg.ShowModal() == wx.ID_OK:
                    if dlg.action_type == "delete":
                        for k in dlg.target_keys: del self.labels_cache[uniqueId][k]
                    elif dlg.action_type == "rename":
                        self.labels_cache[uniqueId][dlg.target_keys[0]] = dlg.new_name
                    elif dlg.action_type == "rescan":
                        wx.CallLater(600, self._batchLabelApp, uniqueId)

                    if dlg.action_type in ["delete", "rename"]:
                        self._save_all_labels()
                        # Translators: Confirmation message shown after labels are deleted or renamed.
                        ui.message(_("Labels updated."))
                dlg.Destroy()
                gui.mainFrame.postPopup()
            wx.CallAfter(show_manager)
        else:
            wx.CallLater(400, self._batchLabelApp, uniqueId)

    def _save_all_labels(self):
        try:
            with open(LABELS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.labels_cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            log.error(f"Failed to save labels: {e}")

    def _batchLabelApp(self, unique_id):
        if check_screen_curtain_active():
            return
        tones.beep(800, 100)
        # Translators: Progress message spoken when the add-on begins scanning the current application window to find UI elements (like buttons or icons) that do not have accessibility names.
        self.current_status = _("Scanning application UI...")
        ui.message(self.current_status)

        root = api.getForegroundObject()
        candidates = []
        stack = [(root, 0)]
        target_roles = {controlTypes.Role.BUTTON, controlTypes.Role.TOGGLEBUTTON, controlTypes.Role.CHECKBOX, controlTypes.Role.RADIOBUTTON, controlTypes.Role.MENUITEM, controlTypes.Role.LINK, controlTypes.Role.TAB, controlTypes.Role.DATAITEM, controlTypes.Role.LISTITEM, controlTypes.Role.COMBOBOX, controlTypes.Role.GRAPHIC, controlTypes.Role.ICON, controlTypes.Role.TABLECELL}

        while stack and len(candidates) < 1500:
            obj, depth = stack.pop()
            if depth > 25:
                continue
            try:
                role = obj.role
                loc = obj.location
                name = obj.name
                if loc and role in target_roles and (not name or not name.strip()):
                    candidates.append(obj)

                child = obj.firstChild
                while child:
                    stack.append((child, depth + 1))
                    child = child.next
            except Exception:
                continue

        if not candidates:
            self.current_status = _("Idle")
            # Translators: Message spoken when the add-on finishes the UI scan but finds no unnamed elements to label (everything already has a name).
            ui.message(_("No unnamed elements found."))
            return

        # Translators: Progress message spoken when the add-on has found unnamed elements and is now sending the full application screenshot to AI for batch labeling.
        self.current_status = _("Analyzing application...")
        ui.message(self.current_status)

        img, w, h, m = self._capture_fullscreen()

        def worker():
            prompt_template = get_prompt_text("label_batch_system")
            prompt = apply_prompt_template(prompt_template, [("app_name", unique_id), ("response_lang", get_lang_name("ai_response_language"))])
            res = AIHandler.call(prompt, attachments=[{'mime_type': m, 'data': img}], json_mode=True, task="operator")

            self.current_status = _("Idle")
            if res and not res.startswith("ERROR:"):
                try:
                    raw_res = res.strip()
                    start_idx = raw_res.find('[')
                    end_idx = raw_res.rfind(']')
                    if start_idx != -1 and end_idx != -1:
                        clean_json = raw_res[start_idx:end_idx+1]
                    else:
                        clean_json = raw_res

                    clean_json = __import__('re').sub(r'\}\s*\{', '}, {', clean_json)
                    ai_items = []
                    try:
                        ai_items = json.loads(clean_json)
                    except Exception:
                        try:
                            ai_items = ast.literal_eval(clean_json)
                        except Exception:
                            for match in __import__('re').finditer(r'\{[^{}]*\}', clean_json):
                                obj_str = match.group(0)
                                lbl_match = __import__('re').search(r'"label"\s*:\s*"([^"]+)"', obj_str)
                                x_match = __import__('re').search(r'"x"\s*:\s*(\d+)', obj_str)
                                y_match = __import__('re').search(r'"y"\s*:\s*(\d+)', obj_str)
                                if lbl_match and x_match and y_match:
                                    ai_items.append({"label": lbl_match.group(1), "x": int(x_match.group(1)), "y": int(y_match.group(1))})

                    def save_batch_ui_thread():
                        if unique_id not in self.labels_cache:
                            self.labels_cache[unique_id] = {}
                        for item in ai_items:
                            if not all(k in item for k in ("x", "y", "label")): continue
                            try:
                                x_val, y_val = float(item["x"]), float(item["y"])
                            except Exception: continue

                            ai_x, ai_y = int(x_val * w / 1000), int(y_val * h / 1000)
                            best_match, min_dist = None, 100

                            for cand in candidates:
                                c_loc = cand.location
                                if not c_loc: continue
                                cx, cy = c_loc.left + c_loc.width/2, c_loc.top + c_loc.height/2
                                dist = ((cx - ai_x)**2 + (cy - ai_y)**2)**0.5
                                if dist < min_dist:
                                    min_dist = dist
                                    best_match = cand
                            if best_match:
                                sig_key = _generate_object_signature(best_match)
                                if sig_key:
                                    self.labels_cache[unique_id][sig_key] = item["label"]
                        self._save_all_labels()
                        tones.beep(1000, 100)
                        # Translators: Success message spoken when the AI finishes analyzing the app and successfully names multiple elements in the background.
                        ui.message(_("Application labeling complete."))
                    wx.CallAfter(save_batch_ui_thread)
                except Exception as e:
                    log.error(f"Batch labeling mapping failed: {e}")
                    # Translators: Error message spoken when the add-on fails to parse or map the labels returned by the AI (e.g., due to invalid AI response format).
                    core.callLater(0, ui.message, _("Batch labeling failed."))
            elif res and res.startswith("ERROR:"):
                wx.CallAfter(show_error_dialog, res[6:])

        threading.Thread(target=worker, daemon=True).start()

    def _getAppId(self, obj):
        try:
            appName = obj.appModule.appName.lower()
        except Exception:
            appName = "unknown_app"
            
        if appName == "applicationframehost":
            try:
                fg = api.getForegroundObject()
                if fg and fg.name:
                    return f"{appName}_{fg.name}"
            except Exception: pass
        return appName

    __gestures = {
        "kb:NVDA+shift+v": "activateLayer",
    }

    __VisionGestures = {
        "kb:t": "translateSmart",
        "kb:r": "refineText",
        "kb:o": "ocrFullScreen",
        "kb:v": "describeObject",
        "kb:d": "analyzeDocument",
        "kb:f": "smartFileAction",
        "kb:m": "mediaTranscriber",
        "kb:c": "solveCaptcha",
        "kb:shift+c": "openDirectChat",
        "kb:i": "announceStatus",
        "kb:s": "smartDictation",
        "kb:u": "checkUpdate",
        "kb:shift+t": "translateClipboard",
        "kb:shift+v": "analyzeOnlineVideo",
        "kb:control+v": "recordLocalVideo",
        "kb:space": "showLastResult",
        "kb:h": "showHelp",
        "kb:e": "toggleUIExplorer",
        "kb:shift+a": "aiOperatorAction",
        "kb:l": "labelObject",
        "kb:shift+l": "manageOrScanApp",
        "kb:control+l": "toggleLiveAssistant",
        "kb:alt+s": "openSettings",
        "kb:alt+q": "reportQuotaExhaustedKeys",
        "kb:alt+m": "reportSelectedModels",
        "kb:downArrow": "layerDown",
        "kb:upArrow": "layerUp",
        "kb:rightArrow": "layerRight",
        "kb:leftArrow": "layerLeft",
        "kb:control+t": "voiceTranslation",
    }