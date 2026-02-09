import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


@pytest.mark.ui
def test_login_success_ui(logged_in_page):
    page, login, secure = logged_in_page
    assert page.url == secure.url


@pytest.mark.ui
def test_secure_page_has_logout_button(logged_in_page):
    page, login, secure = logged_in_page
    # Espera explicita a un elemento clave en la página segura
    # busca el botón de cierre de sesión, usando un selector CSS
    # logout = page.locator("a.button.secondary")
    # logout = page.get_by_role("link", name="Logout")
    logout = secure.logout_button()
    # Espera hasta que el botón de cierre de sesión sea visible
    # logout.wait_for(state="visible")
    # Verifica que el botón de cierre de sesión esté visible
    # assert logout.is_visible()

    # Usando expect para una aserción más legible
    expect(logout).to_be_visible()


@pytest.mark.ui
def test_secure_page_flash_message(logged_in_page):
    page, login, secure = logged_in_page
    # Verifica que el mensaje flash de éxito esté presente en la página segura
    flash = page.locator("#flash")
    flash.wait_for(state="visible")
    # Verifica que el mensaje contenga el texto esperado
    assert "You logged into a secure area!" in flash.inner_text()


@pytest.mark.ui
def test_logout_redirects_to_login(logged_in_page, base_url):
    page, login, secure = logged_in_page

    secure.logout()
    assert page.url == f"{base_url}/login"


# Probando un login fallido y validando el mensaje
@pytest.mark.ui
def test_login_invalid_shows_error(page, base_url):
    login = LoginPage(page, base_url)
    login.login_invalid("bad_user", "bad_pass")
    # page.goto(f"{base_url}/login")

    # page.get_by_label("Username").fill("bad_user")
    # page.get_by_label("Password").fill("bad_pass")
    # page.get_by_role("button", name="Login").click()

    flash = page.locator("#flash")
    flash.wait_for(state="visible")
    assert "Your username is invalid!" in flash.inner_text()
    # assert "Texto incorrecto" in flash.inner_text()
