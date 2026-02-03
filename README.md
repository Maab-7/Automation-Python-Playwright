# Automation Python Playwright

Test automation project using **Playwright (sync)**, **Pytest**, and a **Page Object Model (POM)** approach. Includes **web**, **UI**, and **API** tests.

## Requirements

- Python 3.11+
- Git

## Installation

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
python -m playwright install
```

## Project Structure

- `pages/`: Page Objects (POM)
- `tests/`: tests organized by type (`api`, `web`, `ui`)
- `src/`: support clients/services (e.g., API client)
- `data/`: test data and credentials
- `utils/`: shared utilities
- `docs/`: additional documentation

## Environment Variables and Options

- `BASE_URL`: base URL for web tests (default: `https://the-internet.herokuapp.com`)
- `REQRES_API_KEY`: API key for Reqres tests (if missing, API tests are skipped)
- `--headed`: run the browser in headed mode

Example:

```bash
BASE_URL="https://the-internet.herokuapp.com" pytest -m web --headed
```

## Run Tests

```bash
pytest
```

### Available Markers

- `api`: API tests
- `ui`: UI tests
- `web`: Playwright web tests
- `smoke`: critical and fast tests
- `regression`: full suite

Examples:

```bash
pytest -m smoke
pytest -m "web and not regression"
```

## Code Style

This repo uses `ruff` and `black` via `pre-commit`.

```bash
pre-commit install
pre-commit run --all-files
```
