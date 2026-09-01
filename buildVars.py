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
    addon_version="2026.09.02",
    # Brief changelog for this version
    # Translators: what's new content for the add-on version to be shown in the add-on store
    addon_changelog=_("""## Changes for 2026.09.01

*   **History (Control + H)**: The Command Layer now includes a **History** dialog (`Control + H`) that lists your past chats and documents with filters for All, Chats, and Documents. Reopen any chat with its full conversation — attached files are re-attached automatically — or reopen a document and keep reading. Press **Delete** on any item to remove it, or clear everything at once.
*   **Recent Documents in the Reader**: Pressing **D** in the Command Layer now shows your recently read documents first. Pick one to continue from the page you were on — even when the OCR already finished — or press **Open File...** (`Ctrl + O`) to browse as usual.
*   **Push to Talk for Live Assistant**: Take full control of your live conversations! Enable **Push to Talk** in the new Live Assistant settings tab and assign any key — or even a lone modifier like `Left Ctrl` — to talk. Hold the key to speak and release it when you're done, with a short beep on each press and release. A matching toggle also appears right in the Live Assistant window, so you can switch between push-to-talk and open-mic mode without leaving the conversation.
*   **Gemini 2.5 Flash Native Audio**: The Live Assistant now supports Gemini 2.5 Flash's native audio model (`gemini-2.5-flash-native-audio-preview-12-2025`) for low-latency, natural voice conversations. You can switch to it from **Settings → Advanced Model Routing → Live Assistant Model (Gemini only)**, or keep "Auto" to stay on the recommended model.
*   **Settings Backup & Restore**: Added a powerful backup and restore system in the **Advanced** tab! You can now save all of your add-on settings — including API keys, models, custom prompts, and preferences — into a single JSON file, and restore them perfectly at any time, on any machine, or after reinstalling NVDA. When backing up, you choose what to include: **Everything** (settings, custom labels, OCR progress, and history) or **Settings Only**.
*   **Direct Text & HTML Reading**: The Document Reader can now open plain text (`.txt`) and HTML (`.html`, `.htm`) files directly! It automatically detects the file encoding, strips scripts and formatting clutter, and intelligently splits the content into readable pages — even re-importing its own exported files while preserving page structure — so you can read them instantly with no OCR or AI processing!
*   **Gemini Live TTS for the Document Reader**: The "Generate Audio" button now supports Gemini Live — a high-quality, natural-pace streaming text-to-speech engine! When Gemini is your active provider, you can choose between Standard TTS and Gemini Live right in the reader, and your selection is remembered for next time!
*   **Custom Prompt Shortcuts**: You can now assign a shortcut key to any of your custom prompts right from the Prompt Manager! Give every prompt its own dedicated key or key combination to run it instantly, automatically capturing your current selection or context with zero extra steps!
*   **Chat Message Navigation**: Review any conversation hands-free! Inside any chat window (Direct Chat, document chat, refine, and more), press `Alt + Down` to hear the next message and `Alt + Up` to hear the previous one — with clear "You" / "AI" prefixes and "First message" / "Last message" boundaries announced as you go.
*   **Copy Chat Message (Alt + C)**: While reviewing a conversation with `Alt + Up/Down`, press `Alt + C` to copy the message you are currently on to the clipboard — respecting your Clean Markdown setting — with a spoken confirmation.
*   **Direct Chat System Prompt**: The Direct Chat (`Shift+C`) now has its own editable system prompt — "Direct Chat Instruction" — that sets the assistant's persona and response language for every conversation. You can customize it from the Prompt Manager's Default Prompts tab.
*   **Document Reader Cursor Page Navigation**: Reading multi-page documents just got smoother! In the Document Viewer, when your cursor reaches the last line of a page and you press `Down`, the reader automatically jumps to the next page. Pressing `Up` at the start of a page seamlessly takes you back to the previous one — no more manual page switching while reading!
*   **New Quick Settings Toggles**: Copy AI responses to clipboard, Direct Output (no chat window), Clean Markdown in Chat, and Smart Swap can now be switched on and off instantly from the command layer's Quick Settings!
*   **Live Assistant Settings Tab**: The Live Assistant now has its own dedicated settings tab! The "Live Assistant: Direct Output (No Window)" option moved here from the Connection tab, and the tab appears only when Google Gemini (or a Gemini-compatible Custom provider) is your active provider.
"""),
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