# Installation Guide

First-time setup for the **pytest + Playwright** framework.

## Prerequisites

- Python 3.9 or newer (`python --version`)
- Git

## 1. Clone the repository

```bash
git clone <repository-url>
cd pytest_playwright
```

## 2. Create and activate a virtual environment

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> If activation is blocked, allow scripts for the current user once:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Windows (Command Prompt)

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## 5. Install Playwright browsers

This downloads the browser binaries required by Playwright:

```bash
playwright install
```

To install only a specific browser (optional):

```bash
playwright install chromium
```

## 6. Install the IDE plugin for `.feature` files

`pytest-bdd` (installed in step 4) only **runs** the Gherkin scenarios. The cucumber icon,
syntax highlighting, and step navigation are provided by an **IDE plugin** and cannot be
installed with pip, so each IDE needs its own one-time install.

### PyCharm

Gherkin support is **not bundled** with PyCharm (any edition), so install it manually:

**Settings** (`Ctrl + Alt + S`) **→ Plugins → Marketplace** tab → search and install:

| Plugin | Publisher | Purpose |
|--------|-----------|---------|
| **Gherkin** (plugin id `gherkin`) | JetBrains | `.feature` file type, cucumber icon, Gherkin syntax highlighting, step definition assistance |

Then restart PyCharm.

- For Ctrl+Click navigation from a step to its Python function, set
  **Settings → Languages & Frameworks → BDD → Preferred BDD framework** to **pytest-bdd**
  (this navigation is a PyCharm Professional feature).
- If the icon is still generic afterwards, check **Settings → Editor → File Types**: select
  **Gherkin** and make sure `*.feature` is listed under **Registered Patterns** (and not
  claimed by **Text**). Alternatively right-click the file → **Override File Type** →
  **Gherkin**.

### Cursor / VS Code

| Extension | Extension id | Purpose |
|-----------|--------------|---------|
| **Material Icon Theme** | `PKief.material-icon-theme` | Cucumber icon for `.feature` files (the default Seti theme has no `.feature` mapping) |
| **Cucumber (Gherkin) Full Support** | `alexkrechik.cucumberautocomplete` | Gherkin syntax highlighting, step autocomplete, step navigation |

```powershell
cursor --install-extension PKief.material-icon-theme
cursor --install-extension alexkrechik.cucumberautocomplete
```

Both are already configured in `.vscode/settings.json`; see [CURSOR.md](CURSOR.md) for
details.

## 7. Verify the installation

```bash
pytest --version
playwright --version
```

## 8. Run the tests

```bash
pytest -s
```

Run in headed mode (visible browser):

```bash
pytest -s --headed
```

Run against a specific browser:

```bash
pytest -s --headed --browser_name firefox
```

Run in parallel across CPU cores (via `pytest-xdist`):

```bash
pytest -n auto   # one worker per CPU core
pytest -n 3      # use a specific number of workers
```

Generate an HTML report (via `pytest-html`):

```bash
pytest --html=report.html --self-contained-html
```

Run BDD scenarios written in Gherkin (via `pytest-bdd`):

```bash
pytest --gherkin-terminal-reporter   # show Given/When/Then steps in the output
```

> `pytest-bdd` only runs the scenarios - editor support for `.feature` files comes from the
> IDE plugin installed in step 6.

Record a Playwright trace (saved to `test-results/<test-name>/trace.zip`):

```bash
pytest --tracing on
```

Combined example (browser, marker, parallel, tracing, HTML report):

```bash
pytest --browser_name chrome -m full -n auto --tracing on --html=report.html
```

View a trace locally, or open [trace.playwright.dev](https://trace.playwright.dev/) and
drag-and-drop the `trace.zip` onto the page:

```bash
playwright show-trace test-results/<test-name>/trace.zip
```

## Deactivate the virtual environment

When you are finished working:

```bash
deactivate
```
