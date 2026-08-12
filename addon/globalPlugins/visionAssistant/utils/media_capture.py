# -*- coding: utf-8 -*-
import os
import json
import ssl
import socket
import struct
import time
import re
import base64
import threading
import tempfile
import ctypes
import array
import logging
import urllib.parse
import wx
from urllib import request, error
from urllib.parse import urlparse, quote, urlencode
from http import cookiejar

import subprocess
import sys
import zipfile
import shutil

import config
import gui
import core
import ui
import nvwave

from .. import plugin_state
from .. import vision_config
from .system import show_error_dialog

log = logging.getLogger(__name__)

_ = vision_config._ if hasattr(vision_config, '_') else (lambda x: x)


# Proxy / HTTP helpers

def get_proxy_opener(target_url=None):
    proxy_url = config.conf["VisionAssistant"]["proxy_url"].strip()

    is_local = False
    if target_url:
        parsed_target = urlparse(target_url)
        hostname = parsed_target.hostname or ""
        if hostname.lower() in ["localhost", "127.0.0.1"]:
            is_local = True

    is_reverse_proxy = False
    if proxy_url:
        try:
            clean_proxy = proxy_url if "://" in proxy_url else "http://" + proxy_url
            parsed_proxy = urlparse(clean_proxy)
            p_host = parsed_proxy.hostname or ""
            if p_host and "." in p_host and not p_host.replace(".", "").isdigit() and p_host.lower() not in ["localhost", "127.0.0.1"]:
                is_reverse_proxy = True
        except Exception:
            pass

    if is_local or is_reverse_proxy:
        opener = request.build_opener(request.ProxyHandler({}))
    else:
        opener = request.build_opener()
        if proxy_url:
            if not (proxy_url.startswith("http://") or proxy_url.startswith("https://")):
                proxy_url = "http://" + proxy_url
            try:
                parsed = urlparse(proxy_url)
                if parsed.username:
                    proxy_host = parsed.hostname
                    if parsed.port:
                        proxy_host += f":{parsed.port}"
                    clean_proxy_url = f"{parsed.scheme}://{proxy_host}"
                    auth_str = f"{parsed.username}:{parsed.password or ''}"
                    encoded_auth = base64.b64encode(auth_str.encode()).decode()
                    handler = request.ProxyHandler({'http': clean_proxy_url, 'https': clean_proxy_url})
                    opener = request.build_opener(handler)
                    opener.addheaders.append(('Proxy-Authorization', f'Basic {encoded_auth}'))
                else:
                    handler = request.ProxyHandler({'http': proxy_url, 'https': proxy_url})
                    opener = request.build_opener(handler)
            except Exception as e:
                log.error(f"Proxy Setup Failed: {e}")
    opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'))
    return opener


# FFmpeg utilities

def ensure_ffmpeg():
    lib_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib")
    ffmpeg_lib_path = os.path.join(lib_dir, "ffmpeg.exe")

    if os.path.exists(ffmpeg_lib_path): return ffmpeg_lib_path

    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, timeout=5)
        if result.returncode == 0: return "ffmpeg"
    except Exception: pass

    # Translators: Title of dialog asking user to download ffmpeg
    title = _("Download ffmpeg?")
    # Translators: Message in dialog asking user to download ffmpeg for video processing
    message = _("Video processing requires ffmpeg (approximately 70MB download).\n\nDownload ffmpeg now to the addon's lib folder?\n\nThis is a one-time download.")

    user_choice = [wx.ID_NO]
    if core.isMainThread():
        gui.mainFrame.prePopup()
        try:
            dlg = wx.MessageDialog(gui.mainFrame, message, title, wx.YES_NO | wx.ICON_QUESTION)
            user_choice[0] = dlg.ShowModal()
            dlg.Destroy()
        finally:
            gui.mainFrame.postPopup()

        if user_choice[0] != wx.ID_YES:
            # Translators: Message reported when user cancels downloading ffmpeg required for video processing
            core.callLater(0, ui.message, _("Operation cancelled. ffmpeg is required for video processing."))
            return None

        result_holder = [None]
        done = threading.Event()

        def _download():
            try:
                result_holder[0] = download_ffmpeg(ffmpeg_lib_path)
            finally:
                done.set()

        threading.Thread(target=_download, daemon=True).start()
        done.wait()
        return result_holder[0]

    user_choice = [wx.ID_NO]
    dlg_closed = threading.Event()

    def ask_user():
        gui.mainFrame.prePopup()
        try:
            dlg = wx.MessageDialog(gui.mainFrame, message, title, wx.YES_NO | wx.ICON_QUESTION)
            user_choice[0] = dlg.ShowModal()
            dlg.Destroy()
        finally:
            gui.mainFrame.postPopup()
            dlg_closed.set()

    wx.CallAfter(ask_user)
    dlg_closed.wait()

    if user_choice[0] != wx.ID_YES:
        # Translators: Message reported when user cancels downloading ffmpeg required for video processing
        core.callLater(0, ui.message, _("Operation cancelled. ffmpeg is required for video processing."))
        return None

    return download_ffmpeg(ffmpeg_lib_path)

def download_ffmpeg(target_path):
    try:
        # Translators: Status message when downloading ffmpeg
        core.callLater(0, ui.message, _("Downloading ffmpeg, please wait..."))
        download_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
        from urllib import request
        opener = get_proxy_opener(download_url)
        req = request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
        zip_path = target_path + ".zip"
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
                        if downloaded % (10 * 1024 * 1024) < 1024 * 1024:
                            # Translators: Progress message during ffmpeg download, {percent} is download percentage
                            core.callLater(0, ui.message, _("Downloading ffmpeg: {percent}%").format(percent=percent))

        # Translators: Status message when extracting ffmpeg
        core.callLater(0, ui.message, _("Extracting ffmpeg..."))
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            ffmpeg_file = None
            for name in zip_ref.namelist():
                if name.endswith('bin/ffmpeg.exe'): ffmpeg_file = name; break
            if ffmpeg_file:
                temp_extract = os.path.join(tempfile.gettempdir(), "ffmpeg_temp_extract")
                os.makedirs(temp_extract, exist_ok=True)
                zip_ref.extract(ffmpeg_file, temp_extract)
                shutil.move(os.path.join(temp_extract, ffmpeg_file), target_path)
                try: shutil.rmtree(temp_extract)
                except Exception: pass
        try: os.remove(zip_path)
        except Exception: pass

        if os.path.exists(target_path):
            # Translators: Success message after ffmpeg download completes
            core.callLater(0, ui.message, _("ffmpeg downloaded successfully!"))
            if plugin_state.plugin_instance:
                plugin_state.plugin_instance.current_status = _("Idle")
            return target_path
        else: raise Exception("Failed to extract ffmpeg.exe")
    except Exception as e:
        log.error(f"ffmpeg download failed: {e}", exc_info=True)
        # Translators: Error message when ffmpeg download fails
        wx.CallAfter(show_error_dialog, _("Failed to download ffmpeg: {error}").format(error=str(e)))
        if plugin_state.plugin_instance:
            plugin_state.plugin_instance.current_status = _("Idle")
        return None

def compress_video(input_path):
    ffmpeg_path = ensure_ffmpeg()
    if not ffmpeg_path: return None

    fd, temp_path = tempfile.mkstemp(suffix=".mp4", prefix="vision_assistant_comp_")
    os.close(fd)

    cmd = [
        ffmpeg_path, "-i", input_path,
        "-vf", "scale=-2:min(480\\,ih)",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "30",
        "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", "-y", temp_path
    ]

    startupinfo = None
    creationflags = 0
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        creationflags = 0x08000000

    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, creationflags=creationflags, check=True)
        try:
            if os.path.getsize(temp_path) >= os.path.getsize(input_path):
                os.remove(temp_path)
                return input_path
        except Exception: pass
        return temp_path
    except subprocess.CalledProcessError as e:
        log.error(f"Video compression failed: {e.stderr}")
        try: os.remove(temp_path)
        except Exception: pass
        return None


# Online video download link extractors

def get_twitter_download_link(tweet_url):
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    base_url = "https://savetwitter.net/en4"
    api_url = "https://savetwitter.net/api/ajaxSearch"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'X-Requested-With': 'XMLHttpRequest', 'Referer': base_url}
    try:
        req_init = request.Request(base_url, headers=headers)
        opener.open(req_init)
        params = {'q': tweet_url, 'lang': 'en', 'cftoken': ''}
        data = urlencode(params).encode('utf-8')
        req_post = request.Request(api_url, data=data, headers=headers, method='POST')
        with opener.open(req_post) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get('status') == 'ok':
                html = res_data.get('data', '')
                match = re.search(r'href="(https?://dl\.snapcdn\.app/[^"]+)"', html)
                if match: return match.group(1)
    except Exception as e:
        log.error(f"Twitter download extraction failed: {e}")
    return None

def get_instagram_download_link(insta_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://indown.io/en1"
    }
    try:
        cookie_handler = request.HTTPCookieProcessor()
        opener = get_proxy_opener()
        opener.add_handler(cookie_handler)

        req_get = request.Request("https://indown.io/en1", headers=headers)
        with opener.open(req_get, timeout=15) as res:
            html_page = res.read().decode('utf-8')

        token_match = re.search(r'name="_token"\s+value="([^"]+)"|value="([^"]+)"\s+name="_token"', html_page)
        if not token_match:
            log.error("Failed to extract CSRF token from indown.io.")
            return None
        csrf_token = token_match.group(1) if token_match.group(1) else token_match.group(2)

        payload = {
            "referer": "https://indown.io/en1",
            "locale": "en",
            "_token": csrf_token,
            "link": insta_url,
            "p": "p"
        }
        data = urlencode(payload).encode('utf-8')

        post_headers = headers.copy()
        post_headers["Content-Type"] = "application/x-www-form-urlencoded"
        post_headers["Origin"] = "https://indown.io"

        req_post = request.Request("https://indown.io/download", data=data, headers=post_headers, method='POST')

        with opener.open(req_post, timeout=20) as res:
            result_html = res.read().decode('utf-8')

            links = re.findall(r'href="(https?://[^"\s]+/fetch\?url=[^"\s]+)"', result_html)
            if not links:
                links = re.findall(r'href="(https?://[^\s"]+cdninstagram[^\s"]+\.mp4[^\s"]+)"', result_html)
            if not links:
                links = re.findall(r'href="(https?://[^\s"]+rapidcdn[^\s"]+)"', result_html)
            if not links:
                links = re.findall(r'href="(https?://[^\s"]+\.mp4[^\s"]+)"', result_html)

            if links:
                return links[0].replace('&amp;', '&')
    except Exception as e:
        log.error(f"Instagram download extraction failed: {e}")
    return None

def get_tiktok_download_link(tiktok_url):
    api_url = "https://www.tikwm.com/api/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        params = {'url': tiktok_url, 'hd': '1'}
        data = urlencode(params).encode('utf-8')
        req = request.Request(api_url, data=data, headers=headers, method='POST')
        opener = get_proxy_opener()
        with opener.open(req, timeout=120) as response:
            res = json.loads(response.read().decode('utf-8'))
            if res.get('code') == 0:
                play_url = res['data']['play']
                return play_url if play_url.startswith('http') else "https://www.tikwm.com" + play_url
    except Exception as e:
        log.error(f"TikTok download extraction failed: {e}")
    return None

def _download_temp_video(url, abort_checker=None):
    try:
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        opener = get_proxy_opener(url)
        with opener.open(req, timeout=600) as response:
            fd, path = tempfile.mkstemp(suffix=".mp4")
            os.close(fd)
            try:
                with open(path, 'wb') as f:
                    while True:
                        if abort_checker and abort_checker(): break
                        chunk = response.read(8192)
                        if not chunk: break
                        f.write(chunk)
                if abort_checker and abort_checker():
                    try: os.remove(path)
                    except Exception: pass
                    return None
                return path
            except Exception as e:
                log.error(f"Error writing temp video: {e}")
                if os.path.exists(path):
                    try: os.remove(path)
                    except Exception: pass
                return None
    except Exception as e:
        log.error(f"Error downloading temp video: {e}")
    return None


# Video source classes

class _LocalVideoSource:

    is_direct = False

    def __init__(self, path):
        self.path = path
        # Translators: Error message shown when processing a local video file fails.
        self.error_message = _("Error processing local video.")
        self.log_label = "Local video thread failed"
        self._compressed_path = None

    def prepare(self, report, abort_check):
        return True

    def ensure_local(self, owner, report, abort_check):
        if self._compressed_path and os.path.exists(self._compressed_path):
            return self._compressed_path
        # Translators: Status message when compressing a local video file before uploading.
        report(_("Compressing video (this may take a moment)..."))
        self._compressed_path = compress_video(self.path)
        if not self._compressed_path:
            # Translators: Error message shown when video compression fails or was cancelled by the user.
            report(_("Error: Video compression failed or was cancelled."))
            return None
        return self._compressed_path

    def duration(self, file_uri):
        from ..ai.providers.gemini import GeminiHandler
        return getattr(GeminiHandler, '_file_durations', {}).get(file_uri)

    def cleanup(self):
        cp = self._compressed_path
        if cp and cp != self.path and os.path.exists(cp):
            try: os.remove(cp)
            except Exception: pass


class _DownloadVideoSource:

    is_direct = False

    def __init__(self, url, platform):
        self.url = url
        self.platform = platform
        # Translators: Error message shown when processing an online video fails.
        self.error_message = _("Error processing video.")
        self.log_label = "Online video analysis thread failed"
        self._direct_link = None
        self._temp_path = None

    def prepare(self, report, abort_check):
        # Translators: Message reported when the add-on starts processing an online video link.
        report(_("Processing Video..."))
        return True

    def _extract_link(self, report):
        if self.platform == "instagram":
            link = get_instagram_download_link(self.url)
            # Translators: Error message when the add-on fails to get a direct download link for an Instagram video.
            err = _("Error: Could not extract Instagram video.")
        elif self.platform == "twitter":
            link = get_twitter_download_link(self.url)
            # Translators: Error message when the add-on fails to get a direct download link for a Twitter/X video.
            err = _("Error: Could not extract Twitter video.")
        else:
            link = get_tiktok_download_link(self.url)
            # Translators: Error message when the add-on fails to get a direct download link for a TikTok video.
            err = _("Error: Could not extract TikTok video.")
        if not link:
            log.error(f"Video direct link extraction failed for: {self.url}")
            report(err)
        return link

    def ensure_local(self, owner, report, abort_check):
        if self._temp_path and os.path.exists(self._temp_path):
            return self._temp_path
        if abort_check(): return None
        if not self._direct_link:
            self._direct_link = self._extract_link(report)
            if not self._direct_link:
                return None
        if abort_check(): return None
        # Translators: Message reported when the add-on is downloading the video from the extracted link.
        report(_("Downloading Video..."))
        self._temp_path = _download_temp_video(self._direct_link, abort_checker=abort_check)
        if not self._temp_path:
            log.error(f"Video download failed for link: {self._direct_link}")
            # Translators: Error message when downloading the online video fails.
            report(_("Error: Download failed."))
            return None
        return self._temp_path

    def duration(self, file_uri):
        from ..ai.providers.gemini import GeminiHandler
        return getattr(GeminiHandler, '_file_durations', {}).get(file_uri)

    def cleanup(self):
        if self._temp_path and os.path.exists(self._temp_path):
            try: os.remove(self._temp_path)
            except Exception: pass


class _YouTubeVideoSource:

    is_direct = True

    def __init__(self, url):
        self.url = self._clean_youtube_url(url)
        self.error_message = _("Error processing video.")
        self.log_label = "Online video analysis thread failed"

    def _clean_youtube_url(self, url):
        try:
            parsed = urllib.parse.urlparse(url)
            domain = parsed.netloc.lower()

            if "youtube.com" in domain:
                if parsed.path == "/watch":
                    qs = urllib.parse.parse_qs(parsed.query)
                    if 'v' in qs:
                        return f"https://www.youtube.com/watch?v={qs['v'][0]}"
                elif parsed.path.startswith("/shorts/"):
                    video_id = parsed.path.split("/shorts/")[1].split("?")[0].split("/")[0]
                    return f"https://www.youtube.com/watch?v={video_id}"

            elif "youtu.be" in domain:
                video_id = parsed.path.lstrip('/').split("?")[0].split("/")[0]
                return f"https://www.youtube.com/watch?v={video_id}"

        except Exception as e:
            log.warning(f"YouTube URL cleanup failed: {e}")

        return url

    @property
    def direct_uri(self):
        return self.url

    def prepare(self, report, abort_check):
        report(_("Processing Video..."))
        return True

    def ensure_local(self, owner, report, abort_check):
        return None

    def duration(self, file_uri):
        return None

    def cleanup(self):
        pass


class _InvalidVideoSource:
    is_direct = False

    def __init__(self, message):
        self.message = message
        self.error_message = message
        self.log_label = "Online video analysis thread failed"

    def prepare(self, report, abort_check):
        report(self.message)
        return False

    def ensure_local(self, owner, report, abort_check):
        return None

    def duration(self, file_uri):
        return None

    def cleanup(self):
        pass


# Progress file reader

class ProgressFileReader:
    def __init__(self, file_path, callback=None, abort_checker=None):
        self.file_path = file_path
        self.callback = callback
        self.abort_checker = abort_checker
        self.total_size = os.path.getsize(file_path)
        self.bytes_read = 0
        self.last_reported_percent = 0

    def __iter__(self):
        with open(self.file_path, 'rb') as f:
            while True:
                if self.abort_checker and self.abort_checker():
                    raise Exception("Upload aborted")

                chunk = f.read(1024 * 512)
                if not chunk:
                    break

                self.bytes_read += len(chunk)
                if self.total_size > 0:
                    percent = int((self.bytes_read / self.total_size) * 100)
                    if percent >= self.last_reported_percent + 10:
                        self.last_reported_percent = (percent // 10) * 10
                        if self.callback:
                            self.callback(self.last_reported_percent)

                yield chunk

    def __len__(self):
        return self.total_size


# Minimal WebSocket client (for Live session)

class _MinimalWebSocket:

    def __init__(self, host, path, port=443, is_ssl=True, timeout=30):
        self.host = host
        self.path = path
        self.port = port
        self.is_ssl = is_ssl
        self.timeout = timeout
        self.sock = None
        self._recv_buf = b""
        self.closed = False
        self.close_reason = None
        self._send_lock = threading.Lock()

    def _get_effective_proxy(self):
        proxy_url = config.conf["VisionAssistant"]["proxy_url"].strip()
        if not proxy_url:
            try:
                sys_proxies = request.getproxies()
                proxy_url = sys_proxies.get('https') or sys_proxies.get('http') or ""
            except Exception:
                proxy_url = ""
        if proxy_url and "://" not in proxy_url:
            proxy_url = "http://" + proxy_url
        return proxy_url if proxy_url else None

    def _connect_via_socks5(self, proxy_parsed, timeout):
        p_host = proxy_parsed.hostname
        p_port = proxy_parsed.port or 1080
        s = socket.create_connection((p_host, p_port), timeout=timeout)
        if proxy_parsed.username and proxy_parsed.password:
            s.sendall(b"\x05\x02\x00\x02")
        else:
            s.sendall(b"\x05\x01\x00")
        res = s.recv(2)
        if len(res) < 2 or res[0] != 5:
            s.close()
            raise ConnectionError("SOCKS5 proxy invalid response")
        if res[1] == 2:
            u, p = proxy_parsed.username.encode(), (proxy_parsed.password or '').encode()
            s.sendall(struct.pack("BB", 1, len(u)) + u + struct.pack("B", len(p)) + p)
            if s.recv(2)[1] != 0:
                s.close()
                raise ConnectionError("SOCKS5 auth failed")
        elif res[1] != 0:
            s.close()
            raise ConnectionError(f"Unsupported SOCKS5 auth method: {res[1]}")
        host_b = self.host.encode()
        s.sendall(struct.pack(">BBBB", 5, 1, 0, 3) + struct.pack("B", len(host_b)) + host_b + struct.pack(">H", self.port))
        resp = s.recv(10)
        if len(resp) < 4 or resp[1] != 0:
            s.close()
            raise ConnectionError(f"SOCKS5 connection failed with status code: {resp[1] if len(resp) >= 2 else 'unknown'}")
        return s

    def _connect_via_http_proxy(self, proxy_parsed, timeout):
        p_host = proxy_parsed.hostname
        p_port = proxy_parsed.port or 80
        s = socket.create_connection((p_host, p_port), timeout=timeout)
        connect_req = f"CONNECT {self.host}:{self.port} HTTP/1.1\r\nHost: {self.host}:{self.port}\r\n"
        if proxy_parsed.username:
            auth = base64.b64encode(f"{proxy_parsed.username}:{proxy_parsed.password or ''}".encode()).decode()
            connect_req += f"Proxy-Authorization: Basic {auth}\r\n"
        connect_req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n\r\n"
        s.sendall(connect_req.encode())
        resp = b""
        while b"\r\n\r\n" not in resp:
            chunk = s.recv(4096)
            if not chunk:
                s.close()
                raise ConnectionError("Proxy tunnel closed connection abruptly.")
            resp += chunk
        if b" 200 " not in resp.split(b"\r\n", 1)[0]:
            s.close()
            status_line = resp.split(b"\r\n", 1)[0].decode(errors='ignore')
            raise ConnectionError(f"Proxy tunnel failed: {status_line}")
        return s

    def connect(self):
        proxy_url = self._get_effective_proxy()
        raw = None

        if proxy_url:
            try:
                parsed = urlparse(proxy_url)
                scheme = (parsed.scheme or "http").lower()
                if "socks" in scheme:
                    raw = self._connect_via_socks5(parsed, self.timeout)
                else:
                    raw = self._connect_via_http_proxy(parsed, self.timeout)
            except Exception as e:
                log.error(f"Proxy connection failed: {e}")
                if raw:
                    try: raw.close()
                    except Exception: pass
                raise
        else:
            raw = socket.create_connection((self.host, self.port), timeout=self.timeout)

        if self.is_ssl:
            ctx = ssl.create_default_context()
            self.sock = ctx.wrap_socket(raw, server_hostname=self.host)
        else:
            self.sock = raw

        key = base64.b64encode(os.urandom(16)).decode()
        handshake = (
            f"GET {self.path} HTTP/1.1\r\n"
            f"Host: {self.host}\r\n"
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36\r\n"
            "Origin: https://aistudio.google.com\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        self.sock.sendall(handshake.encode())

        resp = b""
        while b"\r\n\r\n" not in resp:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("WebSocket handshake closed")
            resp += chunk

        if b" 101 " not in resp.split(b"\r\n", 1)[0]:
            try:
                status_line = resp.split(b"\r\n", 1)[0].decode(errors='ignore')
                body = resp.split(b"\r\n\r\n", 1)[1].decode(errors='ignore')
                err_msg = f"WebSocket handshake failed: {status_line} Body: {body[:500]}"
            except Exception:
                err_msg = f"WebSocket handshake failed: {resp[:120]!r}"
            raise ConnectionError(err_msg)

        self._recv_buf = resp.split(b"\r\n\r\n", 1)[1]
        self.sock.settimeout(1.0)

    def _send_frame(self, opcode, payload):
        if self.closed:
            return
        header = bytearray()
        header.append(0x80 | opcode)
        mask = os.urandom(4)
        length = len(payload)
        if length < 126:
            header.append(0x80 | length)
        elif length < 65536:
            header.append(0x80 | 126)
            header += struct.pack(">H", length)
        else:
            header.append(0x80 | 127)
            header += struct.pack(">Q", length)
        header += mask
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        frame = bytes(header) + masked
        with self._send_lock:
            if self.closed:
                return
            self.sock.sendall(frame)

    def send_text(self, text):
        self._send_frame(0x1, text.encode("utf-8"))

    def _recv_exact(self, n):
        while len(self._recv_buf) < n:
            if self.closed:
                raise ConnectionError("WebSocket closed")
            try:
                chunk = self.sock.recv(65536)
                if not chunk:
                    self.close()
                    raise ConnectionError("WebSocket connection closed")
                self._recv_buf += chunk
            except (BlockingIOError, ssl.SSLWantReadError, socket.timeout):
                time.sleep(0.05)
                continue
            except ssl.SSLError as e:
                if "timed out" in str(e).lower():
                    time.sleep(0.05)
                    continue
                self.close()
                raise
            except Exception:
                self.close()
                raise
        data, self._recv_buf = self._recv_buf[:n], self._recv_buf[n:]
        return data

    def recv(self):
        try:
            b0, b1 = self._recv_exact(2)
            opcode = b0 & 0x0F
            length = b1 & 0x7F
            if length == 126:
                length = struct.unpack(">H", self._recv_exact(2))[0]
            elif length == 127:
                length = struct.unpack(">Q", self._recv_exact(8))[0]
            payload = self._recv_exact(length) if length else b""
            if opcode == 0x8:
                if len(payload) >= 2:
                    code = struct.unpack(">H", payload[:2])[0]
                    text = payload[2:].decode("utf-8", "replace")
                    self.close_reason = f"{code} {text}".strip()
                self.closed = True
                return None, None
            return opcode, payload
        except Exception as e:
            self.close_reason = self.close_reason or f"recv error: {e}"
            self.closed = True
            return None, None

    def close(self):
        if self.closed:
            return
        try:
            self._send_frame(0x8, b"")
        except Exception:
            pass
        self.closed = True
        try:
            if self.sock: self.sock.close()
        except Exception:
            pass


# Microphone capture (Windows MCI / waveIn API)

class _WAVEFORMATEX(ctypes.Structure):
    _fields_ = [
        ("wFormatTag", ctypes.c_ushort),
        ("nChannels", ctypes.c_ushort),
        ("nSamplesPerSec", ctypes.c_uint),
        ("nAvgBytesPerSec", ctypes.c_uint),
        ("nBlockAlign", ctypes.c_ushort),
        ("wBitsPerSample", ctypes.c_ushort),
        ("cbSize", ctypes.c_ushort),
    ]


class _WAVEHDR(ctypes.Structure):
    pass


_WAVEHDR._fields_ = [
    ("lpData", ctypes.c_char_p),
    ("dwBufferLength", ctypes.c_uint),
    ("dwBytesRecorded", ctypes.c_uint),
    ("dwUser", ctypes.c_void_p),
    ("dwFlags", ctypes.c_uint),
    ("dwLoops", ctypes.c_uint),
    ("lpNext", ctypes.POINTER(_WAVEHDR)),
    ("reserved", ctypes.c_void_p),
]


class _MicCapture:
    _CALLBACK_NULL = 0x00000000
    _WHDR_DONE = 0x00000001

    def __init__(self, on_data, sample_rate=16000, block_ms=100):
        self.on_data = on_data
        self.sample_rate = sample_rate
        self.block_size = int(sample_rate * 2 * block_ms / 1000)
        self.hwi = None
        self._running = False
        self._thread = None
        self._buffers = []

    def start(self):
        winmm = ctypes.windll.winmm
        fmt = _WAVEFORMATEX(
            wFormatTag=1,
            nChannels=1,
            nSamplesPerSec=self.sample_rate,
            nAvgBytesPerSec=self.sample_rate * 2,
            nBlockAlign=2,
            wBitsPerSample=16,
            cbSize=0,
        )
        self.hwi = ctypes.c_void_p()
        res = winmm.waveInOpen(ctypes.byref(self.hwi), 0xFFFFFFFF, ctypes.byref(fmt), 0, 0, self._CALLBACK_NULL)
        if res != 0:
            raise OSError(f"waveInOpen failed: {res}")
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _make_header(self):
        buf = ctypes.create_string_buffer(self.block_size)
        hdr = _WAVEHDR()
        hdr.lpData = ctypes.cast(buf, ctypes.c_char_p)
        hdr.dwBufferLength = self.block_size
        hdr.dwFlags = 0
        return buf, hdr

    def _loop(self):
        winmm = ctypes.windll.winmm
        hdr_size = ctypes.sizeof(_WAVEHDR)
        headers = [self._make_header() for _i in range(4)]
        for buf, hdr in headers:
            winmm.waveInPrepareHeader(self.hwi, ctypes.byref(hdr), hdr_size)
            winmm.waveInAddBuffer(self.hwi, ctypes.byref(hdr), hdr_size)
        winmm.waveInStart(self.hwi)
        try:
            while self._running:
                progressed = False
                for buf, hdr in headers:
                    if hdr.dwFlags & self._WHDR_DONE:
                        recorded = hdr.dwBytesRecorded
                        if recorded and self.on_data:
                            try: self.on_data(buf.raw[:recorded])
                            except Exception: pass
                        winmm.waveInUnprepareHeader(self.hwi, ctypes.byref(hdr), hdr_size)
                        hdr.dwFlags = 0
                        hdr.dwBytesRecorded = 0
                        winmm.waveInPrepareHeader(self.hwi, ctypes.byref(hdr), hdr_size)
                        winmm.waveInAddBuffer(self.hwi, ctypes.byref(hdr), hdr_size)
                        progressed = True
                if not progressed:
                    time.sleep(0.05)
        finally:
            try: winmm.waveInStop(self.hwi)
            except Exception: pass
            for buf, hdr in headers:
                try: winmm.waveInUnprepareHeader(self.hwi, ctypes.byref(hdr), hdr_size)
                except Exception: pass

    def stop(self):
        self._running = False
        if self.hwi:
            try: ctypes.windll.winmm.waveInReset(self.hwi)
            except Exception: pass
        if self._thread:
            self._thread.join(timeout=2)
        if self.hwi:
            try: ctypes.windll.winmm.waveInClose(self.hwi)
            except Exception: pass
            self.hwi = None


# Live voice session (Gemini Live API)

class LiveSession:
    HOST = vision_config.DEFAULT_API_URLS["gemini"].replace("https://", "")

    def __init__(self, on_text, on_status, on_closed, on_stream=None):
        self.on_text = on_text
        self.on_status = on_status
        self.on_closed = on_closed
        self.on_stream = on_stream
        self.ws = None
        self.mic = None
        self.player = None
        self._running = False
        self._recv_thread = None
        self._stream_speaker = None
        self._interrupted = False
        self._player_lock = threading.Lock()

    def _get_player(self):
        with self._player_lock:
            if self._interrupted:
                return None
            if self.player is None:
                try:
                    device = ""
                    try:
                        device = config.conf["audio"]["outputDevice"]
                    except (KeyError, IndexError):
                        try:
                            device = config.conf["speech"]["outputDevice"]
                        except (KeyError, IndexError):
                            pass
                    self.player = nvwave.WavePlayer(channels=1, samplesPerSec=24000, bitsPerSample=16, outputDevice=device)
                except Exception as e:
                    log.warning(f"Live: WavePlayer with configured device failed ({e}); using default device.")
                    self.player = nvwave.WavePlayer(channels=1, samplesPerSec=24000, bitsPerSample=16)
            return self.player

    def _stop_player(self):
        with self._player_lock:
            self._interrupted = True
            if self.player:
                try:
                    self.player.stop()
                    self.player.close()
                except Exception: pass
                self.player = None

    def _resolve_model(self):
        conf = config.conf["VisionAssistant"]
        default_live = "gemini-3.1-flash-live-preview"
        provider = conf["active_provider"]
        model = ""
        if conf.get("advanced_model_routing", False):
            model = conf.get(f"{provider}_live_model", "").strip()
        if not model:
            model = conf.get("live_model", default_live).strip()
        if not model:
            model = default_live
        if "live" not in model.lower():
            log.warning(f"Live: selected model '{model}' is not a Live model; using '{default_live}'.")
            model = default_live
        return model

    def _resolve_target(self):
        from ..ai.core import AIHandler
        try:
            base = AIHandler.get_base_url(config.conf["VisionAssistant"]["active_provider"])
            parsed = urlparse(base)
            if parsed.hostname:
                port = parsed.port or (443 if parsed.scheme == "https" else 80)
                is_ssl = (parsed.scheme == "https")
                return parsed.hostname, port, is_ssl
        except Exception:
            pass
        return self.HOST, 443, True

    def start(self):
        from ..ai.core import AIHandler
        from ..ai.providers.gemini import GeminiHandler
        from ..prompt_utils import get_prompt_text, apply_prompt_template
        from ..vision_config import get_lang_name

        keys = AIHandler.get_keys(config.conf["VisionAssistant"]["active_provider"])
        if not keys:
            # Translators: Error message when TTS is not supported by the provider
            self.on_status("ERROR:" + _("No API Keys configured."))
            return False
        model = self._resolve_model()
        voice = ""
        thinking_level = ""
        plugin = plugin_state.plugin_instance
        if plugin and getattr(plugin, "live_dlg", None) and plugin.live_dlg:
            try:
                dlg = plugin.live_dlg
                if hasattr(dlg, "voice_sel") and dlg.voice_sel:
                    sel = dlg.voice_sel.GetSelection()
                    if sel != wx.NOT_FOUND:
                        voice = vision_config.GEMINI_VOICES[sel][0]
                if hasattr(dlg, "thinking_sel") and dlg.thinking_sel:
                    t_sel = dlg.thinking_sel.GetSelection()
                    if t_sel != wx.NOT_FOUND:
                        thinking_level = dlg.thinking_choices[t_sel][1]
            except Exception:
                pass
        if not voice:
            voice = config.conf["VisionAssistant"].get("tts_voice", "Puck").strip() or "Puck"
        if not thinking_level:
            thinking_level = config.conf["VisionAssistant"].get("live_thinking_level", "medium").strip() or "medium"
        host, port, is_ssl = self._resolve_target()

        self.ws = None
        num_keys = len(keys)
        start_idx = getattr(GeminiHandler, '_working_key_idx', 0)

        last_error = None
        for i in range(num_keys):
            idx = (start_idx + i) % num_keys
            api_key = keys[idx]
            path = f"/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={api_key}"

            max_retries = getattr(GeminiHandler, '_max_retries', 3)
            attempt = 0
            while attempt < max_retries:
                try:
                    ws_candidate = _MinimalWebSocket(host, path, port=port, is_ssl=is_ssl)
                    ws_candidate.connect()
                    self.ws = ws_candidate
                    GeminiHandler._working_key_idx = idx
                    break
                except Exception as e:
                    last_error = str(e)
                    err_str = last_error.lower()
                    is_retryable = False
                    delay = 1.0 * (attempt + 1)

                    if "500" in err_str or "502" in err_str or "503" in err_str or "504" in err_str:
                        is_retryable = True
                    elif "429" in err_str or "high demand" in err_str or "exhausted" in err_str or "quota" in err_str:
                        if any(x in err_str for x in ["daily", "per day", "per_day", "perday", "requestsperday"]):
                            is_retryable = False
                        else:
                            is_retryable = True
                            if "high demand" in err_str:
                                max_retries = max(max_retries, 10)
                            else:
                                max_retries = max(max_retries, 5)

                    if is_retryable and ("429" in err_str or "quota" in err_str or "exhausted" in err_str):
                        match = re.search(r"retry in ([\d\.]+)s", err_str)
                        if match:
                            try:
                                delay = float(match.group(1)) + 0.5
                            except Exception: pass

                    if not is_retryable:
                        log.error(f"LiveSession: WebSocket connection failed (Key {idx}): {e}")
                        if "403" in err_str or "401" in err_str or "forbidden" in err_str or "unauthorized" in err_str:
                            break
                        break

                    if attempt < max_retries - 1:
                        log.warning(f"LiveSession: Retryable error (Key {idx}, Attempt {attempt+1}/{max_retries}). Retrying in {delay}s...")
                        time.sleep(delay)
                        attempt += 1
                        continue
                    else:
                        break
            if self.ws:
                break

        if not self.ws:
            err_str = last_error if last_error else "Unknown error"
            
            if "403" in err_str or "forbidden" in err_str.lower():
                # Translators: Error message displayed when access to the Live voice service is blocked or forbidden (HTTP 403 Forbidden).
                err_msg = _("Access denied (HTTP 403 Forbidden). Please check your Proxy/VPN or API key.")
            else:
                if "b'HTTP" in err_str:
                    try:
                        status_part = err_str.split("HTTP/1.1 ")[1].split("\\r")[0]
                        err_str = f"HTTP {status_part}"
                    except Exception:
                        pass
                # Translators: Error message announced when connecting to the Live service fails. {error} is replaced with the technical connection error details.
                err_msg = _("Could not connect to the Live service: {error}").format(error=err_str)
                
            self.on_status("ERROR:" + err_msg)
            return False

        lang = get_lang_name("ai_response_language")
        self.response_lang = lang
        live_instruction = apply_prompt_template(
            get_prompt_text("live_assistant_system"), [("response_lang", lang)]
        )
        setup = {
            "setup": {
                "model": f"models/{model}",
                "generationConfig": {
                    "responseModalities": ["AUDIO"],
                    "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
                    "thinkingConfig": {
                        "thinkingLevel": thinking_level
                    }
                },
                "realtimeInputConfig": {
                    "automaticActivityDetection": {
                        "disabled": False
                    }
                },
                "systemInstruction": {"parts": [{"text": live_instruction}]},
                "outputAudioTranscription": {},
                "inputAudioTranscription": {},
            }
        }
        try:
            self.ws.send_text(json.dumps(setup))
        except Exception as e:
            log.error(f"Live: Failed to send setup payload: {e}")
            self.stop()
            return False

        self._running = True
        self._recv_thread = threading.Thread(target=self._recv_loop, daemon=True)
        self._recv_thread.start()
        try:
            self.mic = _MicCapture(self._on_mic_data, block_ms=100)
            self.mic.start()
        except Exception as e:
            log.error(f"Mic capture failed: {e}", exc_info=True)
            # Translators: Error shown when the microphone cannot be opened for the live session.
            self.on_status("ERROR:" + _("Could not open the microphone."))
            self.stop()
            return False
        return True

    def _on_mic_data(self, pcm_bytes):
        if not self._running or not self.ws or self.ws.closed:
            return

        try:
            samples = array.array('h', pcm_bytes)
            peak = max(abs(s) for s in samples)
            if peak > 12000:
                if self.player is not None:
                    self._stop_player()
                    try:
                        cancel_msg = {"clientContent": {"turnComplete": True}}
                        self.ws.send_text(json.dumps(cancel_msg))
                    except Exception: pass
        except Exception: pass

        msg = {
            "realtimeInput": {
                "audio": {
                    "mimeType": "audio/pcm;rate=16000",
                    "data": base64.b64encode(pcm_bytes).decode()
                }
            }
        }
        try:
            self.ws.send_text(json.dumps(msg))
        except Exception: pass

    def send_video_frame(self, jpeg_b64):
        if not self._running or not self.ws or self.ws.closed or not jpeg_b64:
            return
        msg = {
            "realtimeInput": {
                "video": {
                    "mimeType": "image/jpeg",
                    "data": jpeg_b64
                }
            }
        }
        try:
            self.ws.send_text(json.dumps(msg))
        except Exception: pass

    def _recv_loop(self):
        while self._running:
            opcode, payload = self.ws.recv()
            if opcode is None:
                if self._running:
                    reason = self.ws.close_reason

                    # Translators: Line shown when the live server unexpectedly closes the connection. {reason} is the server's reason.
                    self.on_text(_("[Connection closed: {reason}]").format(reason=reason or _("unknown")))
                break
            if opcode == 0x9:
                try: self.ws._send_frame(0xA, payload or b"")
                except Exception: pass
                continue
            if opcode != 0x1 and opcode != 0x2:
                continue
            try:
                data = json.loads(payload.decode("utf-8", "replace"))
                self._handle_message(data)
            except Exception as e:
                log.error(f"Live: Failed to decode received payload: {e}")
        if self._running:
            self.stop()

    def _handle_message(self, data):
        if "setupComplete" in data:
            # Translators: Message announced by NVDA when the live voice conversation starts.
            self.on_status("STATUS:" + _("Live conversation started. You can speak now."))
            lang = getattr(self, "response_lang", "English")
            trigger_prompt = (
                f"Please greet the user warmly, introduce yourself exactly as 'Vision Assistant Pro' (DO NOT translate this name, keep it in English), "
                f"and ask how you can help them today. Speak strictly in {lang}."
            )

            msg = {
                "clientContent": {
                    "turns": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": trigger_prompt
                                }
                            ]
                        }
                    ],
                    "turnComplete": True
                }
            }
            try:
                self.ws.send_text(json.dumps(msg))
            except Exception as e:
                log.error(f"Live: Failed to send dynamic welcome trigger: {e}")
            return
        if "error" in data:
            err = data.get("error", {})
            err_msg = err.get("message") if isinstance(err, dict) else str(err)
            log.error(f"Live: Server returned error: {err_msg}")
            self.on_status("ERROR:" + str(err_msg))
            return

        server_content = data.get("serverContent")
        if not server_content:
            return

        if server_content.get("interrupted"):
            self._stop_player()
            self._end_stream_line()

        if "inputTranscription" in server_content or "input_transcription" in server_content:
            self._interrupted = False
            in_tx = server_content.get("inputTranscription") or server_content.get("input_transcription") or {}
            if in_tx.get("text"):
                # Translators: Prefix for the user's transcribed speech line in the Live Assistant history.
                self._stream("user", _("You: "), in_tx["text"])

        out_tx = server_content.get("outputTranscription") or server_content.get("output_transcription")
        if out_tx and out_tx.get("text"):
            self._stream("ai", _("AI: "), out_tx["text"])

        model_turn = server_content.get("modelTurn") or server_content.get("model_turn") or {}
        for part in model_turn.get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                if not self._interrupted:
                    try:
                        p = self._get_player()
                        if p:
                            p.feed(base64.b64decode(inline["data"]))
                    except Exception as e:
                        log.error(f"Live playback failed: {e}")
            text = part.get("text")
            if text:
                # Translators: Prefix for an AI message line in the Live Assistant history.
                self._stream("ai", _("AI: "), text)

        if server_content.get("turnComplete") or server_content.get("turn_complete"):
            self._interrupted = False
            self._end_stream_line()

    def _stream(self, speaker, prefix, text):
        if self._stream_speaker != speaker:
            if self._stream_speaker is not None and self.on_stream:
                self.on_stream("\n")
            if self.on_stream:
                self.on_stream(prefix)
            self._stream_speaker = speaker
        if self.on_stream:
            self.on_stream(text)

    def _end_stream_line(self):
        if self._stream_speaker is not None and self.on_stream:
            self.on_stream("\n")
        self._stream_speaker = None

    def stop(self):
        if not self._running and self.ws is None:
            return
        self._running = False
        if self.mic:
            try: self.mic.stop()
            except Exception: pass
            self.mic = None
        if self.ws:
            try: self.ws.close()
            except Exception: pass
            self.ws = None
        self._stop_player()
        if self.on_closed:
            try: self.on_closed()
            except Exception: pass