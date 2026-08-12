import addonHandler
import gui
import config
import os.path
import sys
import wx
import shutil
import tempfile
import json
import time
import gc

addon = addonHandler.getCodeAddon()
addonName = addon.name

def _backup_lib_assets():
    try:
        current_name = addonName.lower()
        for add in addonHandler.getAvailableAddons():
            if add.name.lower() == current_name or "vision" in add.name.lower():
                old_lib_dir = os.path.join(add.path, "globalPlugins", add.name, "lib")
                if not os.path.exists(old_lib_dir):
                    old_lib_dir = os.path.join(add.path, "lib")

                if os.path.exists(old_lib_dir):
                    backup_dir = os.path.join(tempfile.gettempdir(), "VisionAssistant_Lib_Backup")
                    if os.path.exists(backup_dir):
                        try:
                            shutil.rmtree(backup_dir, ignore_errors=True)
                        except Exception:
                            pass
                    os.makedirs(backup_dir, exist_ok=True)

                    persistent_items = ["ffmpeg.exe", "espeak-ng"]
                    copied = False
                    for item in persistent_items:
                        src = os.path.join(old_lib_dir, item)
                        dst = os.path.join(backup_dir, item)
                        if os.path.exists(src):
                            try:
                                if os.path.isdir(src):
                                    shutil.copytree(src, dst)
                                else:
                                    shutil.copy2(src, dst)
                                copied = True
                            except Exception:
                                pass

                    if copied:
                        manifest_file = os.path.join(backup_dir, "backup_manifest.json")
                        with open(manifest_file, "w", encoding="utf-8") as f:
                            json.dump({"timestamp": time.time()}, f)
                break
    except Exception:
        pass
    finally:
        gc.collect()

def _doPostInstall():
    addonDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "globalPlugins", addonName))
    if addonDir not in sys.path:
        sys.path.append(addonDir)

    try:
        from dialogs.donate import requestDonations
        gui.mainFrame.prePopup()
        try:
            requestDonations(gui.mainFrame)
            
            conf = config.conf["VisionAssistant"]
            api_keys = [
                conf.get("api_key"),
                conf.get("openai_api_key"),
                conf.get("mistral_api_key"),
                conf.get("groq_api_key"),
                conf.get("minimax_api_key"),
                conf.get("custom_api_key")
            ]
            
            if not any(key and str(key).strip() for key in api_keys):
                # Translators: Message shown after the add-on is installed.
                msg = _("Installation of Vision Assistant Pro is complete. Please make sure to configure your API keys and preferences in the add-on settings to start using the features.")
                # Translators: Title of the installation complete dialog.
                title = _("Installation Complete")
                gui.messageBox(msg, title, wx.OK | wx.ICON_WARNING)
        finally:
            gui.mainFrame.postPopup()
    finally:
        if addonDir in sys.path:
            sys.path.remove(addonDir)

def onInstall():
    _backup_lib_assets()
    wx.CallAfter(_doPostInstall)