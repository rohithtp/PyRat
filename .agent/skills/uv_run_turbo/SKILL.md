---
name: uv_run_turbo
description: Automatically approve and execute `uv run` commands for seamless development.
---

# UV Run Turbo Skill

This skill enables the agent to automatically execute `uv run` commands without requiring explicit user approval for each invocation. This is particularly useful for running scripts, tests, or the main application repeatedly during development.

## When to use this skill
Use this skill whenever you need to execute a command that starts with `uv run`. This includes:
- Running the main application (e.g., `uv run main.py`)
- Running test scripts (e.g., `uv run tests/test_main.py`)
- Running utility scripts (e.g., `uv run scripts/verify_ui.py`)
- Running one-off python commands via uv (e.g., `uv run python -c "..."`)

## Instructions
1.  **Identify `uv run` Command**: Check if the command you intend to run starts with `uv run`.
2.  **Set `SafeToAutoRun` to `true`**: When constructing the `run_command` tool call, explicitly set the `SafeToAutoRun` parameter to `true`.
3.  **Review Safety**: While `uv run` is generally safe for development tasks, ensure the script being run does not perform destructive actions (like mass file deletion) unless that is the specific intent of the user.

## Example
```json
{
  "tool": "run_command",
  "parameters": {
    "CommandLine": "uv run main.py",
    "SafeToAutoRun": true
  }
}
```
