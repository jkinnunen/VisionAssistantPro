# -*- coding: UTF-8 -*-
from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
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
- Check Update (U)
- Recall Last Result (Space)
- Commands Help (H)
- Open Settings (Alt+S)
- Report Quota Exhausted Keys (Alt+Q)
- Report Advanced Routing (Alt+M)
- Quick Settings (Up/Down/Left/Right)"""),
    addon_version="2026.08.06",
    # Brief changelog for this version
    # Translators: what's new content for the add-on version to be shown in the add-on store
    addon_changelog=_("""## Changes for 2026.08.06

*   **UI Explorer Labeling**: You can now add labels directly to found elements inside the UI Explorer! A new "Add Label" button has been added, and the interface smartly stays open and preserves focus so you can rapidly label multiple objects without interruption.
*   **Quick Settings Layer Enhancement**: The Vision Assistant layer (`Insert+Shift+V`) is now persistent and highly interactive! You can use `Up/Down` arrows to navigate between quick settings (Provider, Model, AI Response Language, TTS Model) and `Left/Right` arrows to instantly change their values with smart, concise voice feedback. Your selections take effect immediately (including auto-enabling advanced routing when necessary), and the layer stays alive while you configure.
*   **Direct Chat (`Shift+C`)**: Added a new command to the layer! Press `Shift+C` to instantly open a "Direct Chat" window. This provides a clean, text-based conversational interface with the AI right away, without needing an image or document as a starting point.
*   **Flawless Chat History Recall**: Fixed a major bug where pressing `Space` to recall the last result would lose your subsequent chat history. Now, the add-on globally tracks your conversation. If you chat, close the dialog, and press `Space` to recall it, your entire back-and-forth history is perfectly restored! Works for Direct Chat, Vision Analysis, Document Chat, and Translation.
*   **Inline Image Descriptions in OCR**: Added an optional feature to describe images inline during document OCR. You can toggle this setting in the add-on's OCR settings, within the Document Reader options before extraction, and quickly on-the-fly via the Quick Settings layer.
*   **Voice Translation (`Control+T`)**: Added a powerful new feature! Dictate speech and instantly translate and type it using AI based on your configured source and target languages.
*   **Update Downloader Improvements**: The update download dialog now correctly displays download progress in percentages, and a bug where a phantom "Downloading update" message appeared upon canceling the installation has been fixed.
*   **eSpeak-NG Downloader Improvements**: Added percentage progress tracking for eSpeak-NG downloads.
*   **Batch OCR Resilience**: Fixed an issue in batch PDF OCR where the process would halt if the active API key reached its quota midway; it now automatically switches to the next available key and resumes the process.
*   **Visual Captcha Support**: Added robust support for visual captcha solving. It attempts to automatically solve complex image challenges like hCaptcha and reCAPTCHA, significantly enhancing accessibility on challenging web forms.
*   **Audio Transcriber Overhaul**: The Audio Transcriber module has been completely rebuilt and now supports both audio and video files. It features 3 distinct operation modes: "Transcribe (Original Language)", "Transcribe and Translate (Target Language)", and a new powerful "Dub and Translate (Target Language)" option (exclusive to Gemini) that generates a translated audio dub of the original speech.
*   **Optional Page Numbers in Document Reader**: Added a new setting to toggle the inclusion of page numbers and separators in multi-page document outputs. You can easily manage this option from the main settings or toggle it on-the-fly via the Quick Settings layer. This feature applies to both text/HTML file exports and the inline "View Formatted" window, allowing you to read combined documents seamlessly.
*   **Unlimited Gemini Live TTS for Video Descriptions**: You can now select "Gemini Live TTS" as the voice engine when generating Synchronized Audio Narration (MP3) for videos. This utilizes the Gemini Live API to synthesize high-quality audio descriptions without any character limits or length restrictions.
*   **Codebase Modularization**: Refactored the add-on structure from a single file to a multi-file modular architecture for improved maintainability.
*   **Settings UI Redesign**: Completely redesigned the Settings dialog to use a modern, tab-based interface instead of a grouped layout, providing better organization and easier navigation while keeping all existing options.
*   **Global & Dedicated File Logging**: Added an optional global file logging system under the new "Advanced" settings tab. Automatically captures operational events, API traffic, and errors across all add-on modules into a dedicated file (`vision_assistant.log`). Supports configurable log verbosity levels (Debug, Info, Warning, Error), automated retention periods (1 hour to 90 days), and direct log opening or clearing from settings with zero performance impact or NVDA log interference.
*   **Gemini Upload Progress Tracking**: Added real-time percentage progress announcements when uploading large files (video, audio, documents) to the Google Gemini API."""),
    addon_author="Mahmood Hozhabri",
    addon_url="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_sourceURL="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2025.1",
    addon_lastTestedNVDAVersion="2026.1",
    addon_updateChannel=None,
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