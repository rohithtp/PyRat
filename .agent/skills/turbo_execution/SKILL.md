---
name: turbo_execution
description: Accelerate development by automatically approving and running safe commands within the conversation.
---

# Turbo Execution Skill

This skill allows the agent to auto-execute standard development commands to speed up the workflow, reducing the need for manual user approval for every step.

## When to use this skill
Use this skill when performing iterative development tasks such as:
- Running the application (e.g., `uv run main.py`).
- Running tests.
- Listing files or directories.
- Reading file contents.
- Installing dependencies (if consistent with the project).
- Creating/editing files (via tool calls, though `run_command` is the focus here).

## Instructions
1.  **Set `SafeToAutoRun` to `true`**: When using the `run_command` tool for the tasks listed above, explicitly set the `SafeToAutoRun` parameter to `true`.
2.  **Context Awareness**: Ensure the command is relevant to the current task and does not destroy significant data without backup.
3.  **Exception**: Do **NOT** auto-run commands that push changes to a remote repository or perform irreversible system deletions, unless explicitly covered by another instruction override. 

## Example
```json
{
  "tool": "run_command",
  "parameters": {
    "CommandLine": "uv run tests/test_main.py",
    "SafeToAutoRun": true
  }
}
```
