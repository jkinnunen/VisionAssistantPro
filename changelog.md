## Changes for 5.5.2

*   **Fixed AI Operator Typing Issue:** Resolved a bug where the letter 'v' was typed instead of pasting text on certain systems. This fix addresses timing conflicts that occurred during high system load.
*   **Enhanced Stability:** Added robust error handling for clipboard operations to prevent addon crashes when the system clipboard is temporarily locked by other applications.
*   **Timing Optimization:** Adjusted internal delays for keyboard events to ensure higher reliability across different system speeds and better compatibility with third-party Clipboard Managers.