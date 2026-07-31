# BDD Execution

How to run and extend the **pytest-bdd** scenarios in this folder. For setup
(venv, dependencies, IDE plugins), see [INSTALL.md](INSTALL.md).

Run all commands from the **project root** so `conftest.py` and imports resolve.

## Two step-definition approaches

The same `orderTransaction.feature` is implemented twice so you can compare how
state is passed between steps.

Both step modules bind the **same** feature. Run **one file at a time** (not
`pytest BDD/test/` for both), or pytest-bdd will register duplicate steps and collect
the scenario twice.

### 1. `shared_data` dict — `test_OrderBdd_test.py`

A pytest fixture returns a mutable dict. Each step reads/writes keys on it
(`order_id`, `login_page`, `dashboard_page`, …).

```python
@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_order(playwright, username, password, shared_data):
    ...
    shared_data['order_id'] = order_id

@when('select the orderId')
def select_order_id(shared_data):
    order_details = shared_data['order_history'].select_order_from_history_and_details(
        shared_data['order_id']
    )
    shared_data['order_details'] = order_details
```

**Pros:** Explicit bag of state; easy to see every key.  
**Cons:** Manual get/set; typos in key names fail at runtime.

### 2. `target_fixture` — `test_OrderBdd_testWithtargetFixtureSolution.py`

Each step declares `target_fixture='...'` and **returns** a value. pytest-bdd
exposes that return value as a normal pytest fixture for later steps.

```python
@given(parsers.parse('place the item order with {username} and {password}'),
       target_fixture='order_id')
def place_order(playwright, username, password):
    ...
    return order_id

@when('select the orderId', target_fixture='order_details')
def select_order_id(order_history, order_id):
    return order_history.select_order_from_history_and_details(order_id)

@then('order message is successfully displayed')
def order_message(order_details):
    order_details.verify_order_message()
```

**Pros:** Native fixture wiring; no shared dict; clearer dependencies in the function signature.  
**Cons:** Fixture names must stay consistent across steps.

| | `shared_data` | `target_fixture` |
|--|---------------|------------------|
| File | `test_OrderBdd_test.py` | `test_OrderBdd_testWithtargetFixtureSolution.py` |
| How state moves | Dict keys | Return value → named fixture |
| Later steps inject | `shared_data` | `order_id`, `login_page`, `dashboard_page`, … |

## Run commands

### Run one approach (recommended)

```bash
# shared_data approach
pytest BDD/test/test_OrderBdd_test.py -s

# target_fixture approach
pytest BDD/test/test_OrderBdd_testWithtargetFixtureSolution.py -s
```

### Run by scenario name (`-k`)

Point `-k` at a **single** step file so the feature is not collected twice:

```bash
pytest BDD/test/test_OrderBdd_test.py -k verify_order -s
pytest BDD/test/test_OrderBdd_testWithtargetFixtureSolution.py -k verify_order -s
```

### Show Given / When / Then in the terminal

```bash
pytest BDD/test/test_OrderBdd_test.py --gherkin-terminal-reporter -s
pytest BDD/test/test_OrderBdd_testWithtargetFixtureSolution.py --gherkin-terminal-reporter -s
```

### Useful options (same as the rest of the suite)

```bash
pytest BDD/test/test_OrderBdd_test.py --browser_name chrome -s
pytest BDD/test/test_OrderBdd_test.py --tracing on
pytest BDD/test/test_OrderBdd_test.py --html=report.html --self-contained-html
```

### PyCharm

1. Open either step file under `BDD/test/` (or the `.feature` file if Gherkin is installed).
2. Use the green gutter **Run** icon, or right-click → **Run 'pytest in …'**.
3. Interpreter must be the project `.venv`.

## Current scenario

**Feature:** `orderTransaction.feature`  
**Scenario Outline:** Verify Order success message shown details page

Flow:

1. **Given** place an order via API (`APIUtils.create_order`) with example credentials  
2. **And** open the login page (`context_setup` fixture)  
3. **When** log in and open the dashboard  
4. **And** navigate to Orders  
5. **And** select the created order id  
6. **Then** assert the success message on the order details page  

Examples table credentials must match keys expected by the API helper
(`userEmail` / `UserPassword` are built in the step from `<username>` / `<password>`).

## Adding a new scenario

1. Add or edit a `.feature` file under `BDD/features/`.
2. Bind it from a `test_*.py` under `BDD/test/`:

```python
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/yourFeature.feature')
```

3. Implement every step with a matching decorator. The step text must match the
   feature **exactly** (no stray punctuation after `Given` / `When` / `Then`).

Choose one state style:

```python
# shared_data
@given(parsers.parse('place the item order with {username} and {password}'))
def place_order(..., shared_data):
    shared_data['order_id'] = ...

# target_fixture
@given(parsers.parse('place the item order with {username} and {password}'),
       target_fixture='order_id')
def place_order(...):
    return order_id
```

4. Reuse existing fixtures (`context_setup`, `playwright`) and page objects where possible.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `StepDefinitionNotFoundError` | Step text in `.feature` must match the `@given`/`@when`/`@then` string exactly (watch for extra `:` or spaces after the keyword). |
| Duplicate steps / scenario collected twice | Do not run both step files together; each binds the same feature. Run one file at a time. |
| `KeyError: 'userEmail'` | Pass `{"userEmail": ..., "UserPassword": ...}` into `APIUtils`, not `username`/`password`. |
| `KeyError` on `shared_data[...]` | A previous step did not set that key, or the key name is misspelled. |
| Fixture not found (`order_id`, `login_page`, …) | With `target_fixture`, the producing step must `return` the value and use the same fixture name later steps request. |
| Imports fail (`pageObjects`, `utils`) | Run pytest from the **project root**, not from inside `BDD/`. |
| Browser executable missing | From the project root: `playwright install` (with the same `.venv` activated). See [INSTALL.md](INSTALL.md). |
| No cucumber icon / no highlighting | Install the IDE Gherkin/Cucumber plugin; see [INSTALL.md](INSTALL.md). |
