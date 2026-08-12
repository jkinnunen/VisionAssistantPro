# -*- coding: utf-8 -*-
import json
import logging
import time
import datetime
import core
import ui
import scriptHandler
import addonHandler
import config as nvda_config

from .. import vision_config
from ..vision_config import ADDON_NAME
from ..ai.core import AIHandler

log = logging.getLogger(__name__)

addonHandler.initTranslation()

class QuickSettingsMixin:

    def _get_models_for_provider(self, p):
        if p == "gemini":
            raw = nvda_config.conf["VisionAssistant"].get("gemini_models_list", "")
            if raw:
                try: return [m["id"] for m in json.loads(raw)]
                except: return [part.split("|")[0] for part in raw.split(",") if "|" in part]
            return [m[1] for m in vision_config.MODELS]
        elif p in ("openai", "mistral", "groq", "custom"):
            raw = nvda_config.conf["VisionAssistant"].get(f"{p}_models_list", "")
            if raw:
                try: return [m["id"] for m in json.loads(raw)]
                except: return [part.split("|")[0] for part in raw.split(",") if "|" in part]
            return []
        elif p == "minimax": return ["MiniMax-M3"]
        return []

    def _get_quick_setting_value(self, c):
        if c == "AI Provider": return nvda_config.conf["VisionAssistant"]["active_provider"].capitalize()
        elif c == "OCR Engine":
            cur = nvda_config.conf["VisionAssistant"]["ocr_engine"]
            for name, val in vision_config.OCR_ENGINES:
                if val == cur: return name
            return cur
        elif c == "TTS Voice": return nvda_config.conf["VisionAssistant"]["tts_voice"]
        elif c == "Source Language": return vision_config.get_lang_name("source_language")
        elif c == "Target Language": return vision_config.get_lang_name("target_language")
        elif c == "AI Response Language": return vision_config.get_lang_name("ai_response_language")
        # Translators: Value representing the ON state for a toggle setting (e.g., in quick settings).
        elif c == "Visual CAPTCHA Solver": return _("On") if nvda_config.conf["VisionAssistant"].get("enable_visual_captcha_solver", True) else _("Off")
        elif c == "Text CAPTCHA Method": return _("Full Screen") if nvda_config.conf["VisionAssistant"].get("captcha_mode", "navigator") == "fullscreen" else _("Navigator Object")
        elif c == "Image Description in OCR": return _("On") if nvda_config.conf["VisionAssistant"].get("describe_images_ocr", True) else _("Off")
        elif c == "Document Export Page Numbers": return _("On") if nvda_config.conf["VisionAssistant"].get("document_export_page_numbers", True) else _("Off")
            
        p = nvda_config.conf["VisionAssistant"]["active_provider"]
        k = "model_name" if c == "AI Model" and p == "gemini" else f"{p}_model_name" if c == "AI Model" else f"{p}_{c.split(' ')[0].lower()}_model"
        return nvda_config.conf["VisionAssistant"].get(k, "")

    def _announce_current_quick_setting(self, value_only=False):
        cats = ["AI Provider", "AI Model", "TTS Voice", "OCR Model", "STT Model", "TTS Model", "Operator / CAPTCHA Model", "Video Model", "Live Model", "Source Language", "Target Language", "AI Response Language", "Visual CAPTCHA Solver", "Text CAPTCHA Method", "OCR Engine", "Image Description in OCR", "Document Export Page Numbers"]
        idx = getattr(self, "_quick_settings_idx", 0)
        c = cats[idx]
        val = self._get_quick_setting_value(c) or "Default"
        if value_only:
            core.callLater(0, ui.message, val)
        else:
            # Translators: Announced when navigating to AI Model quick settings
            msg = _("{setting}, Current: {val}. Use left and right arrows to change.").format(setting=c, val=val)
            core.callLater(0, ui.message, msg)

    def _change_quick_setting(self, direction):
        cats = ["AI Provider", "AI Model", "TTS Voice", "OCR Model", "STT Model", "TTS Model", "Operator / CAPTCHA Model", "Video Model", "Live Model", "Source Language", "Target Language", "AI Response Language", "Visual CAPTCHA Solver", "Text CAPTCHA Method", "OCR Engine", "Image Description in OCR", "Document Export Page Numbers"]
        idx = getattr(self, "_quick_settings_idx", 0)
        c = cats[idx]
        
        if c == "AI Provider":
            providers = ["gemini", "openai", "mistral", "groq", "minimax", "custom"]
            cur = nvda_config.conf["VisionAssistant"]["active_provider"]
            try: i = providers.index(cur)
            except: i = 0
            for _i in range(len(providers)):
                i = (i + direction) % len(providers)
                p = providers[i]
                if p == "custom": break
                k = "api_key" if p == "gemini" else f"{p}_api_key"
                if nvda_config.conf["VisionAssistant"].get(k, "").strip(): break
            nvda_config.conf["VisionAssistant"]["active_provider"] = providers[i]
        elif c == "OCR Engine":
            opts = [val for name, val in vision_config.OCR_ENGINES]
            cur = nvda_config.conf["VisionAssistant"]["ocr_engine"]
            try: i = opts.index(cur)
            except: i = 0
            i = (i + direction) % len(opts)
            nvda_config.conf["VisionAssistant"]["ocr_engine"] = opts[i]
        elif c == "TTS Voice":
            opts = [v[0] for v in vision_config.GEMINI_VOICES] + [v[0] for v in vision_config.OPENAI_VOICES]
            unique_opts = list(dict.fromkeys(opts))
            cur = nvda_config.conf["VisionAssistant"]["tts_voice"]
            try: i = unique_opts.index(cur)
            except: i = 0
            i = (i + direction) % len(unique_opts)
            nvda_config.conf["VisionAssistant"]["tts_voice"] = unique_opts[i]
        elif c in ["Source Language", "Target Language", "AI Response Language"]:
            opts = [x[1] for x in (vision_config.SOURCE_LIST if c == "Source Language" else vision_config.TARGET_LIST)]
            cur = nvda_config.conf["VisionAssistant"][c.lower().replace(" ", "_")]
            try: i = opts.index(cur)
            except: i = 0
            i = (i + direction) % len(opts)
            nvda_config.conf["VisionAssistant"][c.lower().replace(" ", "_")] = opts[i]
        elif c == "Visual CAPTCHA Solver":
            nvda_config.conf["VisionAssistant"]["enable_visual_captcha_solver"] = not nvda_config.conf["VisionAssistant"].get("enable_visual_captcha_solver", True)
        elif c == "Text CAPTCHA Method":
            mode = nvda_config.conf["VisionAssistant"].get("captcha_mode", "navigator")
            nvda_config.conf["VisionAssistant"]["captcha_mode"] = "fullscreen" if mode == "navigator" else "navigator"
        elif c == "Image Description in OCR":
            nvda_config.conf["VisionAssistant"]["describe_images_ocr"] = not nvda_config.conf["VisionAssistant"].get("describe_images_ocr", True)
        elif c == "Document Export Page Numbers":
            nvda_config.conf["VisionAssistant"]["document_export_page_numbers"] = not nvda_config.conf["VisionAssistant"].get("document_export_page_numbers", True)
        else:
            p = nvda_config.conf["VisionAssistant"]["active_provider"]
            models = self._get_models_for_provider(p)
            if c == "AI Model":
                filtered = AIHandler.filter_models(p, [(m, m) for m in models], task="main")
                models = [m[0] for m in filtered]
            else: models.insert(0, "")
            if not models:
                # Translators: Warning when models list is not fetched
                core.callLater(0, ui.message, _("No models fetched for {provider}. Please update models list from settings.").format(provider=p.capitalize()))
                return
            k = "model_name" if c == "AI Model" and p == "gemini" else f"{p}_model_name" if c == "AI Model" else f"{p}_{c.split(' ')[0].lower()}_model"
            if c != "AI Model": nvda_config.conf["VisionAssistant"]["advanced_model_routing"] = True
            cur = nvda_config.conf["VisionAssistant"].get(k, "")
            try: i = models.index(cur)
            except: i = 0
            i = (i + direction) % len(models)
            nvda_config.conf["VisionAssistant"][k] = models[i]
            
        self._announce_current_quick_setting(value_only=True)

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

    # Translators: Script description for 'Reports the number of Gemini API keys that have exceeded their daily quota and their reset time.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Reports the number of Gemini API keys that have exceeded their daily quota and their reset time."), category=ADDON_NAME)
    def script_reportQuotaExhaustedKeys(self, gesture):
        if getattr(self, "toggling", False): self.finish()
        if not AIHandler.is_gemini():
            # Translators: Message shown when a user tries to check Gemini API quotas but another provider is active.
            core.callLater(0, ui.message, _("This feature is only available for Google Gemini."))
            return
        try:
            banned_str = nvda_config.conf["VisionAssistant"].get("banned_gemini_keys", "{}")
            banned = json.loads(banned_str)
        except Exception as e:
            log.warning(f"Parse banned keys failed: {e}")
            banned = {}
            
        now = time.time()
        unique_keys = {}
        max_time_per_key = {}
        
        for k_m, ban_time in list(banned.items()):
            if now < ban_time:
                parts = k_m.split("::")
                k = parts[0]
                m = parts[1] if len(parts) > 1 else "Unknown"
                if k not in unique_keys: unique_keys[k] = []
                unique_keys[k].append(m)
                max_time_per_key[k] = max(max_time_per_key.get(k, 0), ban_time)
            else:
                del banned[k_m]
                
        nvda_config.conf["VisionAssistant"]["banned_gemini_keys"] = json.dumps(banned)
        
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
            # Translators: Prefix for time when the daily quota resets on the next day
            if ban_date > today: time_str = _("tomorrow at {time}").format(time=time_str)
            # Translators: Shows detailed information for a banned API key. {key} is the API key, {model} is the model name, {time_str} is the reset time.
            key_info = _("Key: {key}\nModel: {model}\nResets around: {time_str}\n").format(key=k, model=model_str, time_str=time_str)
            msg_parts.append(key_info)

        model_counts = {}
        for models in unique_keys.values():
            for m in models: model_counts[m] = model_counts.get(m, 0) + 1
                
        summary_parts = []
        for m, count in model_counts.items():
            # Translators: Shows how many API keys have exceeded their quota for a specific model. {count} is the number of keys, {model} is the model name.
            summary_parts.append(_("{count} keys for model {model}").format(count=count, model=m))
            
        # Translators: Message shown when API keys run out of quota.
        summary_msg = ", ".join(summary_parts) + " " + _("have exceeded their daily quota.")
        final_msg = summary_msg + "\n\n" + "\n".join(msg_parts).strip()
        # Translators: Title of the browseable message dialog showing exhausted API keys
        ui.browseableMessage(final_msg, _("Exhausted API Keys"))

    # Translators: Script description for 'Reports the AI models selected in advanced routing.' in Input Gestures dialog.
    @scriptHandler.script(description=_("Reports the AI models selected in advanced routing."), category=ADDON_NAME)
    def script_reportSelectedModels(self, gesture):
        if getattr(self, "toggling", False): self.finish()
        models = []
        conf = nvda_config.conf["VisionAssistant"]
        p = conf.get("active_provider", "gemini")
        
        m_key = "model_name" if p == "gemini" else f"{p}_model_name"
        main_m = conf.get(m_key, "")
        # Translators: Prefix for main model status
        if main_m: models.append(_("Main: {model}").format(model=main_m))
        
        def add_adv(task, name):
            m = conf.get(f"{p}_{task}_model", "")
            if m and "Default" not in m and "Auto" not in m: models.append(f"{name}: {m}")
                
        add_adv("ocr", _("OCR"))
        # Translators: Abbreviation for Speech-to-Text.
        add_adv("stt", _("STT"))
        # Translators: Abbreviation for Text-to-Speech.
        add_adv("tts", _("TTS"))
        # Translators: Labels for the AI and User in chat history
        add_adv("operator", _("Operator"))
        add_adv("video", _("Video"))
        add_adv("live", _("Live"))
        
        # Translators: Message when no specific AI models are selected in advanced routing
        if not models: ui.message(_("No specific models selected."))
        else: ui.message(". ".join(models))