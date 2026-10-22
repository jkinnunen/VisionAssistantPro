# -*- coding: UTF-8 -*-
from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
    addon_name="VisionAssistant",
    # Add-on summary/title, usually the user visible name of the add-on
    # Translators: Summary/title for this add-on
    # to be shown on installation and add-on information found in add-on store
    addon_summary=_("Vision Assistant Pro"),
# Add-on description
    # Translators: Long description to be shown for this add-on on add-on information from add-on store
    addon_description=_("""An advanced AI assistant for NVDA using Gemini models.
Command Layer: Press NVDA+Shift+V, then:
- Smart Translator (T) / Clipboard (Shift+T)
- Text Refiner (R)
- Describe Object (V) / Full Screen (O)
- Video Analysis (Shift+V)
- Local Video Recording (Control+V)
- Document Reader (D)
- File OCR (F)
- CAPTCHA Solver (C)
- Direct Chat (Shift+C)
- Media Transcription & Dubbing (M)
- Smart Dictation (S)
        - Voice Translation (Control+T)
- Announce Status (I)
- Label Object (L)
- Manage/Scan Labels (Shift+L)
- UI Explorer (E)
- AI Operator (Shift+A)
- Live Assistant (Control+L) / Live Operator (Control+A)
- Gemini API Key Manager (G)
- Check Update (U)
- Recall Last Result (Space)
- Commands Help (H)
- Open Settings (Alt+S)
- Report Quota Exhausted Keys (Alt+Q)
- Report Advanced Routing (Alt+M)
- Quick Settings (Up/Down/Left/Right)"""),
    addon_version="2026.10.22",
    # Brief changelog for this version
    # Translators: what's new content for the add-on version to be shown in the add-on store
    addon_changelog=_("""## Changes for 2026.10.22

*   **Instagram Video Downloader Fix**: Restored video analysis and audio transcription for Instagram Reels and posts by switching to direct embed media parsing, bypassing third-party scraper failures.
*   **TikTok Video Downloader Fix**: Enhanced API request handling and fallback parsing for more reliable TikTok video link retrieval.
*   **Service Cleanup**: Removed Twitter/X video download support due to upstream platform access restrictions."""),

    addon_author="Mahmood Hozhabri",
    addon_url="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_sourceURL="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2025.1",
    addon_lastTestedNVDAVersion="2026.3",
    addon_updateChannel="beta",
    addon_license="GPL-2.0",
    addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

pythonSources: list[str] = [
    "addon/globalPlugins/visionAssistant/*.py",
    "addon/globalPlugins/visionAssistant/ai/*.py",
    "addon/globalPlugins/visionAssistant/ai/providers/*.py",
    "addon/globalPlugins/visionAssistant/dialogs/*.py",
    "addon/globalPlugins/visionAssistant/features/*.py",
    "addon/globalPlugins/visionAssistant/utils/*.py",
]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = [
    "markdown.extensions.tables",
    "markdown.extensions.toc",
    "markdown.extensions.nl2br",
    "markdown.extensions.extra",
]

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
speechDictionaries: SpeechDictionaries = {}
