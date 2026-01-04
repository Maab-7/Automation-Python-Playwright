import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.mark.web
@pytest.mark.smoke
def test_login_success_pom(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    expect(page).to_have_url(SecurePage.URL)
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")


@pytest.mark.web
def test_login_invalid_password_pom(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "badpass")

    expect(page).to_have_url(LoginPage.URL)
    expect(login.flash_message).to_contain_text("Your password is invalid!")


@pytest.mark.web
@pytest.mark.smoke
def test_logout_pom(page):
    login = LoginPage(page)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    secure = SecurePage(page)
    secure.logout()

    expect(page).to_have_url(LoginPage.URL)
    expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")
