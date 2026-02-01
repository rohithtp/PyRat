---
name: ui_verification
description: Verify that the UI implementation matches the specifications in README.md, MANIFEST.md, and CAPABILITY.md.
---

# UI Verification Skill

This skill guides the verification of the User Interface (UI) to ensure it aligns with the project's documentation and capability requirements.

## When to use this skill
Use this skill after making changes to the UI code (`main.py` or rendering logic) to confirm that the changes verify against the expected behavior described in:
- `README.md` (General description and screenshots/layout)
- `MANIFEST.md` (Design philosophy and specific visual elements)
- `CAPABILITY.md` (Functional requirements and detailed component breakdown)

## Instructions

### 1. Analysis
First, read the reference documents to extract the *expected* state:
- **Header**: What title? What controls? What style/color?
- **Body**: What monitors are expected (CPU, RAM)? What widgets (Sparkline, Gauge)? Colors?
- **Footer**: What text? Exit instructions?

### 2. Code Verification
Inspect the source code (`main.py`) to verify:
- **Structure**: Does the layout split match the documentation (e.g., Stacked Header/Body/Footer)?
- **Components**: Are the correct widgets (`Paragraph`, `Sparkline`, `Gauge`) used?
- **Styles**: Do the colors and modifiers (`Color.Cyan`, `Color.Green`, `Bold`) match the descriptions?
- **Logic**: Is the data being updated in `on_tick`?

### 3. Runtime Verification
Since the agent cannot "see" the terminal output directly, perform a **Headless Verification** or **Smoke Test**:

1.  **Create a Verification Script**: Write a temporary Python script that imports the rendering logic and runs it with a `TestBackend` or simply runs it for a few seconds to check for crashes.
    *   *Note*: If `ratatui` python bindings support inspection of the buffer, use that.
    *   *Alternative*: Run `uv run main.py` with `WaitMsBeforeAsync` set to a few seconds, then send 'q' to quit, checking ensuring exit code 0 or 130 (not 1 or 139).

2.  **Check Logs**: If debug logging is available, verify that render cycles are occurring and dimensions are correct.

### 4. Checklist Comparison
Compare findings against the docs:
- [ ] Header Title matches `MANIFEST.md`?
- [ ] Colors match `CAPABILITY.md` (e.g., Cyan Header, Green CPU)?
- [ ] Footer instructions match `README.md`?
- [ ] No crashes on startup (Layout logic valid)?

## Example Verification Script Pattern
```python
# scripts/verify_layout.py
from main import render, PyRatState, on_start
from ratatui import Terminal, Rect

# Mock terminal or strict layout check
# ...
```
