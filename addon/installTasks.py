import addonHandler
import gui
import os.path
import sys
import wx

addon = addonHandler.getCodeAddon()
addonName = addon.name
addonDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "globalPlugins", addonName))
if addonDir not in sys.path:
    sys.path.append(addonDir)

try:
    from donate_dialog import requestDonations
finally:
    if addonDir in sys.path:
        sys.path.remove(addonDir)

addonHandler.initTranslation()

def _doPostInstall():
    gui.mainFrame.prePopup()
    try:
        requestDonations(gui.mainFrame)
        # Translators: Message shown after the add-on is installed.
        msg = _("Installation of Vision Assistant Pro is complete. Please make sure to configure your API keys and preferences in the add-on settings to start using the features.")
        # Translators: Title of the installation complete dialog.
        title = _("Installation Complete")
        gui.messageBox(msg, title, wx.OK | wx.ICON_WARNING)
    finally:
        gui.mainFrame.postPopup()

def onInstall():
    wx.CallAfter(_doPostInstall)