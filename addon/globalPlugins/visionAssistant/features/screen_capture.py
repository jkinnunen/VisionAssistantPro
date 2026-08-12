# -*- coding: utf-8 -*-
import wx
import io
import base64
import ctypes
import logging
import tempfile
import os
import threading

import api
import textInfos
import NVDAObjects.behaviors
import core

import addonHandler

log = logging.getLogger(__name__)
addonHandler.initTranslation()

class ScreenCaptureMixin:

    def _getClipboardImageFile(self):
        path = None
        if not wx.TheClipboard.Open():
            return None
        try:
            if wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_BITMAP)):
                bmp_data = wx.BitmapDataObject()
                if wx.TheClipboard.GetData(bmp_data):
                    bmp = bmp_data.GetBitmap()
                    if bmp.IsOk():
                        fd, path = tempfile.mkstemp(suffix=".png")
                        os.close(fd)
                        if not bmp.SaveFile(path, wx.BITMAP_TYPE_PNG):
                            try: os.remove(path)
                            except Exception: pass
                            path = None
        except Exception as e:
            log.error(f"Clipboard image extraction failed: {e}")
            path = None
        finally:
            wx.TheClipboard.Close()
        return path

    def _capture_navigator(self):
        try:
            obj = api.getNavigatorObject()
            if not obj or not obj.location: return None, 0, 0, ""
            x, y, w, h = obj.location
            if w < 1 or h < 1: return None, 0, 0, ""
            bmp = wx.Bitmap(w, h)
            wx.MemoryDC(bmp).Blit(0, 0, w, h, wx.ScreenDC(), x, y)
            s = io.BytesIO()
            img = bmp.ConvertToImage()
            img.SetOption("quality", 90)
            img.SaveFile(s, wx.BITMAP_TYPE_JPEG)
            m = "image/jpeg"
            return base64.b64encode(s.getvalue()).decode('utf-8'), w, h, m
        except Exception as e:
            log.error(f"Screen capture failed: {e}")
            return None, 0, 0, ""

    def _capture_fullscreen(self):
        try:
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            dpi = 96
            if hwnd:
                try:
                    dpi = int(ctypes.windll.user32.GetDpiForWindow(hwnd))
                except Exception:
                    dpi = 96
            if dpi <= 0:
                dpi = 96
            scale = dpi / 96.0

            w_logical, h_logical = wx.GetDisplaySize()
            w_physical = int(round(w_logical * scale))
            h_physical = int(round(h_logical * scale))

            bmp = wx.Bitmap(w_physical, h_physical)
            screen = wx.ScreenDC()
            memory = wx.MemoryDC()
            memory.SelectObject(bmp)
            try:
                memory.Blit(0, 0, w_physical, h_physical, screen, 0, 0)
            finally:
                memory.SelectObject(wx.NullBitmap)

            image = bmp.ConvertToImage()
            if scale != 1.0:
                image = image.Scale(w_logical, h_logical, wx.IMAGE_QUALITY_HIGH)

            s = io.BytesIO()
            image.SetOption("quality", 90)
            image.SaveFile(s, wx.BITMAP_TYPE_JPEG)
            m = "image/jpeg"
            return base64.b64encode(s.getvalue()).decode('utf-8'), w_logical, h_logical, m
        except Exception as e:
            log.error(f"DPI-aware capture failed: {e}", exc_info=True)
            return None, 0, 0, ""

    def _capture_foreground(self):
        try:
            obj = api.getForegroundObject()
            if not obj or not obj.location: return None, 0, 0, 0, 0, ""
            x, y, w, h = obj.location
            if w < 1 or h < 1: return None, 0, 0, 0, 0, ""
            bmp = wx.Bitmap(w, h)
            wx.MemoryDC(bmp).Blit(0, 0, w, h, wx.ScreenDC(), x, y)
            s = io.BytesIO()
            img = bmp.ConvertToImage()
            img.SetOption("quality", 90)
            img.SaveFile(s, wx.BITMAP_TYPE_JPEG)
            m = "image/jpeg"
            return base64.b64encode(s.getvalue()).decode('utf-8'), x, y, w, h, m
        except Exception as e: 
            log.error(f"Foreground capture failed: {e}")
            return None, 0, 0, 0, 0, ""    

    def _get_text_smart(self):
        focus_obj = api.getFocusObject()
        if not focus_obj: return None

        if hasattr(focus_obj, "treeInterceptor") and focus_obj.treeInterceptor:
            try:
                info = focus_obj.treeInterceptor.makeTextInfo(textInfos.POSITION_SELECTION)
                if info and info.text and not info.text.isspace():
                    return info.text
            except Exception as e: log.debug(f"Selection extraction via treeInterceptor skipped: {e}")

        try:
            info = focus_obj.makeTextInfo(textInfos.POSITION_SELECTION)
            if info and info.text and not info.text.isspace():
                return info.text
        except Exception as e: log.debug(f"Selection extraction skipped: {e}")

        if isinstance(focus_obj, NVDAObjects.behaviors.EditableText):
            try:
                info = focus_obj.makeTextInfo(textInfos.POSITION_ALL)
                if info and info.text and not info.text.isspace():
                    return info.text
            except Exception as e: log.debug(f"EditableText extraction skipped: {e}")
        
        if isinstance(focus_obj, NVDAObjects.behaviors.Terminal):
            try:
                info = focus_obj.makeTextInfo(textInfos.POSITION_ALL)
                return info.text
            except Exception as e: log.debug(f"Terminal text extraction skipped: {e}")

        try:
            obj = api.getNavigatorObject()
            if not obj: return None
            
            content = []
            if getattr(obj, 'name', None): content.append(obj.name)
            if getattr(obj, 'value', None): content.append(obj.value)
            if getattr(obj, 'description', None): content.append(obj.description)
            
            if hasattr(obj, 'makeTextInfo'):
                try: 
                    ti = obj.makeTextInfo(textInfos.POSITION_ALL)
                    if ti.text and len(ti.text) < 2000: 
                        content.append(ti.text)
                except Exception as e: log.debug(f"Navigator obj makeTextInfo skipped: {e}")
                
            final_text = " ".join(list(dict.fromkeys([c for c in content if c and not c.isspace()])))
            return final_text if final_text else None
        except Exception as e: 
            log.debug(f"Smart text extraction final fallback skipped: {e}")
            return None

    def _capture_fullscreen_sync(self):
        res = [None, 0, 0, ""]
        evt = threading.Event()
        def do_cap():
            try:
                res[0], res[1], res[2], res[3] = self._capture_fullscreen()
            except Exception as e:
                log.warning(f"Capture fullscreen sync failed: {e}")
            finally: 
                evt.set()
        core.callLater(0, do_cap)
        evt.wait()
        return res[0], res[1], res[2], res[3]

    def _get_fg_app_name_sync(self):
        res = [""]
        evt = threading.Event()
        def do_get():
            try: res[0] = api.getForegroundObject().appModule.appName
            except Exception as e: 
                log.warning(f"Get fg app name sync failed: {e}")
            finally: 
                evt.set()
        core.callLater(0, do_get)
        evt.wait()
        return res[0]
        
    def _browse_and_run(self, worker_fn, wildcard, multiple=False):
        from ..utils.system import get_file_path
        # Translators: Message announced by NVDA when the live voice conversation ends.
        title = _("Open")
        path = get_file_path(title, wildcard, multiple=multiple)
        if path:
            threading.Thread(target=worker_fn, args=(path,), daemon=True).start()