# Assignment 2: Continuous Integration Using GitHub Actions

A simple Python application configured with automated testing and continuous integration using GitHub Actions.

## Project Structure
- `calculator.py`: Core mathematical operations.
- `test_calculator.py`: Pytest automated unit tests.
- `requirements.txt`: Python dependencies.
- `.github/workflows/ci.yml`: GitHub Actions automated CI workflow.

## CI Workflow Features
- Triggers on every push and pull request targeting `main`.
- Automates environment provisioning, dependency installation, and test execution on `ubuntu-latest`.
