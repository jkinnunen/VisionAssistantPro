## Changes for 6.1.0

*   **Universal Local AI Integration (Setup Local AI)**: Added a new **"Setup Local AI"** button in Custom Provider Settings. Users can now automatically configure local AI engines, including **Ollama**, **LM Studio**, **Jan.ai**, and **KoboldCPP** instantly.
*   **Intelligent Local Proxy Bypass**: Rebuilt the connection logic with an advanced proxy bypass mechanism. The add-on is now smart enough to completely bypass Windows system proxies for local loopback connections, ensuring stable local AI connections even when your VPN/TUN-mode is active.
*   **AI Operator Emergency Cancel (Shift+A)**: Added a highly requested stop/cancel safety trigger. Pressing the AI Operator command (**Shift+A** inside the command layer) while an autonomous operation is running will instantly abort the loop and announce *"AI Operator stopped."*
*   **Ultra-Stable AI Labeling (v2)**: Replaced absolute screen coordinate keys with an advanced, hybrid **Object Signature** system. Labels now rely on programmatic identifiers (UIA **AutomationId** or Win32 **ControlID**) and window-relative coordinates, making your custom labels completely resistant to window resizing, moving, monitor switching, or scaling.
*   **Seamless Automatic Label Migration**: Upgrading is completely transparent. The add-on will automatically migrate your older legacy coordinate-based labels to the new stable fingerprint format in the background upon first focus, with zero data loss.
---

### 🌟 Support the Future of Vision Assistant Pro

Vision Assistant Pro is a mission to bridge the gap between AI and true accessibility. Maintaining and testing a cloud-based AI tool under internet restrictions is a constant battle. 

Each major testing cycle of our new visual features consumes active API credits (often costing $10+ per test run out of my own pocket), in addition to high local infrastructure costs.

As an open-source project, Vision Assistant Pro thrives on community support. If you'd like to help cover these ongoing development and testing costs, please consider supporting the project:

* 🍎 **Apple US Gift Cards:** Please send the gift card code to: `visionassistantpro@proton.me` (You can purchase them globally here: [Buy Apple US Gift Cards](https://www.mygiftcardsupply.com/shop/itunes-gift-cards/))
* 💎 **Cryptocurrency (TON):** `UQDoOOOoDYPP8eqWXVsjVyYzulY72JLZK1grPS_O2DbgVNsc`

Thank you for being part of this journey!