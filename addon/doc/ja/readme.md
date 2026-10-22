# Vision Assistant Pro ドキュメント

<!-- DOWNLOAD_COUNT_START --> 合計ダウンロード数: 75,681 <!-- DOWNLOAD_COUNT_END -->

**Vision Assistant Pro** は、NVDA向けの高機能かつマルチモーダルなAIアシスタントです。世界最高水準のAIエンジンを活用し、インテリジェントな画面読み上げ、翻訳、音声ディクテーション、およびドキュメント分析を提供します。 It leverages world-class AI engines to provide intelligent screen reading, translation, voice dictation, and document analysis.

_このアドオンは、国際障害者デーを記念してコミュニティに公開されました。_

## 1. セットアップと設定

Go to **NVDA Menu > Preferences > Settings > Vision Assistant Pro**. The settings dialog is organized into 9 accessible tabs: **Connection**, **Live Assistant**, **AI Behavior**, **Translation Languages**, **Document Reader**, **Video**, **CAPTCHA**, **Prompts**, and **Advanced**.

### 1.1 接続 (Connection) タブ

- **Provider:** Select your preferred AI service. **プロバイダー (Provider):** お好みの AI サービスを選択します。サポートされているプロバイダーには、**Google Gemini**、**OpenAI**、**Mistral**、**Groq**、**MiniMax**、および**カスタム (Custom)**（Ollama、LM Studio、Jan.ai、KoboldCPP などの OpenAI 互換サーバー）が含まれます。
- **API キー (API Key):** 自動ローテーション用に、単一または複数の API キー（カンマまたは改行区切り）を入力します。
- **モデルを取得 (Fetch Models):** API キーを入力した後にこのボタンを押すと、プロバイダーから利用可能な最新のモデルリストをダウンロードできます。
- **AI モデル (AI Model):** 一般的なチャットや分析に使用するメインモデルを選択します。
- **高度なモデル ルーティング**: ネイティブプロバイダー（Gemini、OpenAI など）のユーザーは、さまざまなタスク（OCR、STT、TTS）に合わせて、ドロップダウンリストから特定のモデルを選択できるようになりました。 For Gemini, models are dynamically categorized by capability without clutter.
- **Custom Provider Settings:** Configure local or custom endpoints. **カスタムプロバイダー設定 (Custom Provider Settings):** ローカルまたはカスタムのエンドポイントを設定します。**ローカル AI のセットアップ (Setup Local AI)**（Ollama、LM Studio、Jan.ai、KoboldCPP のワンクリックセットアップ）と\*\*高度なエンドポイント設定 (Advanced Endpoint Configuration)\*\*が含まれます。
- **プロキシ設定 (Proxy Configuration):** アドオン全体（ライブアシスタント、アンビエントオブザーバー、TTS を含む）にわたる、トンネリングとエンドポイントリダイレクトの完全なサポート。**プロキシ URL (Proxy URL)** を入力し、**プロキシモード (Proxy Mode)** を選択します。 Enter your **Proxy URL** and select your **Proxy Mode**:
  - **自動検出 (Auto-detect):** URL がフォワードプロキシかリバースプロキシかを自動的に検出します。
  - **SOCKS5 プロキシ (SOCKS5 Proxy):** RFC 1929 ユーザー名/パスワード認証およびドメイン名解決を使用した、SOCKS5 経由のフォワードトンネリングを強制します。
  - **HTTP プロキシ (HTTP Proxy):** Basic 認証を使用した HTTP プロキシ経由のフォワードトンネリングを強制します。
  - **リバースプロキシ (Reverse Proxy):** カスタム AI ゲートウェイおよびセルフホストミラー向けの直接エンドポイント置換（このモードでは資格が無効になります）。
- **プロキシ接続テスト (Test Proxy Connection):** 接続性をテストし、サーバーのレイテンシをミリ秒単位で測定する非ブロッキングボタンです（NVDA を通じて読み上げられます）。
- **接続と出力のオプション (Connection & Output Options):** 起動時のアップデート確認、チャット内のクリーンなマークダウン、AI 応答のクリップボードへのコピー、直接出力（チャットウィンドウなし）を設定します。
- **チャットを履歴に保存 (Save Chats to History):** チャットの会話を履歴リストに保持します。

### 1.2 ライブアシスタント (Live Assistant) タブ

- **ライブアシスタント：直接出力（ウィンドウなし） (Live Assistant: Direct Output (No Window)):** 会話ウィンドウなしでライブアシスタントを開始します。後で「最後の結果を呼び出し (`Space`)」キーで開きます。
- **プッシュトトーク (Push to Talk):** プッシュトトークモードの切り替え。有効にすると、割り当てられたキーを押している間だけマイクが音声を送信します。 When enabled, your microphone only sends audio while you hold the assigned key.
- **プッシュトトークキー (Push to Talk Key):** ショートカットを記録するキーを押します（例: `F12` や `Ctrl+F12`）。`左 Ctrl` のような単独の修飾キーを割り当てることもできます。キーを押したまま話すと、離したときに終了します。短いビープ音が押下と解放を確認させます。 Hold the key to speak and release it to finish; a short beep confirms each press and release.

注: このタブは、**Google Gemini**（または Gemini 互換のカスタムプロバイダー）がアクティブなプロバイダーである場合にのみ表示されます。

### 1.3 AI の動作 (AI Behavior) タブ

- **創造性（温度） (Creativity (Temperature)):** AI のランダム性と創造性を制御します（0.0 から 2.0 まで）。値を低くすると、より決定的で正確な翻訳および OCR 結果が得られます。 Lower values produce more deterministic and accurate translation/OCR results.

### 1.4 翻訳言語 (Translation Languages) タブ

- **ソース言語 (Source Language):** デフォルトの入力言語を選択します。
- **ターゲット言語 (Target Language):** プライマリの翻訳ターゲット言語を選択します。
- **AI 応答言語 (AI Response Language):** 一般的な AI 応答の言語を選択します。
- **スマートスワップ (Smart Swap):** 検出された入力に基づいて、ソース言語とターゲット言語を自動的に入れ替えます。

### 1.5 文書リーダー (Document Reader) タブ

- **OCR エンジン (OCR Engine):** 高速な結果が得られる **Chrome (高速) (Chrome (Fast))** か、優れたレイアウト保持力を誇る **AI (高度) (AI (Advanced))** から選択します。
- **OCR バッチサイズ (OCR Batch Size):** リクエストあたりのページ数を指定します（単一リクエスト処理の場合は 0 に設定）。
- **画像をインラインで説明 (Describe Images Inline):** 文書テキスト抽出中のインライン画像説明の切り替え。
- **ページ番号のエクスポート (Export Page Numbers):** 複数ページの文書出力におけるページ番号と区切り文字の切り替え。
- **TTS 音声 (TTS Voice):** 音声生成のデフォルトの音声スタイルを選択します。
- **文書を履歴に保存 (Save Documents to History):** 開いた文書を履歴リストに保持します。キャッシュされた OCR テキストと再開データは引き続き保存されます。

### 1.6 ビデオ (Video) タブ

- **ビデオチャンクサイズ (Video Chunk Size):** オーディオ解説生成のためのセグメント長（分単位、ファイル全体を処理する場合は 0 に設定）。
- **キャラクターリストを追加 (Add Character List):** 最初の子タイトルエントリとしてキャラクター辞書を追加するオプション。
- **AI 免責事項を追加 (Add AI Disclaimer):** ビデオの SRT 字幕の先頭に AI の免責事項を挿入するオプション。
- **キャラクター辞書とシリーズ管理 (Character Dictionary & Series Management):** シリーズごとのキャラクター名、身体的特徴、役割の追加、編集、インポート、管理を行います。AI は発見されたキャラクターを辞書に自動的に照合し、エピソードを分析するにつれて新しいキャラクターを統合します。手動によるメモは常に AI の更新よりも優先して保持され、身体的特徴はエピソード間で最新の状態に保たれます。 Your manual notes are always preserved with priority over AI updates, while physical descriptions stay up-to-date across episodes.

### 1.7 CAPTCHA タブ

- **視覚的 CAPTCHA ソルバーを有効化 (Enable Visual CAPTCHA Solver):** 自動化された視覚的チャレンジの解決（hCaptcha、reCAPTCHA）の切り替え。
- **テキスト CAPTCHA メソッド (Text CAPTCHA Method):** **ナビゲーターオブジェクト (Navigator Object)** のキャプチャか**全画面 (Full Screen)** かを選択します。

### 1.8 プロンプト (Prompts) タブ

- **プロンプトの管理 (Manage Prompts):** デフォルトのシステムプロンプトをカスタマイズしたり、動的変数（`[selection]`、`[screen_fg_obj]`、`[currentURL]`、`[text]` など）を使用してカスタムユーザー定義プロンプトを作成、編集、並べ替え、プレビューしたりするための専用ダイアログを開きます。
- **Custom Prompt Shortcuts:** Assign a dedicated shortcut key to any custom prompt right in the Prompt Manager. **カスタムプロンプトのショートカット (Custom Prompt Shortcuts):** プロンプトマネージャー内で、任意のカスタムプロンプトに専用のショートカットキーを割り当てます。キーを押して記録します。単独のキーはコマンドレイヤー内で実行され（グローバルには `NVDA + Shift + キー` として機能）、`Control + Shift + 1` などの組み合わせはそれ単体でグローバルに実行されます。
- **プロンプトごとのフィードバック動作 (Per-Prompt Feedback Behavior):** 各プロンプトが結果を出力する方法を個別に選択します（グローバル設定、クリップボードにコピー、直接出力 / NVDA メッセージ、クリップボードにコピー + 直接出力、またはチャットウィンドウ）。

### 1.9 高度な設定とグローバルログ (Advanced Tab & Global Logging)

**高度な設定 (Advanced)** タブに移動して、グローバルのアドオンログを設定します。

- **専用ログファイルを有効にする (Enable dedicated log file):** すべてのアドオンモジュールにわたるすべての操作イベント、API トラフィック、エラーの個別のファイル（`vision_assistant.log`）へのログ記録を切り替えます。
- **ログレベル (Log Level):** 詳細度を **デバッグ（すべての詳細） (Debug (All Details))**、**情報（一般情報） (Info (General Information))**、**警告（警告のみ） (Warning (Warnings Only))**、**エラー（エラーのみ） (Error (Errors Only))** から選択します。
- **ログの保持期間 (Keep Logs For):** 古いログエントリを自動的にクリーンアップするための自動保持期間を設定します（1 時間から 90 日間）。
- **ログ管理コントロール (Log Management Controls):** **ログファイルを開く (Open Log File)**、**ログフォルダーを開く (Open Log Folder)**、または **ログファイルをクリア (Clear Log File)** を使用して、NVDA を再起動したり標準の NVDA ログに干渉したりすることなく、ログデータを直接確認またはクリアします。
- **統合データディレクトリ (Unified Data Directory):** すべてのアドオンデータファイル（履歴、シリーズ、ラベル、OCR の進捗状況、キャッシュ、ログ）は、NVDA 設定ディレクトリ内の単一の `VisionAssistant` フォルダーに保存されます。これによりすべてが整理され、手動でのバックアップが簡単になります。

### 1.10 設定のバックアップと復元 (Settings Backup & Restore)

**高度な設定 (Advanced)** タブには、**バックアップと復元 (Backup and Restore)** セクションも含まれています。

- **バックアップ (Backup):** 設定を単一の JSON ファイルに保存します。クリックすると、含める内容を選択できます：**すべて (Everything)**（設定、カスタムラベル、OCR の進捗状況、履歴）または**設定のみ (Settings Only)**。 When you click it, you choose what to include: **Everything** (settings, custom labels, OCR progress, and history) or **Settings Only**.
- **復元 (Restore):** 以前に保存したバックアップをロードして、いつでも、どのマシンの上でも、あるいは NVDA の再インストール後に、設定とデータを復元します。復元を行うと現在の設定とデータがすべて置き換わるため、最初に確認を求められます。 You will be asked to confirm first, since restoring replaces all of your current settings and data.

## 2. Gemini API Key Manager

**最も要望の多かった修正 — Gemini API キーの作成がようやく簡単に**: **aistudio.google.com** で API キーを取得することは、これまで最も困難な手順の1つでした。スクリーンリーダーを使用している場合、ページが分かりにくく、キーをまったく作成できないユーザーもいました。この問題が、アドオン内で直接解決されました。コマンドレイヤーで **G** を押す（または設定の **Gemini API キーを取得...** を使用する）と、外部でのセットアップなしでデフォルトのブラウザを通じてサインインでき、これまでにプロジェクトを作成したことがない場合でも、1回のエントリ確認でキーが作成および設定されます。 With a screen reader the pages were confusing, and some people simply could not create a key at all. The **Gemini API Key Manager** solves that problem. Press **G** in the Command Layer, or open **NVDA Menu > Preferences > Settings > Vision Assistant > Connection** and press **Get a Gemini API Key...**.

- **Signing in:** When you open the manager, your default browser opens directly with Google's secure sign-in page. Sign in with your Google account — no external tools, SDKs, or command-line setups are required. The account you are signed in with is always shown on the **Sign Out** button.
- **Creating a key:** After signing in, you can create a key immediately with **New Project and Key** without any prior setup. If you already have existing projects, they appear in a simple list where you can select one and press **Create Key for Selected Project**.
- **What happens next:** The new key is copied to the clipboard straight away, saved inside the add-on for later, and you are asked once whether to add it to the add-on's key list. That is all you need — no web pages to hunt through.
- **Working with your keys:** **Copy Key for Selected Project** copies the key of the project you have selected, **Copy Last Created Key** copies the key you created a moment ago, and **Export Saved Keys to CSV...** saves everything you have created to a file.
- **Deleting a key:** **Delete a Key...** shows the keys that exist on the selected project, asks you which one to remove, and confirms before deleting. Deleting a key also removes it from the add-on's key list, so no broken key is ever left in the rotation. Keys created outside the add-on can be deleted too, as long as your account has permission on that project.
- **Signing out:** **Sign Out** removes the stored sign-in information from your computer, so you can switch to another account whenever you like.

## 3. Command Layer & Shortcuts

To prevent keyboard conflicts, this add-on uses a **Command Layer**.

1. \*\*コマンドレイヤー:\*\* ショートカットを1つのマスターキーの下にまとめるコマンドレイヤーシステム（デフォルト: `NVDA+Shift+V`）を導入しました。たとえば、翻訳のために `NVDA+Control+Shift+T` を押す代わりに、まず `NVDA+Shift+V` を押し、その後に `T` を押すようになります。
2. Release keys, then press one of the following single keys:

| Key              | Function                                          | Description                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift + A**    | **AI Operator**                                   | **Autonomous Operation:** Tell the AI to perform a task on your screen. Pressing it again instantly aborts active operations.                                                                                     |
| **E**            | **UI Explorer**                                   | **Interactive Click:** Identifies and clicks UI elements in any app.                                                                                                                                                              |
| **T**            | Smart Translator                                  | Translates text under navigator cursor or selection.                                                                                                                                                                                              |
| **Shift + T**    | Clipboard Translator                              | Translates content currently in the clipboard.                                                                                                                                                                                                    |
| **R**            | Text Refiner                                      | Summarize, Fix Grammar, Explain, or run **Custom Prompts**.                                                                                                                                                                                       |
| **V**            | Object Vision                                     | Describes the current navigator object.                                                                                                                                                                                                           |
| **O**            | Full Screen Vision                                | Analyzes the entire screen layout and content.                                                                                                                                                                                                    |
| **Shift + V**    | Video Analysis                                    | Analyze local video files or online **YouTube**, **Instagram**, **TikTok**, or **Twitter (X)** videos.                                                                                                                         |
| **Control + V**  | Local Video Recording                             | Records a silent video of your screen and analyzes the actions and layout.                                                                                                                                                                        |
| **D**            | Document Reader                                   | Advanced reader for PDF, images, and plain text/HTML files with page range selection.                                                                                                                                                             |
| **F**            | **Smart File Action**                             | Context-aware recognition from selected image, PDF, or TIFF files.                                                                                                                                                                                |
| **M**            | Media Transcription & Dubbing | Transcribe or Dub audio/video files (MP3, WAV, MP4, etc.) into your target language.                                                                                                                           |
| **C**            | CAPTCHA Solver                                    | Captures and solves CAPTCHAs.                                                                                                                                                                                                                     |
| **Shift + C**    | Direct Chat                                       | Opens a direct text-based chat interface with the AI.                                                                                                                                                                                             |
| **S**            | Smart Dictation                                   | Converts speech to text. Press to start recording, again to stop/type.                                                                                                                                                            |
| **Control+T**    | Voice Translation                                 | Transcribes, translates, and types the result based on your language settings.                                                                                                                                                                    |
| **Control+L**    | **Live Assistant**                                | **ライブアシスタント**: リアルタイムの音声および画面アシスタント機能を追加しました。Google Geminiプロバイダー（またはGemini互換のカスタムプロバイダー）専用で利用できます。ダイアログ内で直接インタラクティブな音声や思考深度のカスタマイズが可能で、設定変更時には自動的に再接続されます。                                                                                        |
| **Control+A**    | **Live Operator**                                 | **Autonomous Computer Control (Gemini only):** Starts or ends a live voice session in which the operator carries out your requests on the computer.                                                            |
| **G**            | **Gemini API Key Manager**                        | **Create your API key without the web (Gemini only):** Opens the manager that sets up what your computer needs, opens the browser to sign in, and creates, copies or deletes a key for the project you choose. |
| **I**            | Status Reporting                                  | Announces current progress (e.g., "Scanning...", "Idle").                                                                                      |
| **L**            | **Label Object**                                  | **Semantic AI Labeling:** Permanently labels the current focused element/icon.                                                                                                                                                    |
| **Shift + L**    | **Manage/Scan Labels**                            | Opens Label Manager (if labels exist) or scans the app for unnamed elements.                                                                                                                                                   |
| **U**            | Update Check                                      | Manually check GitHub for the latest version of the add-on.                                                                                                                                                                                       |
| **Space**        | Recall Last Result                                | Shows the last AI response in a chat dialog for review or follow-up.                                                                                                                                                                              |
| **H**            | Commands Help                                     | Displays a list of all available shortcuts.                                                                                                                                                                                                       |
| **Control + H**  | **History**                                       | Opens the History dialog listing your past chats and documents, with type filters and Delete/Clear options.                                                                                                                                       |
| **Alt + S**      | Settings                                          | Vision Assistant Proには高度なツールが多数搭載されています。適切な機能を選択するのに役立つ、一般的なシナリオをいくつか紹介します。                                                                                                                                                                                       |
| **Alt + Q**      | Quota Exhausted Keys Report                       | **クォータ枯渇キーのレポート (`Alt + Q`)**: デ日の制限を超過したGemini APIキーの正確な数を報告し、どの特定モデルで枯渇しているかを特定して、正確なリセット時間をアナウンスします。                                                                                                                        |
| **Alt + M**      | Routing Audit                                     | Reports the AI models currently selected in advanced routing.                                                                                                                                                                                     |
| **Up / Down**    | Quick Settings Nav                                | Navigates between quick settings categories (Provider, Model, etc.) in the layer.                                                                                                                              |
| **Left / Right** | Change Quick Setting                              | Changes the value of the currently selected quick setting.                                                                                                                                                                                        |

## 6. ビデオ分析と音声解説

Chat windows and the History dialog work across all features, so you can review conversations and pick up right where you left off.

### 4.1 Chat Window Shortcuts

When a chat window is open (Direct Chat, document chat, refine, and similar), you can review the conversation with:

- **Alt + Down:** Read the next message.
- **Alt + Up:** Read the previous message.
- **Alt + C:** Copy the current message.

### 4.2 History (Control + H)

Press **Control + H** in the Command Layer to open the **History** dialog with your past chats and documents, filterable by type (All / Chats / Documents). Open a chat to continue the conversation — including its attached files, which are re-attached automatically — or open a document and keep reading. Press **Delete** on any item to remove it, or **Clear All** to empty the list. For documents, Delete asks whether you want to remove only the history entry or also clear that document's cached OCR text so the next open re-scans it from scratch — with a **Don't ask again** option to remember your choice.

You can also choose what the list remembers. **Save chats to history** (Connection tab) and **Save documents to history** (Document Reader tab) are both on by default, and both can be toggled in Quick Settings. The document option affects the History entry only — cached OCR text and resume data are always kept.

## 9. セマンティックAIラベリング & UIエクスプローラー

The **AI Operator** turns Vision Assistant Pro from a passive reader into an active assistant that can interact with your computer on your behalf. You can ask it to describe the screen, answer questions about what it sees, or even take control—clicking buttons, dragging items, typing text, and navigating through applications using natural language commands.

The biggest advantage? It works perfectly in completely inaccessible software. If you are stuck in a custom app, a remote desktop, or a website where your screen reader goes totally silent, the operator doesn't mind. Because it "sees" the screen visually, it can find, read, and interact with elements that have zero accessibility labels.

### 5.1 How It Works

1. Press **NVDA + Shift + V**, then press **Shift + A** (or use the direct shortcut) to open the AI Operator dialog.
2. Type what you want to do in plain language (e.g., "Click the Save button", "What does the error message say?", or "Rename the file to final.pdf").
3. The AI will analyze your screen, identify the relevant elements, and carry out the action or provide the answer. If a task requires multiple steps, the operator will continue working until it's complete.
4. Press **Shift + A** again at any time to instantly abort an ongoing operation.

### 5.2 Supported Actions

The operator understands a wide range of commands:

- **Describe & Answer**: "Describe the screen layout" or "What does the error message say?"
- **Click**: "Click the Save button"
- **Right Click**: "Right-click the file"
- **Double Click**: "Double-click the document"
- **Drag & Drop**: "Drag the document to the Archive folder"
- **Type**: "Type 'Hello World' in the search box"
- **Scroll**: "Scroll down three times"
- **Keypress**: "Press Enter", "Press Tab", "Press Escape"
- **Multi-step Tasks**: "Open File Explorer, find the report, and rename it to final.pdf"

### 5.3 Important Notes

- **⚠️ API Usage Warning**: Because the operator needs to "see" exactly what's happening on screen, it sends a high-resolution screenshot with every step. Frequent use will consume your API quota much faster than standard text-based features.
- **Administrator Applications**: If NVDA is not running with Administrator privileges, the operator may not be able to interact with windows that require elevated permissions. This is a Windows security limitation, not a bug in the add-on.
- **Best Practices**: For best results, give clear and specific commands. "Click the blue Submit button at the bottom of the form" will almost always work better than just "Click the button".

### 5.4 Live Operator (Control+A)

The Live Operator lets the Live Assistant carry out what you ask on your computer while you talk to it, including applications that your screen reader cannot read.
_(Note: This feature is exclusive to Google Gemini and Gemini-compatible Custom providers)._

- **Activation:** Press **Control+A** in the Command Layer to start a live operator session; press it again to end it.
- **How it works:** Ask in plain language, for example "open Chrome and search for a website" or "rename this file to final". The operator looks at the screen, carries out the steps one by one, and keeps working through multi-step requests until the task is done.
- **Announcements:** Every step is spoken in the Live Assistant's own voice, and it tells you when the task is finished, or why it could not be done.
- **CAPTCHA:** If a CAPTCHA appears, the operator tries your built-in **CAPTCHA solver** first; if it cannot solve it, it asks you to complete the accessible challenge yourself.
- **Stopping:** Press **Stop operator action** in the Live Assistant window to cancel the current task.
- **Settings:** The operator's own instruction can be edited in the Prompt Manager (section **Live**, **Live Operator Instruction**). The **Live Direct Output (No Window)** switch is available in Quick Settings as well.

## 7. メディアの文字起こしとダビング (M)

> **注意:** ビデオ分析および音声解説の機能は、**Google Gemini** プロバイダーでのみ動作します。アドオンの設定でアクティブなプロバイダーが Google Gemini に設定されていることを確認してください。 Ensure that your active provider in the add-on settings is set to Google Gemini.

Vision Assistant Pro は、視覚障害者向けに特別に設計された強力なビデオ処理機能を提供します。オンラインビデオとローカル画面録画の両方を分析し、詳細な視覚的説明の提供や、プロ仕様の音声解説スクリプト（SRT）の生成を行うことができます。 It can analyze both online videos and local screen recordings to provide highly detailed visual descriptions and generate professional Audio Description scripts (SRT).

### 6.1 ローカル画面録画 (Control + V)

画面上の音声のないビデオ、アニメーション、チュートリアルなどに遭遇した場合、直接キャプチャすることができます：

1. **NVDA + Shift + V** を押してコマンド層に入り、**Control + V** を押します。
2. アドオンがバックグラウンドで画面の録画をサイレントに開始します。
3. もう一度 **Control + V** を押して録画を停止します。
4. その後、AI が録画されたビデオセグメントを分析し、シーン、登場人物、アクションに関する非常に詳細な説明を提供します。

### 6.2 ビデオ分析 (Shift + V)

ローカルのビデオファイルとオンラインビデオの両方を分析できます。エクスプローラーでローカルのビデオファイルを選択するか、オンラインビデオのリンクをクリップボードにコピーするだけです。また、任意の場所（メディアプレイヤー内など）で **Shift + V** を押すと、ビデオファイルを参照したり、URLを手動で貼り付けたりできるダイアログが開きます。 Simply select a local video file in Windows Explorer, or copy an online video link to your clipboard. You can also press **Shift + V** anywhere (like inside a media player) to open a dialog where you can browse for a video file or paste a URL manually.

- **サポートされているオンラインプラットフォーム:** YouTube、Instagram、TikTok、Twitter (X)。
- AIがローカルファイルまたはURLを自動的に検出し、ビデオを処理して、包括的な視覚的説明と音声の要約を提供します。
- **48時間動画ファイルキャッシュ**: Geminiにアップロードされた動画が48時間キャッシュされるようになりました！NVDAを再起動した後でも、動画を再アップロードすることなく、同じ動画のSRTまたはMP3出力を再生成できます。キャッシュはキーを認識しており、APIキーが変更された場合に自動的に無効化されます。 You can regenerate SRT or MP3 outputs for the same video without re-uploading — even after restarting NVDA. The cache is key-aware and automatically invalidated when your API key changes.

### 6.3 音声解説の生成 (SRT)

より構造化された体験のために、アドオンは標準の SubRip (SRT) 形式でプロ仕様の音声解説スクリプトを生成できます。

- **スマートギャップタイミング:** AIが音声トラックを聴き取り、対話の重なりを最小限に抑えるように、自然な間や無音のギャップに視覚的説明を正確にアンカーします。
- **Character Tracking:** The engine performs a pre-pass to extract distinct characters based on immutable facial features. It builds a global dictionary to accurately track and label characters across different scenes without confusion. It also tracks each character's **first appearance**, describing their physical look only once — at the moment they first show up — and using established names only in later scenes to keep the narrative fresh and natural.
- **厳密なテキストOCR:** 画面上に表示されるテキスト（看板、電話、クレジット）は、厳密にそのまま引用されます。
- **使用方法:** 生成された字幕を聴くには、`.srt` ファイルをビデオファイルと同じフォルダに配置し、全く同じ名前を付けるだけです。その後、再生中に字幕テキストを直接スクリーンリーダーまたはTTSエンジンにルーティングするようにメディアプレイヤー（VLCやPotPlayerなど）を設定します。 Then, configure your media player (e.g., VLC or PotPlayer) to route the subtitle text directly to your screen reader or TTS engine during playback.
- **保存エクスペリエンスの向上:** SRTまたはMP3ファイルを保存する際、ファイルダイアログからビデオを開いた場合でも、エクスプローラーから Shift+V で開いた場合でも、ファイルダイアログはデフォルトでソースビデオのフォルダで開くようになりました。

### 6.4 同期音声ナレーション (MP3エクスポート)

Beyond just creating text-based SRT files, the add-on functions as a complete Audio Description production tool by synthesizing the descriptions into speech and mixing them with the video. You can now choose **Gemini Live TTS** as the voice engine, which utilizes the Gemini Live API to generate highly realistic, unlimited voice narration. When generating an MP3 for local video files, you have multiple mixing modes:

- **標準AD (ボイスミックス):** ナレーションがビデオの音声の上に直接重ね合わされます。ナレーションがクリアに聞こえるように、**オーディオダッキング**（説明中の背景音量を下げる）を適用するかどうかを確認するプロンプトが表示されます。 You will be prompted if you want to apply **Audio Ducking** (lowering the background volume during descriptions) to ensure the narration is clear.
- **拡張AD (オーディオ一時停止):** 説明中に元のビデオ音声が一時停止するため、元のダイアログやAIナレーションの単一の単語を聞き逃すことがなくなります。無音検出には、正確なギャップタイミングのために **Silero VAD** ニューラルモデル（ffmpegやeSpeakと同様に、初回使用時に自動ダウンロードされます）を使用し、音楽や背景雑音と自然なダイアログの間を区別します。 Silence detection now uses the **Silero VAD** neural model (downloaded automatically on first use, just like ffmpeg and eSpeak) for precise gap timing — distinguishing natural dialogue pauses from music and background noise.
- **YouTubeビデオ:** （ローカルにダウンロードされない）YouTubeのソースの場合、MP3エクスポートには背景のビデオ音声なしで、同期されたAI音声トラックのみが厳密に含まれます。

## 8. 高度な文書＆画像リーダー

The Audio Transcriber has been completely rebuilt to support both audio and video files (MP3, WAV, MP4, MKV, etc.). Press **M** in the Command Layer to select a media file and choose one of 3 distinct operation modes:

1. **文字起こし（原言語）**: 話されている言葉を元の言語のまま正確に文字起こしします。
2. **文字起こしと翻訳（ターゲット言語）**: 音声を文字起こしし、設定したターゲット言語に翻訳します。
3. **ダビングと翻訳（ターゲット言語）** _（Geminiのみ）_: 音声を文字起こししてターゲット言語に翻訳し、アドオンのTTSエンジンを使用して音声ダビングを合成する強力な新機能です。

## 10. ライブ音声アシスタント

The **Document Reader** turns your documents into clean, readable text — so you can read, translate, and listen to anything from a scanned book to a stack of photos. It handles multi-page PDFs, complex images, iPhone HEIC formats, and even plain text (`.txt`) and HTML (`.html`, `.htm`) files, which are opened instantly with no OCR or AI processing. Select several files at once and they are merged into a single continuous document in page order. Three OCR engines are available — **Chrome (Fast)**, **AI (Advanced)** for superior layout preservation, and **None (Extract Text Layer)** for searchable PDFs — selected in Settings → Document Reader.

### How It Works

1. **NVDA + Shift + V**を押してから**D**を押して文書リーダーを開くか、エクスプローラーでファイルを事前にハイライトし、**D**または**F**を押してファイルダイアログを完全にスキップします。
2. 1つ以上のPDFまたは画像を選択します。アドオンがそれらをスキャンし、総ページ数をアナウンスします。 The add-on scans them and announces the total page count.
3. In the **Options** dialog, choose the page range (From/To). **オプション**ダイアログでページ範囲（開始/終了）を選択します。また、**出力の翻訳**にチェックを入れてターゲット言語を選択したり、**OCR中の画像インライン説明**を切り替えたり、大きすぎるスキャンページをアップロード前に縮小・再圧縮する**処理前にPDFページを圧縮**を切り替えることもできます。
4. Text extraction starts in the background in batches. You can close the window at any time and continue later — nothing is lost.
5. ページの準備ができたら、ビューアーで読み取ります：ページの移動、任意のページへのジャンプ、AIへの質問、テキストの保存、または音声の生成を行います。

### 8.1 バッチ処理と再開

You don't need to read a massive document all at once. Choose a page range (e.g., `1-20`) or keep the defaults to process everything, and the AI extracts all pages in the background. If NVDA crashes or you interrupt the scan, the add-on remembers your progress and offers to **Resume** exactly where it left off — even across restarts. Completed documents are also cached, so reopening them (from Recent Documents or via **D**) loads the text instantly without re-running OCR, unless the source files have changed.

### 8.2 スマートファイルアクション

常に最初に文書を開く必要とは限りません。WindowsのエクスプローラーでPDF、画像、またはテキスト/HTMLファイルをハイライトし、コマンドレイヤー内で**D**（文書リーダー）を押すか、PDFまたは画像をハイライトして**F**（スマートファイルアクション）を押します。アドオンはファイルダイアログを即座にバイパスし、ハイライトされたファイルの処理を開始します。複数のファイルを一度に選択すると、1つの文書としてまとめて処理されます。 In Windows File Explorer, simply highlight a PDF, image, or text/HTML file and press **D** (Document Reader) — or highlight a PDF or image and press **F** (Smart File Action) — inside the Command Layer. The add-on instantly bypasses the file dialog and begins processing the highlighted file. Selecting several files at once processes them together as one document.

### 8.3 文書ビューアーの操作とショートカット

文書リーダーウィンドウが開いているときは、以下の操作を使用できます。

#### キーボードショートカット

- **Ctrl + PageDown / Ctrl + PageUp:** 次のページ / 前のページに移動します。
- **下 / 上矢印:** カーソルがページの最終行に達したとき、**下**を押すと次のページにジャンプし、ページの先頭で**上**を押すと前のページに戻ります。
- **Alt + A:** 文書に関する質問をするためのチャットダイアログを開きます。
- **Alt + R:** アクティブなプロバイダーを使用して**AIによる再スキャン**を強制実行します。
- **Alt + G:** 高品質な音声ファイル（WAV/MP3）を生成して保存します。_(プロバイダーがTTSをサポートしていない場合は非表示になります)_。 _(Hidden if the provider doesn't support TTS)._
- **Alt + S / Ctrl + S:** 抽出したテキストをTXTまたはHTMLファイルとして保存します。

#### ボタンとコントロール

- **移動先（Go to）:** ページセレクターから任意のページを選択します。
- **整形済み表示（View Formatted）:** 文書全体をフォーマット済みテキストとして結合して表示します。
- **失敗したページを再試行（Retry Failed Pages）:** 一時的なサーバーエラー（高負荷など）が原因で失敗したバッチのみを再試行します。このボタンは必要な場合に自動的に表示されます。 This button appears automatically when needed.
- **TTS音声 / TTSエンジン:** 音声を選択します。Geminiの場合は、**標準TTS**と**Gemini Live**ストリーミングから選択できます。
- **前へ / 次へ:** ページ間を移動します（Ctrl+PageUp/Downショートカットと同じ）。

### 8.4 最近使った文書 (D)

Pressing **D** in the Command Layer lists your recently read documents first. コマンドレイヤーで**D**を押すと、最近読んだ文書が最初にリストされます。OCRがすでに完了している場合でも、選択して以前のページから続行できます。または**ファイルを開く...**（`Ctrl + O`）を押して、通常どおりファイルを参照することもできます。

## 11. アンビエント・オブザーバー（バックグラウンド・アシスタント）

「ラベルのないボタン」だらけのアプリケーションでお困りですか？セマンティックAIラベリングエンジンがこの問題を恒久的に解決します。 The Semantic AI Labeling engine solves this permanently.

### 9.1 永続的なオブジェクトラベリング (L)

Focus your screen reader on an unlabeled graphic or button and press **L** in the Command Layer. The AI will look at the button visually, determine its function, and apply a permanent label.
_Unlike older screen reader labeling tools, this add-on uses an advanced hybrid "Object Signature" system (AutomationId/ControlID). Your custom labels will survive window resizing, monitor switching, and application updates!_

### 9.2 アプリケーション全体のスキャン (Shift + L)

Press **Shift + L** to scan the entire active window at once. The AI will find all unlabeled elements and intelligently name them in one go. You can later manage, rename, or batch-delete these labels from the built-in Label Manager.

### 9.3 UIエクスプローラー (E)

Need to interact with an element without navigating to it manually? Press **E** to activate the UI Explorer. The AI will scan the screen and generate an accessible list of every clickable element (ignoring system noise like taskbars). Pick an item from the list, and the add-on will instantly click it for you.

## 15. プロジェクトのサポーター

ライブアシスタントは、Vision Assistant Proをリアルタイムのインタラクティブなコパイロットに変えます。
_(注: この機能はGoogle GeminiおよびGemini互換のカスタムプロバイダー専用です。)_
_(Note: This feature is exclusive to Google Gemini and Gemini-compatible Custom providers)._

- **起動:** コマンドレイヤーで **Control + L** を押して、ライブアシスタントダイアログを開きます。
- **Real-time Interaction:** Talk naturally through your microphone. The AI will simultaneously listen to your voice and look at your active screen. You can ask questions like "What am I looking at?" or "Read the third paragraph to me."
- **プッシュツートーク:** ライブアシスタントの設定タブで **プッシュツートーク** を有効にするか（またはライブアシスタントウィンドウ内で直接切り替える）、割り当てられたキーを押しながら話して、離して終了します。キーを押すまでマイクがミュートされるため、騒音の多い環境に最適です。 This keeps the microphone muted until you press the key — perfect for noisy environments.
- **Webcam Input:** Tick **Use &Webcam** in the Live Assistant window to send your camera feed to the AI instead of your screen — ask about physical objects, printed documents, or your surroundings. **Webカメラ入力:** ライブアシスタントウィンドウで **Webカメラを使用する (&W)** にチェックを入れると、画面の代わりにカメラの映像をAIに送信します。物理的なオブジェクト、印刷されたドキュメント、周囲の環境について質問できます。ffmpegがまだインストールされていない場合は、チェックを入れると許可を得て一度だけダウンロードされます。カメラが検出されない場合や、Windowsのプライバシー設定でカメラアクセスがブロックされている場合、このオプションは無効になります。
- **カスタマイズ:** ダイアログ内では、AIの音声スタイル（プロフェッショナル、フレンドリー、アップビートなど）の変更や、「思考の深さ」の調整を行い、回答する前にどれだけ深く推論するかを制御できます。

## 14. サポートとコミュニティ

アンビエント・オブザーバーは、会話なしでVision Assistant Proをバックグラウンドの「目」に変えます。作業中も聞き取りや監視を続け、変化があったことだけを報告し、何も起きない時は静かにしています。
_(注意: この機能は、Google GeminiおよびGemini互換のカスタムプロバイダーでのみ利用可能です。)_
_(Note: This feature is exclusive to Google Gemini and Gemini-compatible Custom providers)._

- **Activation:** Press **Shift+O** in the Command Layer to open the Ambient Observer dialog; press it again to stop the observer.
- **モード:** **音声翻訳のみ**（聞き取った音声を翻訳）、**画面ウォッチャーのみ**（画面の変化を報告）、**Webcamウォッチャーのみ**（カメラ映像とプッシュ・オブ・トーク機能を持つライブアシスタントウィンドウを開き、カメラに映っているものについて質問できます）があります。
- **音声ソース:** 音声モードでは、**マイク**または\*\*システム音声（ループバック）\*\*のどちらを翻訳するかを選択します。小さなループバックライブラリは、初回使用時に許可を得た上で一度だけダウンロードされます。 The small loopback library is downloaded once on first use, with your permission.
- **コンテキスト:** 画面およびWebcamモードでは、任意の**何をしているか**オプション（映画鑑賞、会議や通話への参加、ラベルの読取り、身だしなみの確認など）を選択して報告の焦点を絞ることができます。また、独自のコンテキストを入力することもできます。
- **報告:** アドオンはすべての新しいフレームを前のフレームと比較し、画像に実際の変化があった場合にのみAIに送信するため、静止画面でリクエストが無駄に消費されることはありません。AIは新着情報のみを報告し、同じことを繰り返しません。 The AI then reports only what is new and never repeats itself.
- **ウェルカムメッセージ:** 翻訳モードを除き、オブザーバーの起動時に簡単な挨拶があり、監視中であることがわかります。
- **Settings:** In **Settings > Live Assistant**, set the **Observer Mode**, the **Frame Interval** (1 to 10 seconds) and the **Reporting Style** (brief or detailed). The observer instruction and each context text can be edited in the Prompt Manager (section **Ambient**).

## 12. カスタムプロンプトと変数

プロンプトは **設定 > プロンプト > プロンプトの管理...** から管理できます。

- **フィルター:** **デフォルトプロンプト**タブのプロンプト一覧の上部には**すべて**または特定のセクション（**アンビエント**など）のみを表示する**フィルター**リストがあり、長いリストでも簡単に操作できます。

### カスタムプロンプトのショートカット

プロンプトマネージャーで任意のカスタムプロンプトに独自のショートカットキーを直接割り当て、現在の選択範囲やコンテキストで即座に実行できます：

- **単一キー**（例：`1`、`p`、`F3`）：コマンドレイヤー内で機能するほか、グローバルに `NVDA + Shift + キー` として機能します。
- **キーの組み合わせ**（例：`Control + Shift + 1`、`Alt + P`、`Insert + 1`）：単独でグローバルに機能します。

### プロンプトごとのフィードバック動作

各カスタムプロンプトでは、出力の配信動作を個別に定義できます：

- **グローバル設定:** 一般的な接続の出力設定（直接出力またはチャットウィンドウ）に従います。
- **クリップボードにコピー:** ウィンドウを開かずに、AIの応答を直接クリップボードにコピーします。
- **直接出力（NVDAメッセージ）:** NVDAの音声により、AIの応答を直接読み上げ/点字出力します。
- **クリップボードにコピーして直接出力:** 応答をクリップボードにコピーし、直接読み上げます。
- **チャットウィンドウ:** 結果を常にインタラクティブな会話ウィンドウで開きます。

### サポートされている変数

- `[selection]`: 現在選択されているテキスト。
- `[text]`: 現在フォーカスされている編集フィールドのテキスト内容全体（保護されたパスワードボックスは自動的に無視されます）。
- `[currentURL]`: サポートされているウェブブラウザ（Chrome、Edge、Firefox）からのウェブページまたはドキュメントのURL。
- `[clipboard]`: クリップボードの内容。
- `[clipboard_image]`: 現在クリップボードにある画像。
- `[screen_obj]`: ナビゲーターオブジェクトのスクリーンショット。
- `[screen_fg_obj]`: アクティブなフォアグラウンドウィンドウのスクリーンショット。
- `[screen_full]`: 全画面のスクリーンショット。
- `[file_ocr]`: テキスト抽出用の画像/PDFファイルを選択します。
- `[file_read]`: 読み取り用のドキュメント（TXT、コード、PDF）を選択します。
- `[file_audio]`: 分析用の音声ファイル（MP3、WAV、OGG）を選択します。
- `[ambient_screen]`: 継続的な画面オブザーバーのバックグラウンドセッションを開始します。
- `[ambient_webcam]`: 継続的なウェブカムオブザーバーのバックグラウンドセッションを開始します（設定からプッシュツートークを確認します）。
- `[ambient_audio]`: ライブ音声オブザーバーの翻訳セッションを開始します。
- `[loopback]`: システムの音声再生を音源として使用します（`[ambient_audio]`用）。
- `[mic]`: マイクを音源として使用します（`[ambient_audio]`および`[ambient_webcam]`用）。
- `[brief]`: Sets observer reporting style to brief (single sentence).
- `[detailed]`: オブザーバーのレポートスタイルを詳細（2〜3文）に設定します。
- `[lang:code]`: 音声翻訳のターゲット言語コードを指定します（例：`[lang:fa]`、`[lang:en]`）。
- `{target_lang}`: 現在のターゲット言語。
- `{source_lang}`: 現在のソース言語。
- `{response_lang}`: 現在のAI応答言語。
- `{swap_target}`: スマートスワップ翻訳のフォールバック言語。
- `{swap_instruction}`: スマートスワップ翻訳の指示ブロック。

_Note on Ambient Prompts:_ Prompts containing ambient variables act as a toggle — pressing the shortcut while active immediately stops the session. Incompatible combinations (such as combining static screenshot variables like `[screen_full]` with ambient observer modes, combining multiple ambient modes, or adding prompt instructions to `[ambient_audio]`) are strictly validated and prevented when saving.

## 13. 実際のユースケース（どの機能を使うべきか？）

Vision Assistant Pro is packed with advanced tools. Here are some common scenarios to help you choose the right one:

- **シナリオ: 複雑なウィンドウやアクセシビリティ対応していないアプリの全体的なレイアウトを理解したい。**
  _解決策:_ **O**（画面全体ビジョン）を押します。AIが画面全体を解析し、要素、テキスト、ボタンがどこに配置されているかを正確に説明します。 The AI will analyze the entire screen and describe exactly where elements, texts, and buttons are positioned.

- **シナリオ: ウェブページ上で画像を見つけた、またはドキュメント内にラベルのない画像があった。**
  _解決策:_ ナビゲーターオブジェクトをその画像に移動し、**V**（オブジェクトビジョン）を押します。AIがその画像の内容を具体的に説明します。 The AI will describe specifically what that image contains.

- **Scenario: You want to watch a movie or video clip with audio descriptions.**
  _Solution:_ Press **Shift + V** on your video and choose **"Generate Audio Description (SRT File)"**. When it finishes, click **"Generate Synced Narration (MP3)"** and select **"Extended AD"**. The add-on will create an audio track that intelligently pauses the movie's dialogue to describe the visual scenes.

- **Scenario: You encountered an app full of "unlabeled buttons".**
  _Solution:_ Press **L** to permanently label the specific button using AI. Or, press **Shift + L** to scan and label the entire window at once. If you just want to click something quickly, press **E** (UI Explorer) to get a list of all clickable items.

- **Scenario: You need to bypass an inaccessible CAPTCHA.**
  _Solution:_ Press **C** (CAPTCHA Solver). **シナリオ: アクセシビリティ対応していないCAPTCHA（画像認証）を回避する必要がある。**
  _解決策:_ **C**（CAPTCHAソルバー）を押します。AIが自動的にCAPTCHAをキャプチャして解決し、正しいフィールドに答えを入力します。

- **シナリオ: 50ページに及ぶ長いPDFドキュメントを読みたい。**
  _解決策:_ **D**（ドキュメントリーダー）を押し、プロバイダをGoogle Geminiに設定して、ページ範囲 `1-50` を入力します。アドオンがバックグラウンドでテキストを正確に抽出します。 The add-on will extract the text accurately in the background.

- **Scenario: You are watching a silent video tutorial or animation on your screen.**
  _Solution:_ Press **Control + V** to start recording the screen. Let the tutorial play, then press **Control + V** again. The AI will explain exactly what was demonstrated.

- **シナリオ: 予期せぬエラーやAPI接続の失敗が発生した、あるいはカスタムローカルサーバーの問題を診断したい。**
  _解決策:_ **[設定] > [高度な設定]** に移動し、\*\*「専用ログファイルを有効にする」**をオンにして、**ログレベル**を**「デバッグ (Debug)」**に設定します。もう一度その操作を行い、**「ログファイルを開く」\*\*をクリックして技術的な詳細を確認するか、サポートチケットに `vision_assistant.log` を添付してください。 Perform the action again, then click **"Open Log File"** to inspect technical details or attach `vision_assistant.log` to a support ticket.

***

**注意:** すべてのAI機能を使用するには、アクティブなインターネット接続が必要です。複数ページのドキュメントは自動的に処理されます。 Multi-page documents are processed automatically.

## 14. Support & Community

最新ニュース、機能、リリース情報を入手してください：

- **Telegramチャンネル:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** バグ報告や機能リクエストはこちらから。

### バグやログの報告

When opening a GitHub issue or asking for support, please include details about your active AI provider, model, and NVDA version. If you are experiencing connection issues or unexpected crashes, enable the dedicated log file in **Settings > Advanced**, recreate the issue, and attach your `vision_assistant.log` file to help us resolve the problem faster.

## 15. Project Supporters

このプロジェクトの継続的な開発と保守を寛大な経済的支援により支えてくださっているコミュニティメンバーの皆様に心より感謝申し上げます。

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **leonardo0216**
- **Sergei Fleytin**
- **Arne Siebert**
- **Schalkefan**
- **Rainer Brell**
- **[avalai.org](https://avalai.org)**

\*経済的にプロジェクトを支援し、ここに名前を掲載したい場合は、NVDAの「ツール」メニュー（「Vision Assistant」サブメニュー）またはインストール後のセットアッププロセスで\*\*寄付（Donate）\*_オプションを見つけることができます。_

---

## 2026.10.15 の変更点

- **The Most Requested Fix — Creating a Gemini API Key Is Finally Easy**: Getting an API key on **aistudio.google.com** used to be the hardest step of all. With a screen reader the pages were confusing, and some people simply could not create a key at all. That problem is now solved directly inside the add-on. Press **G** in the Command Layer (or use **Get a Gemini API Key...** in Settings), sign in through your default browser with zero external setup, and your key is created and configured with one confirmation — even if you never had a project before.
- **Ambient Observer**: The background assistant is here. Press **Shift+O** in the Command Layer to start it, and press it again to stop it. It can translate what it hears (your microphone or the sound of the system), watch the screen and tell you what changed, or open the Live Assistant with your webcam and Push to Talk so you can ask about whatever the camera sees. It sends a picture only when something really changed, so a still screen costs you nothing, and it stays quiet when nothing is happening. You can also launch and toggle the observer directly through Custom Prompts and dedicated shortcut keys using `[ambient_screen]`, `[ambient_webcam]`, or `[ambient_audio]` along with modifiers (`[loopback]`, `[mic]`, `[brief]`, `[detailed]`, `[lang:code]`), with automatic validation against conflicting variable combinations.
- **Live Operator**: The Live Assistant can now carry out what you ask on your computer while you talk to it. Press **Control+A** in the Command Layer to start a live operator session, then just ask in plain language. It works through multi-step requests, says every step in the Live Assistant’s own voice, takes care of the key combinations it needs, and decides by itself when the task is finished. **Live Direct Output (No Window)** is in Quick Settings too.
- **Character Dictionary & Series Management**: The Video Analysis dialog now includes a powerful **Character Dictionary** system! Add, edit, import, or manage character names, physical descriptions, and roles per series — the AI automatically matches discovered characters to your dictionary and merges new ones as you analyze more episodes. Your manual notes are always preserved with priority over AI updates, while physical descriptions stay up-to-date across episodes. The dictionary is saved per series and reused for every video in that series. In the character list, press **F2** to edit the selected character and **Delete** to remove it.
- **SOCKS5, HTTP, and Reverse Proxy Support with Latency Testing**: Seamlessly bypass network restrictions with complete proxy support across the entire add-on — including the Live Assistant, Ambient Observer, and TTS generation! Choose from 4 operating modes in General settings: **Auto-detect**, **SOCKS5 Proxy**, **HTTP Proxy**, or **Reverse Proxy**. SOCKS5 supports RFC 1929 username/password authentication and domain tunneling; HTTP proxy supports Basic authentication. A new **Test Proxy Connection** button runs in the background and announces your connection latency in milliseconds.
- **48-Hour Video File Caching**: Videos uploaded to Gemini are now cached for 48 hours! You can regenerate SRT or MP3 outputs for the same video without re-uploading — even after restarting NVDA. The cache is key-aware and automatically invalidated when your API key changes.
- **AI駆動型無音検出（Silero VAD）**: 拡張ADで、正確な無音検出のためにSilero VADニューラルモデルが使用されるようになりました。これにより、自然な会話の間と、音楽や背景雑音とが区別されます。このモデルは、ffmpegやeSpeakと同様に、初回使用時に（許可を得た上で）自動的にダウンロードされます。 The model is downloaded automatically on first use (with your permission), just like ffmpeg and eSpeak.
- **ライブアシスタント用ウェブカム動画**: ライブアシスタントウィンドウに、画面の代わりにウェブカムのフィードをAIに送信するための **ウェブカムを使用(&W)** チェックボックスが追加されました。物理的なオブジェクト、書類、または周囲の環境に関する質問をするのに最適です。ffmpegがまだインストールされていない場合は、ボックスにチェックを入れると（初回のみ、許可を得た上で）ダウンロードされます。カメラが検出されない場合や、Windowsのプライバシー設定でカメラへのアクセスがブロックされている場合は、このオプションが無効になり、カメラのプライバシー設定を開くボタンが表示されます。カメラが有効であってもフレームが生成されない場合は、画面に暗黙的に切り替えるのではなく、診断のためにNVDAログに問題が記録されます。 If ffmpeg isn't installed yet, ticking the box downloads it (one-time, with your permission). The option is disabled when no camera is detected or Windows privacy settings block camera access, with a button to open the camera privacy settings. If the camera is enabled but produces no frames, the problem is logged to the NVDA log for diagnosis instead of silently switching back to the screen.
- **Audio Output Device Selection**: You can now select a dedicated audio output device for the Live Assistant and Ambient Observer. **音声出力デバイスの選択**: ライブアシスタントおよびアンビエントオブザーバー用の専用音声出力デバイスを選択できるようになりました。「ライブ設定」タブ、ライブアシスタントダイアログ内、またはクイック設定（`NVDA+Shift+V` を押した後に上下左右キー）から、NVDAのデフォルト出力、Windowsサウンドマッパー、または接続されている物理サウンドカード（USBヘッドホンや外部スピーカーなど）のいずれかを選択できます。
- **プロンプトマネージャー**: 「デフォルトプロンプト」タブに **フィルター** リストが追加され、すべてのプロンプトを表示するか、1つのセクション（**アンビエント** など）のみを表示するかを選択できるようになりました。また、そこでオブザーバーのコンテキストテキストや、新しく追加された **ライブオペレーター指示** を編集することもできます。 You can also edit the observer’s context texts and the new **Live Operator Instruction** there.
- **Smart Model Filtering in Advanced Routing**: Advanced Model Routing dropdowns now dynamically categorize Gemini models by capability without clutter. The Live Assistant only displays genuine bidirectional live and native-audio models, TTS only displays dedicated speech synthesis models, STT prioritizes Transcribe and multimodal models, and Video Analysis, OCR, and AI Operator cleanly filter out single-purpose utility models (such as image generation, video generation, and embedding models). Future models are detected automatically based on capability without requiring version updates.
- **キャラクター初登場追跡**: AIが各キャラクターの身体的特徴を説明するのは、動画への初登場時のみとなりました。以降の登場では名前のみが使用され、セグメント間での重複する説明が排除されると同時に、ナレーションが新鮮で自然な状態に保たれます。 Subsequent appearances use names only, eliminating repetitive descriptions across segments while keeping the narrative fresh and natural.
- **統合データディレクトリ**: すべてのアドオンデータファイル（履歴、シリーズ、ラベル、OCRの進捗状況、キャッシュ、およびログ）が、NVDA設定ディレクトリ内の単一の `VisionAssistant` フォルダに移行されました。これにより、すべてが整理され、手動でのバックアップが簡単になります。
- **動画保存エクスペリエンスの改善**: SRTまたはMP3ファイルを保存する際、ファイルダイアログを開いた場合でも、エクスプローラーから `Shift+V` で開いた場合でも、デフォルトでソース動画のフォルダが開くようになりました。
- **キャッシュされたテキストの有無によるドキュメントの削除**: 履歴ダイアログ（`Control + H`）でドキュメントを削除する際の2つの方法が提供されるようになりました。Deleteキーを押して、**履歴からのみ削除** または **履歴とキャッシュされたテキストから削除** を選択できます。2番目のオプションはそのドキュメントのキャッシュされたOCRテキストをクリアするため、次回開いたときに最初から再スキャンされます。これは精度の低いスキャンを行った後などに最適です。「**今後確認しない**」チェックボックスを使用すると、今後の削除のために選択内容が記憶されます。中断された操作の復元データが影響を受けることはありません。 The second option clears that document's cached OCR text, so the next open re-scans it from scratch — ideal after a poor scan. A **Don't ask again** checkbox remembers your choice for future deletions. Your interrupted-operation resume data is never touched.
- **ドキュメントリーダーにおけるエンジン認識型のマージOCRキャッシュ**: キャッシュされたOCRテキストがOCRエンジンごとに保存されるようになりました。これにより、OCRエンジンを切り替えたときに古い結果が再生されるのではなく、常に新しいエンジンで再スキャンされます。ドキュメントを再度開くと、ページ範囲ダイアログが再び表示され（最後の選択が事前に入力されます）、すでにスキャンされたページが即座に再利用され、不足しているページのみがスキャンされます。キャッシュは置き換えられるのではなくページごとにマージされるため、読み取ったすべての範囲が後で使用できるように保持されます。 Reopening a document shows the page-range dialog again (pre-filled with your last choice), instantly reusing already-scanned pages and scanning only the missing ones — the cache merges page by page instead of being replaced, so every range you read is kept for later.
- **PDF Compression in Document Reader**: Added an optional **Compress PDF pages before processing** setting in the Document Reader's page range dialog. When uploading large or high-resolution scanned PDF documents to Gemini or Mistral, pages are automatically downscaled and re-compressed to dramatically reduce upload payload size, speed up processing, and prevent network timeouts. The option is disabled by default and automatically hidden when using the Chrome engine or base64-based image providers.
- **Per-Prompt Feedback Behavior Customization**: Customize how each custom prompt delivers its output individually! In the custom prompt editor, choose between **Global setting**, **Copy to clipboard**, **Direct Output (NVDA message)**, **Copy to clipboard and Direct Output**, or **Chat window**. This allows specific prompts to speak directly without opening a window while others open a full chat.
- **新しい動的プロンプト変数（`[currentURL]` および `[text]`）**: カスタムプロンプトが、Google Chrome、Mozilla Firefox、Microsoft Edge全体でアクティブなドキュメントURLをキャプチャする `[currentURL]` と、現在フォーマットされている入力フィールドのテキストコンテンツ全体を動的に挿入する（保護されたパスワードボックスは無視されます）`[text]` をサポートするようになりました。
- **Twitter/X動画ダウンローダーの刷新**: 上流のスクレイパー障害に対応し、Twitter/X動画のダウンロードおよび分析機能が復旧しました。動画の抽出には堅牢な FixTweet API が使用されるようになり、自動 TwitSave フォールバックとプロキシサポートを完備した上で、TwitterのCDNから最高品質のMP4ストリームを直接取得します。 Video extraction now utilizes the robust FixTweet API to directly fetch highest-quality MP4 streams from Twitter's CDN, complete with automatic TwitSave fallback and proxy support.
- **Instagram動画ダウンローダーの修正**: ダウンローダーサービスにおける上流のフォーム変更に伴い、Instagramのリール（Reels）および動画URLのダウンロードと分析が復旧しました。
- **Fixes & Performance**: Push to Talk answers the moment you press the key, the Live Assistant no longer starts a reply in the middle of a sentence, the observer no longer reports the previous picture, and the Thinking Depth list only offers what your model actually supports. The AI Operator can scroll left and right too. Fixed an `AttributeError` when analyzing online videos, and prevented custom prompts without text selection from accidentally injecting background window titles into AI requests.

## 2026.09.01 の変更点

- **履歴 (Control + H)**: コマンドレイヤーに「すべて」「チャット」「ドキュメント」のフィルター付きで過去のチャットやドキュメントの一覧を表示する**履歴**ダイアログ（`Control + H`）が追加されました。完全な会話状態で任意のチャットを再開できます（添付ファイルも自動的に再添付されます）。また、ドキュメントを再開してそのまま読み続けることもできます。任意の項目で **Delete** キーを押すと削除でき、すべてを一度にクリアすることも可能です。 Reopen any chat with its full conversation — attached files are re-attached automatically — or reopen a document and keep reading. Press **Delete** on any item to remove it, or clear everything at once.
- **Recent Documents in the Reader**: Pressing **D** in the Command Layer now shows your recently read documents first. Pick one to continue from the page you were on — even when the OCR already finished — or press **Open File...** (`Ctrl + O`) to browse as usual.
- **ライブアシスタントのプッシュtoトーク**: ライブ会話を完全にコントロールできるようになりました！新しいライブアシスタントの設定タブで**プッシュtoトーク**を有効にし、`Left Ctrl` などの単独の修飾キーを含め、話すための任意のキーを割り当てます。キーを押している間だけ音声が伝わり、離すと終了します。押した時と離した時には短いビープ音が鳴ります。ライブアシスタントウィンドウ内にも対応する切り替えスイッチが表示されるため、会話から離れることなく、プッシュtoトークモードとオープンマイクモードを切り替えることができます。 Enable **Push to Talk** in the new Live Assistant settings tab and assign any key — or even a lone modifier like `Left Ctrl` — to talk. Hold the key to speak and release it when you're done, with a short beep on each press and release. A matching toggle also appears right in the Live Assistant window, so you can switch between push-to-talk and open-mic mode without leaving the conversation.
- **Gemini 2.5 Flash ネイティブ音声**: ライブアシスタントが、低遅延で自然な音声会話を実現する Gemini 2.5 Flash のネイティブ音声モデル（`gemini-2.5-flash-native-audio-preview-12-2025`）をサポートしました。\*\*設定 → 高度なモデルルーティング → ライブアシスタントモデル（Geminiのみ）\*\*から切り替えるか、「自動」のままにして推奨モデルを使用し続けることができます。 You can switch to it from **Settings → Advanced Model Routing → Live Assistant Model (Gemini only)**, or keep "Auto" to stay on the recommended model.
- **Settings Backup & Restore**: Added a powerful backup and restore system in the **Advanced** tab! You can now save all of your add-on settings — including API keys, models, custom prompts, and preferences — into a single JSON file, and restore them perfectly at any time, on any machine, or after reinstalling NVDA. When backing up, you choose what to include: **Everything** (settings, custom labels, OCR progress, and history) or **Settings Only**.
- **Direct Text & HTML Reading**: The Document Reader can now open plain text (`.txt`) and HTML (`.html`, `.htm`) files directly! **テキストおよびHTMLの直接読み込み**: ドキュメントリーダーで、プレーンテキスト（`.txt`）およびHTML（`.html`、`.htm`）ファイルを直接開けるようになりました！ファイルの文字コードを自動検出し、スクリプトや余分なフォーマットを取り除き、コンテンツを読みやすいページにスマートに分割します（ページ構造を維持したまま、アドオン固有の書き出しファイル自身を再インポートすることも可能です）。OCRやAI処理なしで、すぐに読み始めることができます！
- **ドキュメントリーダー向けの Gemini Live TTS**: 「音声を生成」ボタンが、高品質で自然なペースのストリーミング音声合成（TTS）エンジンである Gemini Live をサポートしました！Gemini アクティブプロバイダーとして使用している場合、リーダー内で標準TTSと Gemini Live を選択でき、選択内容は次回起動時にも記憶されます。 When Gemini is your active provider, you can choose between Standard TTS and Gemini Live right in the reader, and your selection is remembered for next time!
- **カスタムプロンプトのショートカット**: プロンプトマネージャーから、任意のカスタムプロンプトにショートカットキーを直接割り当てられるようになりました！すべてのプロンプトに専用のキーまたはキーの組み合わせを割り当てて即座に実行でき、追加の手順を踏むことなく、現在の選択範囲やコンテキストを自動的に取得します。 Give every prompt its own dedicated key or key combination to run it instantly, automatically capturing your current selection or context with zero extra steps!
- **Chat Message Navigation**: Review any conversation hands-free! Inside any chat window (Direct Chat, document chat, refine, and more), press `Alt + Down` to hear the next message and `Alt + Up` to hear the previous one — with clear "You" / "AI" prefixes and "First message" / "Last message" boundaries announced as you go.
- **チャットメッセージのコピー (Alt + C)**: `Alt + Up/Down` で会話を確認しているときに `Alt + C` を押すと、「クリーンMarkdown」設定に従って現在位置のメッセージがクリップボードにコピーされ、音声で確認が通知されます。
- **ダイレクトチャットのシステムプロンプト**: ダイレクトチャット（`Shift+C`）に、独自の編集可能なシステムプロンプト「ダイレクトチャットの指示」が追加されました。これにより、すべての会話におけるアシスタントのペルソナと応答言語を設定できます。プロンプトマネージャーの「デフォルトのプロンプト」タブからカスタマイズ可能です。 You can customize it from the Prompt Manager's Default Prompts tab.
- **ドキュメントリーダーのカーソルによるページ移動**: 複数ページにわたるドキュメントの読み取りがさらにスムーズになりました！ドキュメントビューアーでカーソルがページの最終行に達した状態で `Down` キーを押すと、リーダーが自動的に次のページにジャンプします。ページの先頭で `Up` キーを押すと、シームレスに前のページに戻ります。読書中に手動でページを切り替える必要はもうありません！ In the Document Viewer, when your cursor reaches the last line of a page and you press `Down`, the reader automatically jumps to the next page. Pressing `Up` at the start of a page seamlessly takes you back to the previous one — no more manual page switching while reading!
- **新しいクイック設定の切り替え**: AI応答をクリップボードにコピー、直接出力（チャットウィンドウなし）、チャット内のクリーンMarkdown、スマートスワップを、コマンドレイヤーのクイック設定から即座にオン/オフできるようになりました！
- **Live Assistant Settings Tab**: The Live Assistant now has its own dedicated settings tab! **ライブアシスタント設定タブ**: ライブアシスタント専用の設定タブが追加されました！「ライブアシスタント: 直接出力（ウィンドウなし）」オプションが接続タブからこちらに移動しました。このタブは、Google Gemini（またはGemini互換のカスタムプロンプト）がアクティブなプロバイダーである場合にのみ表示されます。

## 2026.08.06 の変更点

- **UIエクスプローラーのラベル付け**: UIエクスプローラー内で見つかった要素に直接ラベルを追加できるようになりました！新しい「ラベルを追加」ボタンが追加され、インターフェースは開いたままフォーカスが維持されるため、中断することなく複数のオブジェクトに素早くラベル付けできます。 A new "Add Label" button has been added, and the interface smartly stays open and preserves focus so you can rapidly label multiple objects without interruption.
- **Quick Settings Layer Enhancement**: The Vision Assistant layer (`Insert+Shift+V`) is now persistent and highly interactive! You can use `Up/Down` arrows to navigate between quick settings (Provider, Model, AI Response Language, TTS Model) and `Left/Right` arrows to instantly change their values with smart, concise voice feedback. Your selections take effect immediately (including auto-enabling advanced routing when necessary), and the layer stays alive while you configure.
- **ダイレクトチャット（`Shift+C`）**: レイヤーに新しいコマンドを追加しました！`Shift+C`を押すと、「ダイレクトチャット」ウィンドウが即座に開きます。これにより、画像やドキュメントを起点とすることなく、AIとクリーンなテキストベースの会話インターフェースをすぐに利用できます。 Press `Shift+C` to instantly open a "Direct Chat" window. This provides a clean, text-based conversational interface with the AI right away, without needing an image or document as a starting point.
- **Flawless Chat History Recall**: Fixed a major bug where pressing `Space` to recall the last result would lose your subsequent chat history. Now, the add-on globally tracks your conversation. If you chat, close the dialog, and press `Space` to recall it, your entire back-and-forth history is perfectly restored! Works for Direct Chat, Vision Analysis, Document Chat, and Translation.
- **OCRにおけるインライン画像説明**: ドキュメントのOCR実行時に、インラインで画像の説明を追加するオプション機能を追加しました。この設定は、アドオンのOCR設定、抽出前のドキュメントリーダーオプション内、およびクイック設定レイヤーからその場で素早く切り替えることができます。 You can toggle this setting in the add-on's OCR settings, within the Document Reader options before extraction, and quickly on-the-fly via the Quick Settings layer.
- **音声翻訳（`Control+T`）**: 強力な新機能を追加しました！音声をディクテーションし、設定したソース言語とターゲット言語に基づいて、AIを使用して即座に翻訳および入力します。 Dictate speech and instantly translate and type it using AI based on your configured source and target languages.
- **アップデートダウンローダーの改善**: アップデートダウンロードダイアログでダウンロードの進捗状況がパーセンテージで正しく表示されるようになり、インストールのキャンセル時に「アップデートをダウンロードしています」という幽霊のようなメッセージが表示されるバグが修正されました。
- **eSpeak-NGダウンローダーの改善**: eSpeak-NGのダウンロードにおけるパーセンテージの進捗追跡を追加しました。
- **一括OCRの復元力**: アクティブなAPIキーが途中でクォータ（上限）に達した場合にプロセスが停止していたバグを修正しました。自動的に次に利用可能なキーに切り替えて処理を再開します。
- **ビジュアルCAPTCHAサポート**: ビジュアルCAPTCHA解決に対する強力なサポートを追加しました。hCaptchaやreCAPTCHAなどの複雑な画像チャレンジを自動的に解決し、困難なウェブフォームでのアクセシビリティを大幅に向上させます。 It attempts to automatically solve complex image challenges like hCaptcha and reCAPTCHA, significantly enhancing accessibility on challenging web forms.
- **Audio Transcriber Overhaul**: The Audio Transcriber module has been completely rebuilt and now supports both audio and video files. It features 3 distinct operation modes: "Transcribe (Original Language)", "Transcribe and Translate (Target Language)", and a new powerful "Dub and Translate (Target Language)" option (exclusive to Gemini) that generates a translated audio dub of the original speech.
- **ドキュメントリーダーのオプショナルなページ番号**: 複数ページドキュメントの出力にページ番号と区切り文字を含めるかどうかを切り替える新しい設定を追加しました。このオプションは、メイン設定から簡単に管理するか、クイック設定レイヤーからその場で切り替えることができます。この機能は、テキスト/HTMLファイルの書き出しとインラインの「整形表示」ウィンドウの両方に適用され、結合されたドキュメントをシームレスに読み上げることを可能にします。 You can easily manage this option from the main settings or toggle it on-the-fly via the Quick Settings layer. This feature applies to both text/HTML file exports and the inline "View Formatted" window, allowing you to read combined documents seamlessly.
- **動画説明のための無制限 Gemini Live TTS**: 動画の同期音声ナレーション（MP3）を生成する際、音声エンジンとして「Gemini Live TTS」を選択できるようになりました。これにより、Gemini Live APIを使用して、文字数や長さの制限なしで高品質な音声解説を合成できます。 This utilizes the Gemini Live API to synthesize high-quality audio descriptions without any character limits or length restrictions.
- **コードベースのモジュール化**: 保守性を向上させるため、単一ファイル構成だったアドオンの構造をマルチファイルのモジュールアーキテクチャにリファクタリングしました。
- **設定UIの再設計**: グループ化されたレイアウトの代わりに、モダンなタブベースのインターフェースを使用するように設定ダイアログを完全に再設計しました。既存のすべてのオプションを維持しながら、より優れた整理と簡単なナビゲーションを提供します。
- **Global & Dedicated File Logging**: Added an optional global file logging system under the new "Advanced" settings tab. Automatically captures operational events, API traffic, and errors across all add-on modules into a dedicated file (`vision_assistant.log`). Supports configurable log verbosity levels (Debug, Info, Warning, Error), automated retention periods (1 hour to 90 days), and direct log opening or clearing from settings with zero performance impact or NVDA log interference.
- **Geminiアップロードの進捗追跡**: 大きなファイル（動画、音声、ドキュメント）をGoogle Gemini APIにアップロードする際、リアルタイムのパーセンテージによる進捗アナウンスを追加しました。

## Changes for 2026.07.15

- **インテリジェントAPIモデルフィルタリング**: ホワイトリスト方式から完全にブラックリスト方式へとモデルフィルタリングシステムを刷新しました。メインのチャットモデルドロップダウンを常にクリーンかつ将来性のある状態に保ちつつ、高度なルーティング（Advanced Routing）セクションですべての特殊モデルにアクセスできるよう、強力なフィルタリングキーワード（`embedding`、`bison`、`gecko`、`audio`、`realtime`、`babbage`、`moderation`、`deep`、`antigravity`、`computer`）を追加しました。 Added stronger filtering keywords (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) to ensure the main chat model dropdown remains perfectly clean and future-proof, while keeping all specialized models accessible in the Advanced Routing section.
- **高度なルーティングの検索機能**: すべての高度なモデルルーティングドロップダウン（OCR、STT、TTS、オペレーター、ビデオ、ライブ）およびeSpeakバリアントセレクターが完全に検索可能になりました。入力を素早く行ってフィルタリングし、希望のモデルやバリアントを簡単に見つけることができます。 You can quickly type to filter and find your desired model or variant.
- **新しいコマンドレイヤーショートカット**:
  - **設定 (`Alt + S`)**: Vision Assistant Proの設定ダイアログを瞬時に開きます。
  - **スマートなAPIクォータ管理**: モデルごとにクォータを追跡することにより、429（日次制限）エラーの処理を強化しました。キーが特定のモデルで日次制限に達した場合、その特定のモデルに対してのみスマートに隔離され、他のモデルでは引き続きキーを使用できるように維持されます。
  - **ルーティング監査 (`Alt + M`)**: 現在の高度なルーティング設定を監査してアナウンスし、特殊なタスクにどのモデルがアクティブに選択されているかを読み上げます（デフォルト設定はスキップされます）。
- **ビデオアナライザーの完全な刷新**: ビデオアナライザーが完全に生まれ変わりました！以前はオンラインビデオの基本的な説明を提供するだけでした。今回の刷新により、視覚障害者向けに調整された包括的なビデオ処理スイートとなりました： Previously, it only provided a basic description of online videos. Now, it is a comprehensive video processing suite tailored for blind users:
  - **Local Screen Recording (`Control+V`)**: You can now record silent videos directly from your screen. The AI will analyze the recorded segment and provide a highly detailed description of the scene, layout, and actions.
  - **音声解説の生成 (SRT)**: ビデオの非常に詳細な音声解説スクリプト（標準のSRT形式）を生成できるようになりました。音声トラックの自然なポーズに解説を賢く配置するスマートなギャップタイミング機能や、画面上のテキストに対する完全一致OCRを備えています。
  - **同期された音声ナレーション (MP3エクスポート)**: テキストベースの字幕を超えて、アドオンが音声解説を合成し、ビデオの元の音声トラックと自動的にミックスし、音声ダッキング（解説中の背景音量の低下）を適用し、最終的に同期された結果をMP3ファイルとしてエクスポートします！
  - **スマートなビデオファイルアクション**: ローカルのビデオファイルにフォーカスしてビデオのショートカットを押すと、アドオンがそれを自動的に検出してファイルを直接処理します。
  - **高度なキャラクター追跡**: AIがキャラクター抽出のプリパス（事前処理）を実行するようになりました。グローバルなキャラクター辞書を構築し、キャラクターの混同なしにセグメントごとに正確にキャラクターを追跡します。 It builds a global character dictionary and tracks characters accurately segment-by-segment without confusing identities.
  - **ビデオ分析の設定**: SRTのチャンクサイズ、キャラクター字幕、および免責事項を制御するための新しい設定を追加しました。
  - **拡張モデルルーティング**: 高度なモデルルーティング設定で、特殊なビデオモデル（`gemini_video_model`、`custom_video_model`）を明示的に選択できるようになりました。
- **Smart API Quota Management**: Enhanced handling of 429 (Daily Limit) errors by tracking quotas per-model. If a key hits its daily limit on one model, it is intelligently quarantined for that specific model only, leaving the key available for use with other models.

## バージョン 4.6 の変更点

- **中断したスキャンの一時停止・再開機能**: ドキュメントリーダーとスマートファイルアクションの両方に再開機能を追加しました。スキャンが中断された場合、最初からやり直すのではなく、停止した場所から継続できるようになりました。 If a scan gets interrupted, you can now continue from where it stopped instead of starting over from scratch.
- **新しい `[screen_fg_obj]` 変数**: 画面全体ではなく、アクティブなフォアグラウンドウィンドウのみのスクリーンショットをキャプチャするためのカスタムプロンプト変数を追加しました。
- **スマートリトライとキーローテーション**: サーバーの一時的な過負荷（「高負荷」や不正な応答など）が発生した場合、アドオンは同じAPIキーで最大5回まで自動的にサイレントリトライを行うようになりました。リトライが失敗した場合は、リスト内の次のAPIキーに自動的に切り替わります。 If the retries fail, it automatically switches to the next API key in your list.
- **スクリーンカーテンの検知**: スクリーンカーテンが有効な場合（常時有効化されているか、ホットキーで一時的に切り替えられているかにかかわらず）、スクリーンショットの撮影を防止するチェック機能を追加しました。警告を発して処理を停止するため、黒い画像を送信してAPIトークンを無駄に消費するのを防ぎます。 It will warn you and stop, preventing you from sending black images and wasting API tokens.
- **ドキュメントリーダーの調整**: PDFの範囲指定ダイアログで、アドオンの設定からデフォルトのターゲット言語が自動的に事前選択されるようになりました。また、リーダーを閉じた際にバックグラウンドタスクが確実にクリーンに停止するように、スレッド処理を改善しました。 Also improved thread handling to make sure background tasks stop cleanly when the reader is closed.
- **MistralネイティブOCR統合**: MistralのネイティブドキュメントOCR APIを統合しました。複数ページのドキュメントは、Mistralの専用 `/v1/ocr` エンドポイントを使用して自動的に結合、アップロード、バッチ処理されます。一方、単一ページの画像は、不要なPDF変換を行わずに直接処理されます [1]。 Multi-page documents are automatically merged, uploaded, and processed in batches using Mistral's specialized `/v1/ocr` endpoint, while single-page images are processed directly without unnecessary PDF conversions [1].
- **動的なカスタムURLハンドラー**: カスタムAPI URLを変更すると、キャッシュされたモデルリストが即座にクリアされ、手動のモデル入力テキストボックスが復元されるようになりました。これにより、標準の `/v1/models` リスティングエンドポイントをサポートしていないカスタムエンドポイント（Cloudflare AI Gatewayなど）との完全な互換性が確保されます。 This ensures full compatibility with custom endpoints (such as Cloudflare AI Gateway) that do not support the standard `/v1/models` listing endpoint.
- **AIオペレーター入力エンジンの刷新**: AIオペレーターの基盤となるマウスおよびキーボードシミュレーションシステムを完全に書き直しました。レガシーの `mouse_event` APIをモダンなWindowsの `SendInput` APIに置き換え、最新のアプリケーション、UAC保護されたウィンドウ、高DPIディスプレイとの互換性を大幅に向上させました。 Replaced the legacy `mouse_event` API with the modern Windows `SendInput` API, bringing significantly higher compatibility with modern applications, UAC-protected windows, and high-DPI displays.
- **ドラッグ＆ドロップ操作の修正**: AIオペレーターでのドラッグ＆ドロップアクションが完全に安定し、信頼性が向上しました。新しいエンジンでは、自然な「イージング」曲線、正確なカーソル位置調整、最適化されたタイミング、およびスマートな「ナッジ」技術を使用し、Windowsやアプリケーションが途中で失敗することなくドラッグ＆ドロップジェスチャを正しく認識して実行できるようにしています。 The new engine uses natural "easing" curves, precise cursor positioning, optimized timing, and a smart "nudge" technique to ensure that Windows and applications correctly recognize and execute drag-and-drop gestures without failing mid-way.
- **マルチモニターサポート**: AIオペレーターがマルチモニター環境を完全にサポートするようになりました。`MOUSEEVENTF_VIRTUALDESK` フラグを使用してすべてのモニター間でマウスの移動とクリックが正しく動作し、ターゲットアプリケーションがどのモニターにあるかに関係なく正確な位置指定が保証されます。 Mouse movements and clicks work correctly across all monitors using the `MOUSEEVENTF_VIRTUALDESK` flag, ensuring accurate positioning regardless of which monitor the target application is on.
- **キーボードシミュレーションの強化**: キーストロークのインジェクションを改善し、「拡張キー」（矢印キー、Home、End、Page Up/Down、Insert、Delete、F1〜F12など）を完全にサポートしました。これにより、AIオペレーターによって送信されるナビゲーションやショートカットコマンドが、すべてのアプリケーションで完璧に動作するようになります。 This ensures that navigation and shortcut commands sent by the AI Operator work flawlessly across all applications.
- **HEIC/HEIF画像サポート**: iPhoneの写真フォーマットのネイティブサポートを追加しました。事前の変換なしで、AIの説明、OCR、またはドキュメント読み取り用に `.heic` および `.heif` ファイルを直接選択できるようになりました。 You can now directly select `.heic` and `.heif` files for AI description, OCR, or Document Reading without prior conversion.

## バージョン 4.5 の変更点

- **Live Assistant**: Added a real-time voice and screen assistant feature, available exclusively for the Google Gemini provider (or Gemini-compatible custom providers). Includes interactive voice and thinking depth customization directly inside the dialog, with automatic reconnection upon changing settings.
- **MiniMax AIプロバイダー**: ミニマックス（MiniMax）を同等のプロバイダーとして統合しました。完全なマルチモーダルサポート（チャット、ビジョン、OCR）、300種類以上の動的音声を使用したカスタムTTS、および出力からの推論ブロック（例: ` thinking... response`）の自動削除を備えています。
- **ドキュメントビューアの翻訳**: 英語以外のNVDAユーザー向けに、Google翻訳へローカライズされた言語名の代わりに標準の2文字の言語コードが確実に送信されるようにすることで、サイレント翻訳エラーを修正しました。
- **PDFバッチスキャン再試行**: PDFドキュメントのバッチスキャン用に、高度に最適化された個別かつサイレントな再試行ロジックを実装し、冗長なアップロードを防ぎ、再試行中の煩わしいエラーポップアップを回避します。
- **ドキュメントビューアの状態**: 長時間のドキュメントスキャン中に、プラグイン全体のステータス（`I` で確認）が「バッチ処理が開始されました」のまま停止してしまうバグを修正しました。
- **スレッドクラッシュの解決**: バックグラウンドスレッドからドキュメントを開く際に発生していた深刻な `IsMain() failed in wxTimerImpl` スレッドアサーションクラッシュを、GUIコールバックキューを `wx.CallAfter` に移行することで修正しました。

## 6.1.2 の変更点

- **重複ラベルの事前チェック**: 単一のラベル付けにおいて、重複チェックが古い座標キーを使用していた問題を修正しました。これにより、NVDAが既存のラベルを読み上げる代わりに、すでにラベル付けされているオブジェクトに対して重複してAIリクエストを送信してしまう問題が解消されました。
- **非Geminiプロバイダー向けドキュメントチャット**: ドキュメントチャット（`on_ask`）における厳密なAPIキーチェックを修正し、OpenAI、Groq、またはローカルのカスタムプロバイダー（Ollamaなど）を使用するユーザーが、ブロックされることなくドキュメントと正常にチャットできるようにしました。
- **高速Chrome OCR翻訳**: Chrome OCR向けの無料かつキー不要の翻訳APIを復元しました。抽出されたテキストの翻訳でGemini AIがバイパスされるようになり、APIクォータの節約と翻訳プロセスの高速化を実現しました。 Translating extracted text now bypasses Gemini AI, saving API quotas and speeding up the translation process.
- **CAPTCHA英数字フィルター**: CAPTCHAソルバーのフィルタリングロジックを修正し、あらゆる状況で非英数字が適切に削除されるようにしました。
- **コマンドレイヤーヘルプの更新**: ヘルプメニューにおけるステータスアナウンスのショートカットを `L` から `I` に修正し、両方のラベル付けコマンド（`L` および `Shift+L`）をリストに追加しました。

## 6.1.1 の変更点

- **Gemma 4 の思考出力の修正**: Gemma 4 モデルにおいて、内部の思考プロセス全体が最終的な応答として表示されてしまったり、思考を無効にすると空の応答になったりする問題を修正しました。アドオンは、最終的なクリーンなテキスト応答のみを正しく分離して抽出するようになりました。 The add-on now correctly isolates and extracts only the final clean text response.
- **ファイル エクスプローラーからのバッチ OCR**: Windows のファイル エクスプローラーで複数の写真や PDF を直接選択し、テキストを抽出したり一括で分析したりできるようになりました。アドオンはサポートされているファイル形式のみを自動的にフィルター処理します。 The add-on will automatically filter and process only the supported file formats.

## バージョン 6.1.0 の変更点

- **Universal Local AI Integration (Setup Local AI)**: Added a new **"Setup Local AI"** button in Custom Provider Settings. **ユニバーサル・ローカルAI統合（ローカルAIのセットアップ）**: カスタムプロバイダー設定に新しい\*\*「ローカルAIのセットアップ」\*\*ボタンを追加しました。これにより、**Ollama**、**LM Studio**、**Jan.ai**、**KoboldCPP**などのローカルAIエンジンを即座に自動設定できるようになりました。
- **Intelligent Local Proxy Bypass**: Rebuilt the connection logic with an advanced proxy bypass mechanism. The add-on is now smart enough to completely bypass Windows system proxies for local loopback connections, ensuring stable local AI connections even when your VPN/TUN-mode is active.
- **Ultra-Stable AI Labeling (v2)**: Replaced absolute screen coordinate keys with an advanced, hybrid **Object Signature** system. **超安定AIラベリング（v2）**: 絶対画面座標キーを、高度でハイブリッドな**オブジェクト署名**システムに置き換えました。ラベルがプログラム上の識別子（UIAの**AutomationId**またはWin32の**ControlID**）とウィンドウ相対座標に依存するようになったため、ウィンドウのリサイズ、移動、モニターの切り替え、スケーリングに対してカスタムラベルが完全に強固になりました。
- **シームレスな自動ラベル移行**: アップグレードは完全に透過的です。初回フォーカス時に、古いレガシーの座標ベースのラベルがバックグラウンドで新しい安定したフィンガープ的フォーマットに自動的に移行され、データの損失は一切ありません。 The add-on will automatically migrate your older legacy coordinate-based labels to the new stable fingerprint format in the background upon first focus, with zero data loss.

## バージョン 3.5.0 の変更点

- **Introducing Semantic AI Labeling**: Users can now permanently label unnamed buttons and icons using AI. Press **L** to label the current navigator object (supporting both Tab focus and object navigation) or **Shift+L** to scan and label the entire application at once.
- **インテリジェントなラベル管理**: カスタムラベルの表示、名前変更、一括削除を行うための、完全にアクセシブルな新しい「ラベル マネージャー」ダイアログを追加しました（ラベルが存在する場合は **Shift+L** でアクセス可能）。
- **直接ファイル分析（ファイルダイアログのバイパス）**: Windows エクスプローラーで PDF や画像ファイルにフォーカスしているかどうかを、アドオンが自動で検出できるようになりました。ハイライトされたファイル上で **F (スマート ファイル アクション)** または **D (ドキュメント リーダー)** を押すと、通常の「開く」ダイアログを完全にバイパスして、即座に処理が実行されます。 Pressing **F (Smart File Action)** or **D (Document Reader)** on a highlighted file will immediately process it, bypassing the standard "Open" dialog entirely.

## 3.1.0 の変更点

- **「なし (テキストレイヤーを抽出)」OCR エンジンの追加**: ユーザーが AI クレジットを消費せずに検索可能な PDF から直接テキストを抽出できるようになり、テキストベースのドキュメントの処理速度とプライバシーが大幅に向上しました。
- **UI エクスプローラーの精度向上**: UI エクスプローラーのプロンプトを改良し、要素の種類 (リスト項目など) の識別精度を向上させました。また、タスクバーや時計などの Windows システムコンポーネントを無視しながら、「(チェック済み)」、「(選択済み)」、「(展開済み)」などの状態を正確に報告できるようになりました。
- **インストールセットアップのリマインダー**: インストール後に通知を表示し、API キーや環境設定を行うための設定メニューへユーザーを誘導するようにしました。

## バージョン 3.0 の変更点

- **AIオペレーターの入力に関する不具合の修正:** 一部のシステムで、テキストの貼り付け時に文字「v」が入力されてしまうバグを修正しました。この修正により、高システム負荷時に発生していたタイミング競合に対処しています。 This fix addresses timing conflicts that occurred during high system load.
- **安定性の向上:** システムのクリップボードが他のアプリケーションによって一時的にロックされている際に、アドオンがクラッシュするのを防ぐため、クリップボード操作に対する堅牢なエラー処理を追加しました。
- **タイミングの最適化:** さまざまなシステム速度での信頼性向上とサードパーティ製クリップボードマネージャーとの互換性改善のため、キーボードイベントの内部遅延を調整しました。

## バージョン 5.5 の変更点（自動化アップデート）

- **AI オペレーター（自律制御 - Shift+A）:** これは v5.5 の最大の目玉機能です受動的なアシスタントから、あなた専用の**AI オペレーター**へと進化しました。画面を説明するだけでなく、実際に操作を引き継ぎます。 Vision Assistant Pro has graduated from being a passive assistant to becoming your personal **AI Operator**. It doesn't just describe the screen—it takes command.
  - _How it works:_ You can now give verbal instructions to operate your PC. For example, in a completely inaccessible application where your screen reader stays silent, you can press **Shift+A** and type: _"Click on the Settings button"_ or _"Find the search field, type 'Latest News' and press enter."_ The AI visually identifies the elements, moves the mouse, and executes the task for you.
  - _パフォーマンスに関する注意:_ この機能は **Gemini 3.0 Flash (Preview)** 向けに最適化されており、非常に高速かつインテリジェントな応答を実現し、複雑な UI レイアウトにも対応します。
  - **⚠️ API 利用に関する警告:** AI オペレーターは正確性を期すために状況を正確に「見る」必要があるため、各ステップで高解像度のスクリーンショットを送信します。頻繁に使用すると、標準的なテキストベースのタスクよりもはるかに速く API の割り当て量を消費しますのでご注意ください。 Please note that frequent use will consume your API quota much faster than standard text-based tasks.
- **Visual UI Explorer (E):** Tired of navigating through "unlabeled buttons"? Press **E** to activate the UI Explorer. The AI will scan the entire window and generate a list of every clickable element it sees—including icons, graphics, and menus. Simply pick an item from the list, and the AI Operator will click it for you. It’s like having an "accessible layer" on top of any app.
- **Context-Aware Smart File Action (F):** The "F" key has been completely overhauled. It no longer assumes you only want OCR. When you select a single image, it now intelligently asks for your intent: you can choose a **Detailed Visual Description** to understand the scene or a **Structured Text Extraction (OCR)** for reading. The menu adapts dynamically based on the file type and your active AI engine.
- **コアの最適化:** アドオンの内部ロジックの徹底的なクリーンアップを実施し、使用されていないレガシー機能や冗長なコードを削除しました。これにより、すべてのユーザーにとってより軽量で高速、かつ信頼性の高い体験が提供されます。 This results in a leaner, faster, and more reliable experience for all users.

## バージョン 5.0 の変更点

- **マルチプロバイダー アーキテクチャ**: Google Gemini に加え、**OpenAI**、**Groq**、**Mistral** の完全なサポートを追加しました。ユーザーは好みの AI バックエンドを選択できるようになりました。 Users can now choose their preferred AI backend.
- **Advanced Model Routing**: Users of native providers (Gemini, OpenAI, etc.) can now select specific models from a dropdown list for different tasks (OCR, STT, TTS).
- **高度なエンドポイント設定**: カスタムプロバイダーのユーザーは、ローカルサーバーやサードパーティサーバーをきめ細かく制御するために、特定の URL やモデル名を手動で入力できるようになりました。
- **スマート機能表示**: 設定メニューおよびドキュメントリーダーの UI は、選択されたプロバイダーに基づいてサポートされていない機能（TTS など）を自動的に非表示にするようになりました。
- **動的なモデル取得**: アドオンがプロバイダーの API から利用可能なモデルリストを直接取得するようになったため、新しいモデルがリリースされ次第、すぐに互換性が確保されます。
- **ハイブリッド OCR & 翻訳**: Chrome OCR 使用時は速度重視で Google 翻訳を使用し、Gemini / Groq / OpenAI エンジン使用時は AI 駆動の翻訳を使用するようにロジックを最適化しました。
- **ユニバーサルな「AI で再スキャン」**: ドキュメントリーダーの再スキャン機能が Gemini に限定されなくなりました。現在アクティブな AI プロバイダーを使用してページを再処理するようになります。 It now utilizes whatever AI provider is currently active to re-process pages.

## 2.7 の変更点

- **インタラクティブな結果の呼び出し:** コマンドレイヤーに **Space** キーを追加しました。「ダイレクト出力」モードが有効な場合でも、チャットウィンドウで最後のAIレスポンスを瞬時に再度開き、追加の質問を行うことができるようになりました。
- **Telegram コミュニティハブ:** NVDA ツールメニューに「公式 Telegram チャンネル」のリンクを追加しました。最新のニュース、機能、リリース情報を素早く確認できます。
- **応答の安定性の向上:** 翻訳、OCR、およびビジョン機能の中核ロジックを最適化し、より信頼性の高いパフォーマンスと、ダイレクト音声出力使用時のよりスムーズなエクスペリエンスを実現しました。
- **インターフェース案内の改善:** 新しい呼び出しシステムや、それがダイレクト出力設定とどのように連携して動作するのかをより分かりやすく説明するように、設定の説明文とドキュメントを更新しました。

## バージョン 5.5.2 の変更点

- **高度なプロンプトマネージャー:** デフォルトのシステムプロンプトのカスタマイズや、ユーザー定義プロンプトの管理（追加、編集、並び替え、プレビューの完全サポート）を行うための専用管理ダイアログを環境設定に追加しました。
- **包括的なプロキシサポート:** ユーザーが設定したプロキシ設定が、翻訳、OCR、音声生成を含むすべてのAPIリクエストに厳密に適用されるようにし、ネットワーク接続の問題を解決しました。
- **自動データ移行:** データの損失なしに、初回起動時に従来のプロンプト設定を堅牢なv2 JSON形式へ自動的にアップグレードするスマートな移行システムを統合しました。
- **互換性の更新 (2025.1):** 安定したパフォーマンスを確保するため、ドキュメントリーダーなどの高度な機能におけるライブラリの依存関係に基づき、必要なNVDAの最小バージョンを2025.1に設定しました。
- **最適化された設定インターフェース:** プロンプト管理を別のダイアログに再整理することで設定インターフェースを効率化し、よりクリーンでアクセシブルなユーザー体験を提供します。
- **プロンプト変数ガイド:** プロンプトダイアログ内に組み込みガイドを追加し、ユーザーが `[selection]`、`[clipboard]`、`[screen_obj]` などの動的変数を容易に識別して使用できるようにしました。

## 4.0.3 の変更点

- **ネットワーク耐性の強化:** 不安定なインターネット接続や一時的なサーバーエラーに対処するための自動再試行メカニズムを追加し、AI からの応答の信頼性を向上させました。
- **画像翻訳ダイアログ:** 翻訳結果専用のウィンドウを導入しました。OCR の結果と同様に、ユーザーは長い翻訳を 1 行ずつ簡単に移動して読むことができるようになりました。**視覚的翻訳ダイアログ:** 翻訳結果専用のウィンドウを新しく導入しました。OCR の結果と同様に、ユーザーは長い翻訳文を 1 行ずつ簡単に移動して読むことができるようになりました。
- **統合されたフォーマット表示:** ドキュメントリーダーの「フォーマット表示」機能により、処理されたすべてのページが、明確なページヘッダー付きの整理された単一のウィンドウに表示されるようになりました。
- **OCR ワークフローの最適化:** 単一ページドキュメントの場合のページ範囲選択を自動的にスキップし、認識プロセスをより高速かつスムーズに行えるようにしました。
- **API の安定性向上:** より堅牢なヘッダーベースの認証方式に変更し、キーローテーションの競合によって発生する可能性があった「すべての API キーが失敗しました (All API Keys failed)」エラーを解消しました。
- **バグ修正:** アドオン終了時の問題や、チャットダイアログにおけるフォーカスエラーなど、いくつかの潜在的なクラッシュを修正しました。

## バージョン 4.0.1 の変更点

- **高度なドキュメントリーダー:** ページ範囲の選択、バックグラウンド処理、および `Ctrl+PageUp/Down` によるスムーズな移動機能を備えた、PDFと画像用の強力な新しいビューアです。
- **新しい「ツール」サブメニュー:** コア機能、設定、およびドキュメントに素早くアクセスできるよう、NVDAの「ツール」メニューの下に専用の「Vision Assistant」サブメニューを追加しました。
- **柔軟なカスタマイズ:** 設定パネルから、お好みのOCRエンジンとTTS音声を直接選択できるようになりました。
- **複数のAPIキーのサポート:** 複数のGemini APIキーのサポートを追加しました。設定で1行に1つのキーを入力するか、カンマで区切って入力できます。 You can enter one key per line or separate them with commas in the settings.
- **代替OCRエンジン:** Gemini APIのクォータ（制限）に達した場合でも、信頼性の高いテキスト認識を確保するための新しいOCRエンジンを導入しました。
- **スマートなAPIキーローテーション:** クォータ制限を回避するため、最も動作が速いAPIキーに自動的に切り替えて記憶します。
- **ドキュメントのMP3/WAV変換:** リーダー内で直接、MP3（128kbps）およびWAV形式の高音質な音声ファイルを生成・保存する機能が統合されました。
- **Instagramストーリーズのサポート:** URLを使用してInstagramストーリーズを説明および分析する機能を追加しました。
- **TikTokのサポート:** TikTok動画のサポートを導入し、クリップの完全な視覚的説明と文字起こしが可能になりました。
- **アップデートダイアログのデザイン刷新:** インストール前にバージョン変更点を明確に読み上げられる、スクロール可能なテキストボックスを備えた新しいアクセシブルなインターフェースを特徴としています。
- **ステータスとUXの統一:** アドオン全体でファイルダイアログを標準化し、リアルタイムの進捗状況を報告する `L` コマンドを強化しました。

## Changes for 3.6.0

- **ヘルプシステム:** コマンドレイヤー内にヘルプコマンド (`H`) を追加し、すべてのショートカットとそれらの機能の一覧に簡単にアクセスできるようにしました。
- **オンライン動画解析:** **Twitter (X)** の動画が含まれるようにサポートを拡張しました。また、より信頼性の高いエクスペリエンスを提供するため、URLの検出と安定性を改善しました。 Also improved URL detection and stability for a more reliable experience.
- **プロジェクトへの貢献:** プロジェクトの将来のアップデートと継続的な成長を支援したいユーザー向けに、任意の寄付ダイアログを追加しました。

## バージョン 2.0 の変更点

\*   \*\*Command Layer:\*\* Introduced a Command Layer system (default: `NVDA+Shift+V`) to group shortcuts under a single master key. For example, instead of pressing `NVDA+Control+Shift+T` for translation, you now press `NVDA+Shift+V` followed by `T`.
\*\*オンライン動画分析:\*\* URLを指定してYouTubeやInstagramの動画を直接分析する新機能を追加しました。

## バージョン 1.5 の変更点

- **ダイレクト出力モード:** チャットダイアログをスキップし、AI の応答を音声で直接聴くことができるオプションを追加しました。より高速でシームレスな操作性を実現します。
- **クリップボード連携:** AIの応答をクリップボードに自動的にコピーする新しい設定を追加しました。

## 1.0 の変更点

- **新規言語:** **ペルシャ語**および**ベトナム語**の翻訳を追加しました。
- **AIモデルの拡充:** ユーザーが無料モデルとレート制限付き（有料）モデルを区別しやすいよう、明確なプレフィックス (`[Free]`、`[Pro]`、`[Auto]`) を付けてモデル選択リストを再編成しました。**Gemini 3.0 Pro** および **Gemini 2.0 Flash Lite** のサポートを追加しました。 Added support for **Gemini 3.0 Pro** and **Gemini 2.0 Flash Lite**.
- **Dictation Stability:** Significantly improved Smart Dictation stability. Added a safety check to ignore audio clips shorter than 1 second, preventing AI hallucinations and empty errors.
- **ファイル処理:** 英語以外の名前を持つファイルのアップロードが失敗する問題を修正しました。
- **プロンプトの最適化:** 翻訳ロジックと構造化された視覚認識（Vision）の結果を改善しました。

## バージョン 2.9 の変更点

- **フランス語とトルコ語の翻訳を追加しました。**
- **整形済み表示:** チャットダイアログに「整形済み表示」ボタンを追加し、会話を見やすいブラウズモードウィンドウで適切なスタイル（見出し、太字、コード）とともに確認できるようにしました。
- **Markdown設定:** 設定に「チャットでMarkdownをクリーンアップする」という新しいオプションを追加しました。このチェックを外すと、チャットウィンドウで生のリッチテキスト構文（`**`、`#` など）を確認できるようになります。 Unchecking this allows users to see raw Markdown syntax (e.g., `**`, `#`) in the chat window.
- **ダイアログ管理:** 「テキストの洗練」やチャットウィンドウが複数回開いてしまったり、正しくフォーカス当たらない問題を修正しました。
- **UX（ユーザーエクスペリエンス）の改善:** ファイルダイアログのタイトルを「開く」に統一し、よりスムーズな操作のために冗長な音声読み上げ（「メニューを開いています...」など）を削除しました。 for a smoother experience.

## バージョン 2.8 の変更点

- イタリア語の翻訳を追加しました。
- **ステータス通知:** アドオンの現在の状態（例：「アップロード中...」、「解析中...」など）をアナウンスする新しいコマンド（`NVDA+Control+Shift+I`）を追加しました。
- **HTML エクスポート:** 結果ダイアログの「コンテンツを保存」ボタンで、見出しや太字などのスタイルを保持した整形済み HTML ファイルとして出力できるようになりました。
- **設定 UI:** アクセシブルなグループ化により、設定パネルのレイアウトを改善しました。
- **新しいモデル:** `gemini-flash-latest` および `gemini-flash-lite-latest` のサポートを追加しました。
- **言語:** サポートする言語にネパール語を追加しました。
- **テキストの洗練メニューのロジック修正:** NVDA のインターフェース言語が英語以外の場合に「テキストを洗練」コマンドが失敗する重大な不具合を修正しました。
- **音声入力（ディクテーション）:** 音声入力がない場合に誤ったテキストが出力されるのを防ぐため、無音検出を改善しました。
- **アップデート設定:** アドオンストアのポリシーに準拠するため、「起動時にアップデートを確認する」をデフォルトで無効にしました。
- コードのクリーンアップ。

## バージョン 7.0.0 の変更点

- 標準準拠性を高めるため、プロジェクト構造を公式の NV Access アドオンテンプレートに移行しました。
- 高負荷時の信頼性を確保するため、HTTP 429（レート制限）エラーに対する自動リトライロジックを実装しました。
- より高い精度と「スマートスワップ」ロジックの適切な処理を実現するため、翻訳プロンプトを最適化しました。
- ロシア語の翻訳を更新しました。

## 2.6 の変更点

- ロシア語の翻訳サポートを追加しました（nvda-ru 氏に感謝いたします）。
- 接続に関するより詳細なフィードバックを提供できるようにエラーメッセージを更新しました。
- デフォルトのターゲット言語を英語に変更しました。

## バージョン 2.5 の変更点

- ネイティブファイル OCR コマンド (`NVDA+Control+Shift+F`) を追加しました。
- 結果ダイアログに「チャットを保存」ボタンを追加しました。
- 完全なローカライゼーション（i18n）サポートを実装しました。
- 音声フィードバックを NVDA のネイティブトーンモジュールに移行しました。
- PDF および音声ファイルの処理を改善するため、Gemini File API に切り替えました。
- 波括弧を含むテキストの翻訳時に発生するクラッシュを修正しました。

## 2.1.1 の変更点

- カスタムプロンプト内で `[file_ocr]` 変数正しく機能していなかった問題を修正しました。

## 2.1 の変更点

- NVDA のノートパソコン用配列やシステムホットキーとの競合を解消するため、すべてのショートカットを `NVDA+Control+Shift` を使用するように標準化しました。

## 2.1 の変更点

- 内蔵自動アップデートシステムを実装しました。
- 以前翻訳したテキストを即座に取得するためのスマート翻訳キャッシュを追加しました。
- チャットダイアログでの結果を文脈に応じて洗練させるための会話メモリを追加しました。
- 専用のクリップボード翻訳コマンド（`NVDA+Control+Shift+Y`）を追加しました。
- ターゲット言語での出力を厳密に強制するようにAIプロンプトを最適化しました。
- 入力テキスト内の特殊文字によって引き起こされるクラッシュを修正しました。

## 5.5.2 での変更点

- 20以上の新しい言語のサポートを追加しました。
- Implemented Interactive Refine Dialog for follow-up questions.
- ネイティブのスマートディクテーション機能を追加しました。
- NVDAの「入力ジェスチャー」ダイアログに「Vision Assistant」カテゴリを追加しました。
- FirefoxやWordなどの特定のアプリケーションにおけるCOMErrorのクラッシュを修正しました。
- サーバーエラーに対する自動再試行メカニズムを追加しました。

## 3.1.0 の変更点

- 初回リリース。
