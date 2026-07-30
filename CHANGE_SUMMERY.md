# Change Summary

- 2026-07-29 18:42 — Documented tracing execution in `README.md`, `Documentation/INSTALL.md`, and `Documentation/CURSOR.md`: added the `--tracing on` usage, the combined example (`pytest --browser_name chrome -m full -n auto --tracing on --html=report.html`), and how to view a `trace.zip` locally or via drag-and-drop at trace.playwright.dev.
- 2026-07-29 18:04 — Removed the redundant `os.makedirs` before `context.tracing.stop()` in `conftest.py`; verified that Playwright's `tracing.stop(path=...)` auto-creates the parent directories.
- 2026-07-29 17:58 — Added Playwright tracing to the `context_setup` fixture in `conftest.py`: when `--tracing on` (or `retain-on-failure`) is passed, it records the test's own context and saves `test-results/<test-name>/trace.zip`. Verified a real 5.4MB trace is produced.
- 2026-07-29 15:03 — Improved `get_token` in `utils/api_base.py`: replaced the bare `assert response.ok` with an assertion message that includes the user email, HTTP status, and response body, so login-API failures report the actual cause.
- 2026-07-29 14:24 — Added `pytest-html` to `requirements.txt` and documented HTML report generation (`pytest --html=report.html --self-contained-html`) in `README.md`, `Documentation/INSTALL.md`, and `Documentation/CURSOR.md`.
- 2026-07-29 14:00 — Documented running with a specific number of parallel workers (`pytest -n 3`) in `README.md`, `Documentation/INSTALL.md`, and `Documentation/CURSOR.md`.
- 2026-07-29 13:55 — Added `pytest-xdist` to `requirements.txt` and documented parallel test runs (`pytest -n auto` / `-n N`) in `README.md`, `Documentation/INSTALL.md`, and `Documentation/CURSOR.md`.
- 2026-07-29 12:40 — Added a "Run by partial name" section to `README.md` documenting `pytest -k` (e.g. `pytest -k create`), including combined expressions.
- 2026-07-29 12:17 — Expanded the "Running Tests" section in `README.md` with run-by-marker options (`smoke`/`full`), custom `--browser_name`/`--url` options, and useful flags (`--co`, `--markers`, `-k`).
- 2026-07-29 12:11 — Added `pytest.ini` registering the custom `smoke` and `full` markers to remove `PytestUnknownMarkWarning` warnings.
- 2026-07-29 11:58 — Fixed `TypeError: list indices must be integers or slices, not str` in `test_e2e_framework_web_api_create_order.py`: passed a single user credential (`user_credentials_params[1]`) to `create_order`/`get_token` instead of the entire list.
- 2026-07-29 11:13 — Made the `--browser_name` and `--url` defaults in `conftest.py` load from `data/execution_data.json` (path resolved relative to `conftest.py`). Fixed the `browser` value in the JSON (was a URL, now `chrome`).
- 2026-07-29 00:32 — Added `CURSOR.md` with full instructions to set up and run the project in Cursor (Python extension, venv, dependencies, interpreter selection, pytest config, running/debugging tests, custom `--browser_name` option, and troubleshooting).
- 2026-07-29 00:29 — Added `.vscode/settings.json` to enable pytest test discovery and inline Run/Debug gutter buttons in Cursor, and set the default interpreter to the project `.venv`.
- 2026-07-29 00:10 — Added `INSTALL.md` with first-time installation instructions, including virtual environment setup (Windows PowerShell/CMD and macOS/Linux), dependency install, Playwright browser install, and test run commands.
- 2026-07-29 00:07 — Added `requirements.txt` listing the project dependencies (`pytest`, `playwright`, `pytest-playwright`) derived from the project's imports.
- 2026-07-29 00:02 — Reformatted `README.md` into structured Markdown with headings and fenced code blocks (content preserved, no code logic changed).
