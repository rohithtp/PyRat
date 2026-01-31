---
name: jj_commit_push
description: Commit and push changes using Jujutsu (jj)
---

# JJ Commit and Push

This skill handles committing and pushing changes using the Jujutsu (jj) version control system.

## Instructions

1.  **Describe the current change**:
    Use `jj describe -m "<message>"` to describe the changes you have made. Please ensure the message is descriptive of the changes.

2.  **Create a new change**:
    Use `jj new` to finalize the current change and start a new one on top of it. This effectively "commits" the previous change.

3.  **Push to remote**:
    Use `jj git push` to push the changes to the configured git remote.

## Example Usage

When you are ready to save your work and push it:

```bash
jj describe -m "feat: implement new login flow"
jj new
jj git push
```
