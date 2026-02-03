# QA Automation Project – Python & Playwright

Hands-on QA Automation project demonstrating web UI and API testing using **Playwright (sync)**, **Pytest**, and the **Page Object Model (POM)** approach.

---

## What this project demonstrates

This project showcases my practical experience as a QA Engineer, including:

- Designing and executing automated tests for web and API applications
- Applying Page Object Model (POM) for maintainable and scalable automation
- Validating functional flows, edge cases, and negative scenarios
- Organizing test suites using pytest markers (smoke, regression)
- Handling configuration through environment variables
- Writing clean, readable, and maintainable test code

---

## My role as QA Engineer

In this project, I acted as a QA Engineer responsible for:

- Analyzing application behavior and identifying relevant test scenarios
- Designing test cases based on functional requirements
- Implementing automated tests using Playwright and Pytest
- Debugging failing tests and analyzing root causes
- Validating UI behavior, API responses, and data consistency

---

## Tech Stack

- Python 3.11+
- Playwright (sync)
- Pytest
- Page Object Model (POM)

---

## Project Structure

pages/ # Page Objects (POM)
tests/ # Tests organized by type (api, web, ui)
src/ # Support clients/services (e.g. API client)
data/ # Test data and credentials
utils/ # Shared utilities
docs/ # Additional documentation

---

## Test Scenarios Covered

- UI validation for dynamic elements and page interactions
- Positive and negative functional scenarios
- API validation for status codes and response data
- Handling asynchronous behavior using waits
- Smoke and regression test execution

---

## Requirements

- Python 3.11+
- Git

---

## Installation

1. Create and activate a virtual environment
2. Install dependencies and browsers:

pip install -r requirements.txt
python -m playwright install

---

## Environment Variables and Options

- BASE_URL: base URL for web tests  
  Default: https://the-internet.herokuapp.com
- REQRES_API_KEY: API key for Reqres API tests  
  If not set, API tests are skipped
- --headed: runs browser in headed mode

Example:

BASE_URL="https://the-internet.herokuapp.com" pytest -m web --headed

---

## Run Tests

pytest

### Available Markers

- api: API tests
- ui: UI tests
- web: Playwright web tests
- smoke: critical and fast tests
- regression: full test suite

Examples:

pytest -m smoke
pytest -m "web and not regression"

---

## Code Style and Quality

This repository uses **black** and **ruff** enforced via **pre-commit** hooks to maintain code quality.

pre-commit install
pre-commit run --all-files
