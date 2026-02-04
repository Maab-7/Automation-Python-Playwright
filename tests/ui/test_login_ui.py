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
    logout = page.locator("a.button.secondary")
    # Espera hasta que el botón de cierre de sesión sea visible
    logout.wait_for(state="visible")
    # Verifica que el botón de cierre de sesión esté visible
    assert logout.is_visible()
