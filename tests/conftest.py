import os

import pytest
from playwright.sync_api import expect, sync_playwright

from data.credentials import VALID_PASSWORD, VALID_USER
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://the-internet.herokuapp.com"),
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


# Fixture para proporcionar una página ya autenticada
@pytest.fixture()
def logged_in_page(page, base_url):
    # Un fixture es una función especial que se utiliza para configurar
    # el entorno de prueba y proporcionar datos o estados necesarios
    # para las pruebas.
    # Aquí, el fixture 'logged_in_page' se encarga de iniciar sesión
    # en la aplicación web antes de que se ejecute cualquier prueba
    # que lo requiera.
    login = LoginPage(page, base_url)
    secure = SecurePage(page, base_url)

    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    # sanity check para asegurar que el inicio de sesión fue exitoso
    expect(page).to_have_url(secure.url)

    return page, login, secure
    # Se devuelve la página, junto con los objetos de las páginas
    # de inicio de sesión y segura para su uso en las pruebas
