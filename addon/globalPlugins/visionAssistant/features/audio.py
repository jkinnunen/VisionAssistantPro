# -*- coding: utf-8 -*-
import wx
import os
import wave
import base64
import threading
import ctypes
import logging
import re
import subprocess
import time
import json
import tempfile

import ui
import core
import api
import tones
import scriptHandler
import gui
import config as nvda_config
import addonHandler

from .. import vision_config
from ..vision_config import ADDON_NAME
from ..ai.core import AIHandler
from ..utils.system import clean_markdown, show_error_dialog, get_mime_type, get_file_path, get_focused_explorer_files
from ..utils.mouse_keyboard import send_ctrl_v
from ..utils.media_capture import ensure_ffmpeg


log = logging.getLogger(__name__)

addonHandler.initTranslation()


class AudioMixin:

    # Translators: Script description for 'Records voice, transcribes it using AI, and types the result.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Records voice, transcribes it using AI, and types the result."), category=ADDON_NAME)
    def script_smartDictation(self, gesture):
        if getattr(self, "toggling", False): self.finish()
        if not self.is_recording:
            self.is_recording = True
            tones.beep(800, 100)
            try:
                ret_open = ctypes.windll.winmm.mciSendStringW('open new type waveaudio alias myaudio', None, 0, 0)
                if ret_open != 0:
                    self.is_recording = False
                    # Translators: Message in an error dialog which can pop up while trying dictation.
                    msg = _("Audio Hardware Error: {error}").format(error=f"MCI_OPEN_ERR_{ret_open}")
                    show_error_dialog(msg)
                    return
                
                ret_rec = ctypes.windll.winmm.mciSendStringW('record myaudio', None, 0, 0)
                if ret_rec != 0:
                    self.is_recording = False
                    ctypes.windll.winmm.mciSendStringW('close all', None, 0, 0)
                    # Translators: Message reported when dictation starts
                    msg = _("Audio Hardware Error: {error}").format(error=f"MCI_RECORD_ERR_{ret_rec}")
                    show_error_dialog(msg)
                    return

                msg = _("Listening...")
                self.report_status(msg)
            except Exception as e:
                msg = _("Audio Hardware Error: {error}").format(error=e)
                show_error_dialog(msg)
                self.is_recording = False
        else:
            self.is_recording = False
            tones.beep(500, 100)
            try:
                ctypes.windll.winmm.mciSendStringW(f'save myaudio "{self.temp_audio_file}"', None, 0, 0)
                ctypes.windll.winmm.mciSendStringW('close myaudio', None, 0, 0)
                threading.Thread(target=self._thread_dictation, daemon=True).start()
            except Exception as e:
                # Translators: Message in an error dialog which can pop up while trying dictation.
                msg = _("Save Recording Error: {error}").format(error=e)
                show_error_dialog(msg)

    def _thread_dictation(self):
        try:
            if not os.path.exists(self.temp_audio_file): return
            
            try:
                with wave.open(self.temp_audio_file, "rb") as wave_file:
                    frame_rate = wave_file.getframerate()
                    n_frames = wave_file.getnframes()
                    duration = n_frames / float(frame_rate)
                
                if duration < 1.0:
                    # Translators: Message reported when the AI detects silence or empty speech
                    msg = _("No speech detected.")
                    core.callLater(0, self.report_status, msg)
                    if os.path.exists(self.temp_audio_file):
                        try: os.remove(self.temp_audio_file)
                        except Exception as e: log.warning(f"Temp file removal failed: {e}")
                    return
            except Exception as e:
                log.warning(f"Dictation duration check failed: {e}")

            # Translators: Message reported when processing dictation
            core.callLater(0, self.report_status, _("Typing..."))
            with open(self.temp_audio_file, "rb") as f:
                audio_data = base64.b64encode(f.read()).decode('utf-8')
            
            dictation_template = vision_config.get_prompt_text("dictation_transcribe") or (
                "Transcribe speech. Use native script. Fix stutters. If there is no speech, "
                "silence, or background noise only, write exactly: [[[NOSPEECH]]]"
            )
            p = vision_config.apply_prompt_template(dictation_template, [("response_lang", vision_config.get_lang_name("ai_response_language"))])
            
            res = AIHandler.call(p, attachments=[{'mime_type': 'audio/wav', 'data': audio_data}])
            
            if res:
                if res.startswith("ERROR:"):
                    log.error(f"Dictation AI call error: {res}")
                    wx.CallAfter(show_error_dialog, res[6:])
                elif "NOSPEECH" in res.upper():
                    msg = _("No speech detected.")
                    core.callLater(0, self.report_status, msg)
                else:
                    cleaned_text = clean_markdown(res)
                    core.callLater(0, self._paste_text, cleaned_text)
            else: 
                log.error("Dictation: AI returned empty response")
                # Translators: Message reported while trying dictation.
                msg = _("No speech recognized or Error.")
                core.callLater(0, self.report_status, msg)

            if os.path.exists(self.temp_audio_file):
                try: os.remove(self.temp_audio_file)
                except Exception as e: log.warning(f"Temp file removal failed: {e}")
        except Exception as e:
            log.error(f"Dictation thread failed: {e}", exc_info=True)
        finally:
            # Translators: Error message shown when uploading a video file fails.
            self.current_status = _("Idle")
            self.is_recording = False

    # Translators: Script description for 'Shows a list of available commands in the layer.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Records voice, transcribes and translates it using AI, and types the result."), category=ADDON_NAME)
    def script_voiceTranslation(self, gesture):
        if getattr(self, "toggling", False): self.finish()
        if getattr(self, "is_translation_recording", False) == False:
            self.is_translation_recording = True
            tones.beep(800, 100)
            try:
                ret_open = ctypes.windll.winmm.mciSendStringW('open new type waveaudio alias myaudiotrans', None, 0, 0)
                if ret_open != 0:
                    self.is_translation_recording = False
                    msg = _("Audio Hardware Error: {error}").format(error=f"MCI_OPEN_ERR_{ret_open}")
                    show_error_dialog(msg)
                    return

                ret_rec = ctypes.windll.winmm.mciSendStringW('record myaudiotrans', None, 0, 0)
                if ret_rec != 0:
                    self.is_translation_recording = False
                    ctypes.windll.winmm.mciSendStringW('close all', None, 0, 0)
                    msg = _("Audio Hardware Error: {error}").format(error=f"MCI_RECORD_ERR_{ret_rec}")
                    show_error_dialog(msg)
                    return

                msg = _("Listening...")
                self.report_status(msg)
            except Exception as e:
                msg = _("Audio Hardware Error: {error}").format(error=e)
                show_error_dialog(msg)
                self.is_translation_recording = False
        else:
            self.is_translation_recording = False
            tones.beep(500, 100)
            try:
                ctypes.windll.winmm.mciSendStringW(f'save myaudiotrans "{self.temp_audio_file}"', None, 0, 0)
                ctypes.windll.winmm.mciSendStringW('close myaudiotrans', None, 0, 0)
                threading.Thread(target=self._thread_voiceTranslation, daemon=True).start()
            except Exception as e:
                # Translators: Message in an error dialog which can pop up while trying dictation.
                msg = _("Save Recording Error: {error}").format(error=e)
                show_error_dialog(msg)

    def _thread_voiceTranslation(self):
        try:
            if not os.path.exists(self.temp_audio_file): return

            try:
                with wave.open(self.temp_audio_file, "rb") as wave_file:
                    frame_rate = wave_file.getframerate()
                    n_frames = wave_file.getnframes()
                    duration = n_frames / float(frame_rate)

                if duration < 1.0:
                    msg = _("No speech detected.")
                    core.callLater(0, self.report_status, msg)
                    if os.path.exists(self.temp_audio_file):
                        try: os.remove(self.temp_audio_file)
                        except Exception as e: log.warning(f"Temp file removal failed: {e}")
                    return
            except Exception as e:
                log.warning(f"Dictation duration check failed: {e}")

            # Translators: Message reported when calling translation command
            core.callLater(0, self.report_status, _("Translating..."))
            with open(self.temp_audio_file, "rb") as f:
                audio_data = base64.b64encode(f.read()).decode('utf-8')

            translation_template = vision_config.get_prompt_text("dictation_translate") or (
                "Transcribe and translate the spoken audio from {source_lang} to {target_lang}. "
                "If {source_lang} is Auto-detect, identify the language first. "
                "SMART SWAP RULE: If the spoken language is ALREADY {target_lang} AND Smart Swap is {smart_swap}, translate the audio into {swap_target} instead. "
                "Output ONLY the final translation. Do not add any extra comments or notes. "
                "If there is no speech, silence, or background noise only, write exactly: [[[NOSPEECH]]]"
            )
            
            s = vision_config.get_lang_name("source_language")
            t = vision_config.get_lang_name("target_language")
            swap = nvda_config.conf["VisionAssistant"]["smart_swap"]
            fallback = "English" if s == "Auto-detect" else s
            
            p = vision_config.apply_prompt_template(translation_template, [
                ("source_lang", s),
                ("target_lang", t),
                ("swap_target", fallback),
                ("smart_swap", str(swap))
            ])

            res = AIHandler.call(p, attachments=[{'mime_type': 'audio/wav', 'data': audio_data}])

            if res:
                if res.startswith("ERROR:"):
                    log.error(f"Voice Translation AI call error: {res}")
                    wx.CallAfter(show_error_dialog, res[6:])
                elif "NOSPEECH" in res.upper():
                    msg = _("No speech detected.")
                    core.callLater(0, self.report_status, msg)
                else:
                    cleaned_text = clean_markdown(res)
                    core.callLater(0, self._paste_text, cleaned_text)
            else:
                log.error("Voice Translation: AI returned empty response")
                msg = _("No speech recognized or Error.")
                core.callLater(0, self.report_status, msg)

            if os.path.exists(self.temp_audio_file):
                try: os.remove(self.temp_audio_file)
                except Exception as e: log.warning(f"Temp file removal failed: {e}")
        except Exception as e:
            log.error(f"Voice Translation thread failed: {e}", exc_info=True)
        finally:
            self.current_status = _("Idle")
            self.is_translation_recording = False

    def _paste_text(self, text):
        api.copyToClip(text)
        send_ctrl_v()
        wx.CallLater(300, self._announce_paste, text)

    def _announce_paste(self, text):
        preview = text[:100]
        # Translators: Message reported when dictation is complete
        msg = _("Typed: {text}").format(text=preview)
        tones.beep(1000, 100)
        self.report_status(msg)

    @scriptHandler.script(description=_("Transcribes or dubs a selected media file."), category=ADDON_NAME)
    def script_mediaTranscriber(self, gesture):
        if getattr(self, "toggling", False): self.finish()
        if getattr(self, "_dialog_open", False): return
        focused_paths = get_focused_explorer_files()
        valid_exts = ('.mp3', '.wav', '.ogg', '.m4a', '.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv')
        valid_paths = [p for p in focused_paths if p.lower().endswith(valid_exts)]
        if valid_paths:
            wx.CallAfter(self._ask_audio_action, valid_paths[0])
            return
        wx.CallLater(100, self._open_audio)

    def _open_audio(self):
        self._dialog_open = True
        wc = "Audio/Video|*.mp3;*.wav;*.ogg;*.m4a;*.mp4;*.mkv;*.avi;*.mov;*.flv;*.wmv"
        self._browse_and_run(self._ask_audio_action_from_browse, wc, multiple=False)
        self._dialog_open = False

    def _ask_audio_action_from_browse(self, paths):
        if paths: wx.CallAfter(self._ask_audio_action, paths[0])

    def _ask_audio_action(self, path):
        self._dialog_open = True
        # Translators: Options for the media file action menu
        choices = [_("Transcribe (Original Language)"), _("Transcribe and Translate (Target Language)")]
        # Translators: Option in media action menu to live translate/dub audio
        if AIHandler.is_gemini(): choices.append(_("Dub and Translate (Target Language)"))
            
        import gui
        gui.mainFrame.prePopup()
        try:
            # Translators: Title of the Refine dialog
            dlg = wx.SingleChoiceDialog(gui.mainFrame, _("Choose action:"), _("Media File"), choices)
            dlg.Raise()
            if dlg.ShowModal() == wx.ID_OK:
                selection = dlg.GetSelection()
                if selection == 0:
                    threading.Thread(target=self._thread_audio, args=(path, "transcribe"), daemon=True).start()
                elif selection == 1:
                    dlg.Destroy()
                    from ..dialogs.media import DubbingDialog
                    dub_dlg = DubbingDialog(gui.mainFrame, is_dubbing=False)
                    dub_dlg.Raise()
                    if dub_dlg.ShowModal() == wx.ID_OK:
                        s_lang, t_lang = dub_dlg.get_settings()
                        threading.Thread(target=self._thread_audio, args=(path, "translate", s_lang, t_lang), daemon=True).start()
                    dub_dlg.Destroy()
                    return
                elif selection == 2:
                    dlg.Destroy()
                    from ..dialogs.media import DubbingDialog
                    dub_dlg = DubbingDialog(gui.mainFrame, is_dubbing=True)
                    dub_dlg.Raise()
                    if dub_dlg.ShowModal() == wx.ID_OK:
                        s_lang, t_lang = dub_dlg.get_settings()
                        threading.Thread(target=self._thread_live_translate_audio, args=(path, s_lang, t_lang), daemon=True).start()
                    dub_dlg.Destroy()
                    return
            dlg.Destroy()
        except Exception as e: log.warning(f"Audio action dialog failed: {e}")
        finally:
            gui.mainFrame.postPopup()
            self._dialog_open = False

    def _thread_audio(self, path, action_type, s_lang=None, t_lang=None):
        try:
            # Translators: Message reported when calling the audio transcription command
            msg = _("Uploading...")
            core.callLater(0, self.report_status, msg)
            mime_type = get_mime_type(path)
            lang = vision_config.get_lang_name("ai_response_language")
            if action_type == "transcribe":
                audio_template = vision_config.get_prompt_text("audio_transcription")
                p = vision_config.apply_prompt_template(audio_template, [("response_lang", lang)])
            else:
                audio_template = vision_config.get_prompt_text("audio_translation")
                target_lang = t_lang if t_lang else vision_config.get_lang_name("target_language")
                source_lang = s_lang if s_lang else vision_config.get_lang_name("source_language")
                p = vision_config.apply_prompt_template(audio_template, [("target_lang", target_lang), ("source_lang", source_lang)])
            
            if AIHandler.is_gemini():
                file_uri = self._upload_file_to_gemini(path, mime_type)
                if not file_uri: return
                att = [{'mime_type': mime_type, 'file_uri': file_uri}]
            else:
                with open(path, "rb") as f: audio_data = base64.b64encode(f.read()).decode('utf-8')
                att =[{'mime_type': mime_type, 'data': audio_data}]

            # Translators: Progress message spoken when the add-on starts taking a screenshot of the current focused object.
            msg = _("Analyzing...")
            core.callLater(0, self.report_status, msg)
            res = AIHandler.call(p, attachments=att)
            
            if res:
                if res.startswith("ERROR:"):
                    wx.CallAfter(show_error_dialog, res[6:])
                    return
                wx.CallAfter(self._open_doc_chat_dialog, res, att, res, res)
        except Exception as e:
            log.error(f"Audio analysis thread failed: {e}", exc_info=True)
        finally:
            self.current_status = _("Idle")

    def _thread_live_translate_audio(self, path, s_lang, t_lang):
        try:
            # Translators: Status message when extracting audio and connecting to Gemini for dubbing
            core.callLater(0, self.report_status, _("Extracting audio and connecting to Gemini..."))
            
            ffmpeg_path = ensure_ffmpeg()
            if not ffmpeg_path: return

            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = 0
            CREATE_NO_WINDOW = 0x08000000

            duration_sec = 0
            try:
                proc = subprocess.run([ffmpeg_path, "-i", path], stderr=subprocess.PIPE, text=True, startupinfo=startupinfo, creationflags=CREATE_NO_WINDOW)
                m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", proc.stderr)
                if m: duration_sec = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
            except: pass

            model = "gemini-3.5-live-translate-preview"
            api_keys = AIHandler.get_keys("gemini")
            if not api_keys:
                # Translators: Error message when TTS is not supported by the provider
                wx.CallAfter(show_error_dialog, _("No API Keys configured."))
                return
                
            ws = None
            num_keys = len(api_keys)
            from ..ai.providers.gemini import GeminiHandler
            start_idx = getattr(GeminiHandler, '_working_key_idx', 0)
            from ..utils.media_capture import _MinimalWebSocket
            
            for i in range(num_keys):
                idx = (start_idx + i) % num_keys
                api_key = api_keys[idx]
                
                base_host = vision_config.DEFAULT_API_URLS["gemini"].replace("https://", "")
                try:
                    import urllib.parse
                    base = AIHandler.get_base_url("gemini")
                    host = urllib.parse.urlparse(base).hostname
                    if host: base_host = host
                except: pass
                
                ws_path = f"/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key={api_key}"
                
                max_retries = getattr(GeminiHandler, '_max_retries', 3)
                attempt = 0
                while attempt < max_retries:
                    ws_candidate = _MinimalWebSocket(base_host, ws_path)
                    try:
                        ws_candidate.connect()
                        ws = ws_candidate
                        GeminiHandler._working_key_idx = idx
                        break
                    except Exception as e:
                        err_str = str(e).lower()
                        is_retryable = False
                        delay = 1.0 * (attempt + 1)
                        
                        if "500" in err_str or "502" in err_str or "503" in err_str or "504" in err_str: is_retryable = True
                        elif "429" in err_str or "high demand" in err_str or "exhausted" in err_str or "quota" in err_str:
                            if any(x in err_str for x in ["daily", "per day", "per_day", "perday", "requestsperday"]): is_retryable = False
                            else:
                                is_retryable = True
                                if "high demand" in err_str: max_retries = max(max_retries, 10)
                                else: max_retries = max(max_retries, 5)
                            
                        if is_retryable and ("429" in err_str or "quota" in err_str or "exhausted" in err_str):
                            match = re.search(r"retry in ([\d\.]+)s", err_str)
                            if match:
                                try: delay = float(match.group(1)) + 0.5
                                except Exception: pass
                                    
                        if not is_retryable:
                            log.error(f"Live Translate: WebSocket connection failed (Key {idx}): {e}")
                            break
                            
                        if attempt < max_retries - 1:
                            log.warning(f"Live Translate: Retryable error (Key {idx}, Attempt {attempt+1}/{max_retries}). Retrying in {delay}s...")
                            time.sleep(delay)
                            attempt += 1
                            continue
                        else: break
                if ws: break
        
            if not ws:
                # Translators: Error message shown when Live Translate cannot connect to the server.
                wx.CallAfter(show_error_dialog, _("WebSocket connection failed for all available API keys."))
                return

            target_code = vision_config.TARGET_CODES.get(t_lang, "en")
            swap = nvda_config.conf["VisionAssistant"]["smart_swap"]
            
            setup_msg = {
                "setup": {
                    "model": f"models/{model}",
                    "generationConfig": {
                        "responseModalities": ["AUDIO"],
                        "translationConfig": {
                            "targetLanguageCode": target_code,
                            "echoTargetLanguage": True if swap else False
                        }
                    }
                }
            }
            ws.send_text(json.dumps(setup_msg))

            setup_success = False
            for step in range(5):
                opcode, payload = ws.recv()
                if not payload: break
                err_msg = payload.decode('utf-8', 'replace')
                if "setupComplete" in err_msg or "setup_complete" in err_msg:
                    setup_success = True
                    break

            if not setup_success:
                # Translators: Error message shown when the Live translation setup fails.
                msg = _("Failed to setup Live translation session. Error: {error}").format(error=err_msg if 'err_msg' in locals() else "Unknown")
                wx.CallAfter(show_error_dialog, msg)
                ws.close()
                return

            duration_str = ""
            import datetime
            if duration_sec > 0:
                mins = int(duration_sec // 60)
                secs = int(duration_sec % 60)
                finish_time = datetime.datetime.now() + datetime.timedelta(seconds=duration_sec)
                time_str = finish_time.strftime("%I:%M %p")
                # Translators: Status message part showing estimated time remaining and completion time.
                if mins > 0: duration_str = _(" (approx. {mins} min {secs} sec, finishing around {time})").format(mins=mins, secs=secs, time=time_str)
                # Translators: Status message part showing estimated seconds remaining and completion time.
                else: duration_str = _(" (approx. {secs} sec, finishing around {time})").format(secs=secs, time=time_str)

            # Translators: Status message when live dubbing is actively streaming
            core.callLater(0, self.report_status, _("Dubbing in progress...") + duration_str)

            ffmpeg_proc = subprocess.Popen(
                [ffmpeg_path, "-i", path, "-f", "s16le", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", "pipe:1"],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                startupinfo=startupinfo, creationflags=CREATE_NO_WINDOW
            )

            def send_audio():
                try:
                    start_time = time.time()
                    total_bytes = 0
                    bytes_per_sec = 32000.0
                    while True:
                        data = ffmpeg_proc.stdout.read(3200)
                        if not data: break
                        total_bytes += len(data)
                        b64_data = base64.b64encode(data).decode('utf-8')
                        realtime_msg = {
                            "realtimeInput": {
                                "mediaChunks": [
                                    {
                                        "mimeType": "audio/pcm;rate=16000",
                                        "data": b64_data
                                    }
                                ]
                            }
                        }
                        ws.send_text(json.dumps(realtime_msg))
                        
                        expected_time = total_bytes / bytes_per_sec
                        elapsed = time.time() - start_time
                        if expected_time > elapsed: time.sleep(expected_time - elapsed)
                    
                    time.sleep(2)
                    end_msg = {"clientContent": {"turnComplete": True}}
                    ws.send_text(json.dumps(end_msg))
                except Exception as e: log.error(f"Live Translate Send Audio failed: {e}")
                finally:
                    try:
                        ffmpeg_proc.terminate()
                        ffmpeg_proc.wait(timeout=2)
                    except Exception: pass

            sender_thread = threading.Thread(target=send_audio, daemon=True)
            sender_thread.start()

            base, _ext = os.path.splitext(path)
            bname = os.path.basename(base)
            temp_dir = tempfile.gettempdir()
            out_pcm = os.path.join(temp_dir, bname + "_dubbed.pcm")
            if not hasattr(self, "_temp_files_to_cleanup"): self._temp_files_to_cleanup = []
            self._temp_files_to_cleanup.append(out_pcm)

            with open(out_pcm, "wb") as f:
                while True:
                    opcode, payload = ws.recv()
                    if opcode is None:
                        reason = str(ws.close_reason)
                        if "1007" not in reason and "1000" not in reason:
                            log.error(f"Live Translate: WebSocket closed unexpectedly. Reason: {reason}")
                        break
                    if opcode == 0x9:
                        try: ws._send_frame(0xA, payload or b"")
                        except Exception: pass
                        continue
                    if opcode != 0x1 and opcode != 0x2: continue
                    try:
                        data = json.loads(payload.decode("utf-8", "replace"))
                        srv = data.get("serverContent") or data.get("server_content")
                        if srv:
                            turn = srv.get("modelTurn") or srv.get("model_turn")
                            if turn:
                                for part in turn.get("parts", []):
                                    inline = part.get("inlineData") or part.get("inline_data")
                                    if inline and "data" in inline:
                                        chunk = base64.b64decode(inline["data"])
                                        f.write(chunk)
                                        
                            is_complete = srv.get("turnComplete") or srv.get("turn_complete")
                            if is_complete and not sender_thread.is_alive():
                                break
                    except Exception: pass
            
            ws.close()
            sender_thread.join(timeout=2)
            try: ffmpeg_proc.kill()
            except: pass

            if os.path.getsize(out_pcm) == 0:
                # Translators: Error message shown when live dubbing fails to return any audio
                wx.CallAfter(show_error_dialog, _("Dubbing failed. No audio returned. Check NVDA log for details."))
                try: os.remove(out_pcm)
                except: pass
                return

            temp_mp3 = os.path.join(temp_dir, bname + "_dubbed_temp.mp3")
            self._temp_files_to_cleanup.append(temp_mp3)

            filter_complex = "[0:a]volume=0.35[bg];[bg][1:a]amix=inputs=2:duration=longest:normalize=0"
            proc = subprocess.run([
                ffmpeg_path, "-y",
                "-i", path,
                "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", out_pcm,
                "-filter_complex", filter_complex,
                "-ac", "2",
                temp_mp3
            ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, startupinfo=startupinfo, creationflags=CREATE_NO_WINDOW)
            
            if proc.returncode != 0 or not os.path.exists(temp_mp3):
                err = proc.stderr.decode('utf-8', 'ignore') if proc.stderr else 'None'
                log.error(f"Live Translate mixing failed (Return code: {proc.returncode}). Fallback to simple dubbing. ffmpeg stderr: {err}")
                subprocess.run([
                    ffmpeg_path, "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", out_pcm, "-y", temp_mp3
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=startupinfo, creationflags=CREATE_NO_WINDOW)

            try: os.remove(out_pcm)
            except: pass

            def _save_file():
                import gui
                default_file = os.path.basename(base) + "_dubbed.mp3"
                save_dlg = wx.FileDialog(
                    # Translators: Dialog title when saving a dubbed media file
                    gui.mainFrame, message=_("Save dubbed audio as"),
                    defaultDir=os.path.dirname(path), 
                    defaultFile=default_file,
                    wildcard="MP3 Audio (*.mp3)|*.mp3",
                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
                )
                save_dlg.Raise()
                if save_dlg.ShowModal() == wx.ID_OK:
                    import shutil
                    out_path = save_dlg.GetPath()
                    shutil.move(temp_mp3, out_path)
                    # Translators: Message reported when dubbed file is successfully saved
                    core.callLater(0, ui.message, _("Dubbed file saved: {path}").format(path=out_path))
                else:
                    try: os.remove(temp_mp3)
                    except: pass
                save_dlg.Destroy()

            wx.CallAfter(_save_file)
            # Translators: Status message when dubbing process finishes
            core.callLater(0, self.report_status, _("Dubbing finished."))

        except Exception as e:
            log.error(f"Live translate failed: {e}", exc_info=True)
            # Translators: Error message when live translate fails
            core.callLater(0, self.report_status, _("Dubbing failed."))
            wx.CallAfter(show_error_dialog, str(e))
        finally:
            self.current_status = _("Idle")