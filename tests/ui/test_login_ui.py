import pytest


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
    logout.wait_for(state="visible")
    # Verifica que el botón de cierre de sesión esté visible
    assert logout.is_visible()


@pytest.mark.ui
def test_secure_page_flash_message(logged_in_page):
    page, login, secure = logged_in_page
    # Verifica que el mensaje flash de éxito esté presente en la página segura
    flash = page.locator("#flash")
    flash.wait_for(state="visible")
    # Verifica que el mensaje contenga el texto esperado
    assert "You logged into a secure area!" in flash.inner_text()
