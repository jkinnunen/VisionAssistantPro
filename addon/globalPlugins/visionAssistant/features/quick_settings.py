# -*- coding: utf-8 -*-
import json
import core
import ui
import addonHandler
import config as nvda_config

from .. import vision_config
from ..ai.core import AIHandler

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
        elif c == "Copy AI responses to clipboard": return _("On") if nvda_config.conf["VisionAssistant"].get("copy_to_clipboard", False) else _("Off")
        elif c == "Direct Output (No Chat Window)": return _("On") if nvda_config.conf["VisionAssistant"].get("skip_chat_dialog", False) else _("Off")
        elif c == "Clean Markdown in Chat": return _("On") if nvda_config.conf["VisionAssistant"].get("clean_markdown_chat", True) else _("Off")
        elif c == "Smart Swap": return _("On") if nvda_config.conf["VisionAssistant"].get("smart_swap", True) else _("Off")
            
        p = nvda_config.conf["VisionAssistant"]["active_provider"]
        k = "model_name" if c == "AI Model" and p == "gemini" else f"{p}_model_name" if c == "AI Model" else f"{p}_{c.split(' ')[0].lower()}_model"
        return nvda_config.conf["VisionAssistant"].get(k, "")

    def _announce_current_quick_setting(self, value_only=False):
        cats = ["AI Provider", "AI Model", "TTS Voice", "OCR Model", "STT Model", "TTS Model", "Operator / CAPTCHA Model", "Video Model", "Live Model", "Source Language", "Target Language", "AI Response Language", "Visual CAPTCHA Solver", "Text CAPTCHA Method", "OCR Engine", "Image Description in OCR", "Document Export Page Numbers", "Copy AI responses to clipboard", "Direct Output (No Chat Window)", "Clean Markdown in Chat", "Smart Swap"]
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
        cats = ["AI Provider", "AI Model", "TTS Voice", "OCR Model", "STT Model", "TTS Model", "Operator / CAPTCHA Model", "Video Model", "Live Model", "Source Language", "Target Language", "AI Response Language", "Visual CAPTCHA Solver", "Text CAPTCHA Method", "OCR Engine", "Image Description in OCR", "Document Export Page Numbers", "Copy AI responses to clipboard", "Direct Output (No Chat Window)", "Clean Markdown in Chat", "Smart Swap"]
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
        elif c == "Copy AI responses to clipboard":
            nvda_config.conf["VisionAssistant"]["copy_to_clipboard"] = not nvda_config.conf["VisionAssistant"].get("copy_to_clipboard", False)
        elif c == "Direct Output (No Chat Window)":
            nvda_config.conf["VisionAssistant"]["skip_chat_dialog"] = not nvda_config.conf["VisionAssistant"].get("skip_chat_dialog", False)
        elif c == "Clean Markdown in Chat":
            nvda_config.conf["VisionAssistant"]["clean_markdown_chat"] = not nvda_config.conf["VisionAssistant"].get("clean_markdown_chat", True)
        elif c == "Smart Swap":
            nvda_config.conf["VisionAssistant"]["smart_swap"] = not nvda_config.conf["VisionAssistant"].get("smart_swap", True)
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
        self._quick_settings_idx = (getattr(self, '_quick_settings_idx', 0) + 1) % 21
        self._announce_current_quick_setting()
    script_layerDown.keep_layer_alive = True

    def script_layerUp(self, gesture):
        self._quick_settings_idx = (getattr(self, '_quick_settings_idx', 0) - 1) % 21
        self._announce_current_quick_setting()
    script_layerUp.keep_layer_alive = True

    def script_layerRight(self, gesture):
        self._change_quick_setting(1)
    script_layerRight.keep_layer_alive = True

    def script_layerLeft(self, gesture):
        self._change_quick_setting(-1)
    script_layerLeft.keep_layer_alive = True