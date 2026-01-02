import os

import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://example.com"),
    )
    parser.addoption("--headed", action="store_true", default=False)


@pytest.fixture(scope="session")
def base_url(request) -> str:
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def headed(request) -> bool:
    return bool(request.config.getoption("--headed"))


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, headed):
    browser = playwright_instance.chromium.launch(
        headless=not headed, slow_mo=50 if headed else 0
    )
    yield browser
    browser.close()


@pytest.fixture()
def context(browser):
    ctx = browser.new_context()
    yield ctx
    ctx.close()


@pytest.fixture()
def page(context, base_url):
    page = context.new_page()
    page.goto(base_url)
    yield page
    page.close()
