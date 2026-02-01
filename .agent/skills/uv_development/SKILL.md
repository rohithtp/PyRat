---
name: uv_development
description: Use uv for Python development tasks (running code, managing dependencies, environment setup)
---

# UV Development Skill

This skill provides instructions on how to use `uv` for Python development tasks. `uv` is a fast Python package installer and resolver.

## When to use this skill
Use this skill whenever you need to:
- Run Python scripts or the application.
- Install or remove dependencies.
- Initialize new Python projects.
- Manage virtual environments.

## Common Commands

### 1. Running Code
Instead of `python main.py` or `./.venv/bin/python main.py`, use `uv run`:

```bash
uv run main.py
```

To run a module:
```bash
uv run -m my_module
```

To run an arbitrary command in the environment:
```bash
uv run -- python -c "import sys; print(sys.executable)"
```

### 2. Managing Dependencies
To add a new package (e.g., `requests`):
```bash
uv add requests
```

To add a development dependency (e.g., `pytest`):
```bash
uv add --dev pytest
```

To remove a package:
```bash
uv remove requests
```

### 3. Environment Management
To create/sync the virtual environment (install all dependencies from `pyproject.toml`):
```bash
uv sync
```

To create a new project:
```bash
uv init
```

## Best Practices
- **Do not** manually run `source .venv/bin/activate`. Use `uv run` which handles environment activation automatically.
- **Do not** use `pip install` directly if you are managing a project with `pyproject.toml`. Use `uv add` to ensure `pyproject.toml` and `uv.lock` are updated.
- `uv` automatically manages the `.venv` directory.
