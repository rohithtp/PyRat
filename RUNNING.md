# 🚀 Running PyRat

This guide provides step-by-step instructions on how to set up and run **PyRat** locally.

## Prerequisites

- **Python 3.x** installed on your system.
- **uv** (fast Python package installer and runner).

### Installing uv

If you don't have `uv` installed, you can install it via:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*(See [astral.sh/uv](https://astral.sh/uv) for more details)*

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd PyRat
    ```

2.  **Sync dependencies:**
    This command creates the virtual environment and installs all necessary packages defined in `pyproject.toml`.
    ```bash
    uv sync
    ```

    > **Note:** `uv sync` automatically creates and manages a `.venv` directory for you. You don't need to manually verify or activate it when using `uv run`.

## ⚓ Execution

To launch the PyRat system monitor:

```bash
uv run main.py
```

## ⌨️ Controls

- **q**: Quit the application.
- **Ctrl+C**: Force exit.
