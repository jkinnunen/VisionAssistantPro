# -*- coding: utf-8 -*-
import core
import ui

# This holds the global instance of Vision Assistant Pro to avoid circular imports.
plugin_instance = None

def speak_status(msg):
    core.callLater(0, ui.message, msg)