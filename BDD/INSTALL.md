# BDD Installation

Setup for the **pytest-bdd** scenarios in this folder. For run commands and
step-definition approaches, see [EXECUTION.md](EXECUTION.md).

Complete the main project setup in
[Documentation/INSTALL.md](../Documentation/INSTALL.md) first (venv,
`requirements.txt`, Playwright browsers).

## Folder layout

```
BDD/
├── INSTALL.md                                            # this file
├── EXECUTION.md                                          # how to run and extend scenarios
├── features/
│   └── orderTransaction.feature                          # Gherkin scenarios
└── test/
    ├── test_OrderBdd_test.py                             # shared_data dict approach
    └── test_OrderBdd_testWithtargetFixtureSolution.py    # target_fixture approach
```

| Path | Role |
|------|------|
| `BDD/features/*.feature` | Gherkin Feature / Scenario / Scenario Outline |
| `BDD/test/test_*.py` | Python step definitions (`@given` / `@when` / `@then`) |
| Project root `conftest.py`, `pageObjects/`, `utils/` | Shared fixtures and page objects used by the steps |

The `scenarios('../features/orderTransaction.feature')` call in each test file is
**relative to that test file**, not the project root.

## Prerequisites

- Python 3.9+ and an activated project `.venv`
- Dependencies from the project root, including `pytest-bdd`:

```bash
pip install -r requirements.txt
playwright install
```

`pytest-bdd` is listed in `requirements.txt` (`pytest-bdd>=8.0.0`).

## IDE support for `.feature` files

`pytest-bdd` only **runs** scenarios. Editor highlighting and step navigation need an IDE plugin.

### PyCharm

**Settings → Plugins → Marketplace** → install **Gherkin** (JetBrains, plugin id `gherkin`).

Optional (PyCharm Professional): **Settings → Languages & Frameworks → BDD → Preferred BDD framework** = **pytest-bdd**.

### Cursor / VS Code

```powershell
cursor --install-extension PKief.material-icon-theme
cursor --install-extension alexkrechik.cucumberautocomplete
```

See [Documentation/INSTALL.md](../Documentation/INSTALL.md) step 6 and
[Documentation/CURSOR.md](../Documentation/CURSOR.md) for details.

## Next step

After install is complete, follow [EXECUTION.md](EXECUTION.md) to run the scenarios.
