---
name: human_verified_commit
description: strict protocol ensuring human approval for version control commit and push operations.
---

# Human Verified Commit Skill

This skill mandates that all version control "commit" and "push" operations require explicit human verification. This ensures that no code is permanently recorded or sent to a remote repository without the user's consent.

## When to use this skill
Use this skill whenever you are about to:
- Commit changes (git, jj, svn, etc.).
- Push changes to a remote repository.
- Force push or rewrite history.

## Instructions
1.  **Set `SafeToAutoRun` to `false`**: For ANY command involving `commit`, `push`, `upload`, or `publish`, you MUST set the `SafeToAutoRun` parameter to `false`.
2.  **Ask for Confirmation**: Before executing the tool call, or effectively *by* setting `SafeToAutoRun: false`, you ensure the user sees the command and must manually click "Approve" (or equivalent) in their interface.
3.  **Review Changes**: Briefly summarize what is being committed before invoking the command.

## Example
**Correct Usage for Commit:**
```json
{
  "tool": "run_command",
  "parameters": {
    "CommandLine": "jj commit -m \"feat: update layout logic\"",
    "SafeToAutoRun": false
  }
}
```

**Correct Usage for Push:**
```json
{
  "tool": "run_command",
  "parameters": {
    "CommandLine": "jj git push",
    "SafeToAutoRun": false
  }
}
```
