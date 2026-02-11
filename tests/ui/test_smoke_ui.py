import pytest
from playwright.sync_api import expect

from data.credentials import VALID_PASSWORD, VALID_USER
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.mark.ui
@pytest.mark.smoke
def test_smoke_login_logout(page, base_url):
    # Arrange: Preparamos el entorno para la prueba
    login = LoginPage(page, base_url)
    secure = SecurePage(page, base_url)

    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    expect(page).to_have_url(secure.url)
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

    secure.logout()
    expect(page).to_have_url(f"{base_url}/login")
