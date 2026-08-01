# Installing Claude Code

Guide to install and configure **Claude Code** (Anthropic CLI + IDE plugins) for
this **pytest + Playwright** project. For the project itself (venv, dependencies,
browsers), see [INSTALL.md](INSTALL.md). For Cursor IDE setup, see [CURSOR.md](CURSOR.md).

Official docs: [Install Claude Code](https://code.claude.com/docs/en/install) ·
[JetBrains plugin](https://code.claude.com/docs/en/jetbrains)

## Prerequisites

- **OS:** Windows 10 (1809+) / Windows Server 2019+, macOS 13+, or a supported Linux distro
- **Hardware:** 4 GB+ RAM (x64 or ARM64)
- **Account:** a paid Claude plan (Pro, Max, Team, or Enterprise) or a Claude Console account  
  (the free Claude.ai plan does not include Claude Code)
- **Git** recommended (on Windows, [Git for Windows](https://git-scm.com/downloads/win) enables the Bash tool; without it Claude Code uses PowerShell)
- Internet connection for install and login

Node.js is **not** required for the native installer.

## 1. Install the CLI (native — recommended)

### Windows (PowerShell)

Use a **64-bit** PowerShell window (prompt shows `PS C:\...`):

```powershell
irm https://claude.ai/install.ps1 | iex
```

### Windows (CMD)

```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

> If you see `The token '&&' is not a valid statement separator`, you are in PowerShell — use the PowerShell command instead.  
> If `'irm' is not recognized`, you are in CMD — use the CMD command.

### macOS / Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Alternative package managers

```powershell
# Windows WinGet (does not auto-update — run upgrade periodically)
winget install Anthropic.ClaudeCode
winget upgrade Anthropic.ClaudeCode
```

```bash
# macOS Homebrew
brew install --cask claude-code
brew upgrade claude-code
```

Native installs auto-update in the background. WinGet/Homebrew do not.

Default binary location on Windows:

```
C:\Users\<you>\.local\bin\claude.exe
```

## 2. Fix `PATH` (Windows)

If the installer reports that `C:\Users\<you>\.local\bin` is not on your `PATH`, add it permanently:

```powershell
$claudePath = "$env:USERPROFILE\.local\bin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")

if (($userPath -split ";") -notcontains $claudePath) {
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$userPath;$claudePath",
        "User"
    )
}
```

Open a **new** terminal (or refresh the current session):

```powershell
$env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
            [Environment]::GetEnvironmentVariable("Path", "User")
```

Verify:

```powershell
Get-Command claude
claude --version
```

Or call the binary directly (works even before `PATH` is fixed):

```powershell
& "$env:USERPROFILE\.local\bin\claude.exe" --version
```

## 3. Log in and start Claude Code

From the **project root** (`pytest_playwright_with_bdd`):

```powershell
claude
```

The first run opens a browser login. After that, Claude Code starts an interactive session in the terminal.

Useful checks:

```powershell
claude --version
claude doctor
```

## 4. PyCharm / JetBrains plugin

The JetBrains plugin does **not** bundle the CLI — install the CLI first (steps 1–3).

1. **Settings → Plugins → Marketplace** → install **Claude Code [Beta]**  
   ([Marketplace plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-))
2. Restart PyCharm completely.
3. Open Claude with **Ctrl+Esc** (Windows/Linux) or the Claude Code button, or run `claude` in the IDE terminal.

If the plugin cannot find `claude` (stale IDE `PATH`), set the full path:

**Settings → Tools → Claude Code [Beta] → Claude command**

```
C:\Users\<you>\.local\bin\claude.exe
```

**Apply → OK**, then fully quit PyCharm (and JetBrains Toolbox from the tray if you use it) and reopen.

| Shortcut | Action |
|----------|--------|
| `Ctrl+Esc` | Open Claude Code from the editor |
| `Alt+Ctrl+K` | Insert a file reference (`@path#L…`) |

From an external terminal connected to the project, you can also run `claude` then `/ide` to attach to PyCharm.

### Remote Development

Install the plugin on the **remote host** (**Settings → Plugin (Host)**), not only on the local client.

## 5. Optional: Desktop app

Prefer a GUI without the terminal? Install the [Claude Desktop app](https://claude.com/download) for Windows/macOS. The CLI above is what the JetBrains/VS Code plugins launch.

## 6. Use Claude with this project

1. Complete project setup: [INSTALL.md](INSTALL.md) (venv, `pip install -r requirements.txt`, `playwright install`).
2. Open the repo root in PyCharm (or your IDE).
3. Start Claude from that root so it sees `conftest.py`, `BDD/`, `pageObjects/`, etc.
4. Example prompts:
   - “Run the BDD order scenario and fix any step mismatches.”
   - “Explain how `context_setup` launches the browser.”
   - “Add a new Gherkin scenario under `BDD/features/` using `target_fixture`.”

BDD-specific docs: [BDD/INSTALL.md](../BDD/INSTALL.md) · [BDD/EXECUTION.md](../BDD/EXECUTION.md).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `claude` is not recognized | Add `%USERPROFILE%\.local\bin` to User `PATH`, open a new terminal, or set the full path in the PyCharm plugin |
| Installer fails (`403`, curl HTML error) | See [Troubleshoot installation](https://code.claude.com/docs/en/troubleshoot-install); try WinGet/`winget install Anthropic.ClaudeCode` |
| Wrong shell for install command | PowerShell uses `irm … \| iex`; CMD uses `curl … install.cmd` |
| “Raw mode is not supported” | Do not run the interactive CLI in Git Bash; use PowerShell or CMD |
| Claude icon in PyCharm does nothing | Install CLI first; set **Claude command** to the full `claude.exe` path; restart IDE (and Toolbox) |
| ESC does not interrupt Claude in PyCharm | **Settings → Tools → Terminal** → uncheck “Move focus to the editor with Escape” |
| Login / plan errors | Need a paid Claude plan or Console account; see [authentication docs](https://code.claude.com/docs/en/authentication) |
| WSL + JetBrains “No available IDEs” | Prefer mirrored networking or firewall rules — see [JetBrains WSL notes](https://code.claude.com/docs/en/jetbrains#wsl-configuration) |
