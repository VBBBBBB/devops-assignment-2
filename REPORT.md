# Assignment 2: Continuous Integration Using GitHub Actions - Lab Report

## 1. Introduction & GitHub Actions Core Components

Continuous Integration (CI) is a foundational DevOps practice that automates the building, testing, and validation of code changes as soon as they are pushed to a shared repository.

### Key Components of GitHub Actions
1. **Workflow**: An automated configurable process made up of one or more jobs defined in a YAML file under `.github/workflows/`.
2. **Event**: A specific activity that triggers the workflow (e.g., `push` to `main`, `pull_request`).
3. **Job**: A set of steps executed on the same runner. Jobs can run sequentially or in parallel.
4. **Step**: An individual task within a job (e.g., running a shell command or calling an Action).
5. **Runner**: The compute engine / virtual machine executing the workflow (e.g., `ubuntu-latest`).
6. **Action**: A reusable extension/component that performs common repetitive tasks (e.g., `actions/checkout@v4`, `actions/setup-python@v5`).

---

## 2. Project & Workflow Specification

### File: `.github/workflows/ci.yml`
```yaml
name: Continuous Integration Workflow

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    name: Build & Run Automated Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository code
        uses: actions/checkout@v4

      - name: Set up Python runtime
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Execute automated unit tests
        run: |
          pytest -v --tb=short
```

---

## 3. Demonstration of Failed & Fixed CI Workflows

### Phase 1: Intentional Failure
- **Test Introduced in `test_calculator.py`**:
  ```python
  def test_intentional_failure():
      assert add(2, 2) == 5, "Intentional failure for CI demonstration"
  ```
- **Commit**: `cb33d5b` - *"feat: initial setup with intentional failing test for CI demonstration"*
- **Result in GitHub Actions**:
  - The job `build-and-test` fails at step `Execute automated unit tests`.
  - Pytest catches `AssertionError: Intentional failure for CI demonstration`.
  - Workflow status turns **Red (Failed / ❌)**.

### Phase 2: Correction & Verification
- **Fix Applied in `test_calculator.py`**:
  ```python
  def test_intentional_failure():
      assert add(2, 2) == 4
  ```
- **Commit**: *"fix: resolve intentional test failure to achieve green CI build"*
- **Result in GitHub Actions**:
  - All unit tests pass with `5 passed in 0.0X seconds`.
  - Workflow status turns **Green (Passed / ✅)**.

---

## 4. Best Practices Applied
1. **Runner Environment Isolation**: Built cleanly on standard `ubuntu-latest` with reproducible Python runtime configuration.
2. **Security**: No credentials or private tokens hardcoded into workflow YAML files.
3. **Early Feedback Loop**: Triggers automatically on both push and pull request to detect regressions before merging into production.
