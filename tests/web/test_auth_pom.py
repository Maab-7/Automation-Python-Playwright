import pytest
from playwright.sync_api import expect

from data.credentials import INVALID_CASES, VALID_PASSWORD, VALID_USER
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.mark.web
@pytest.mark.smoke
def test_login_success_pom(page, base_url):
    login = LoginPage(page, base_url)
    secure = SecurePage(page, base_url)

    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    expect(page).to_have_url(secure.url)
    expect(secure.flash).to_contain_text("You logged into a secure area!")


@pytest.mark.web
@pytest.mark.parametrize("user,pwd,expected_msg", INVALID_CASES)
def test_login_invalid_password_pom(page, base_url, user, pwd, expected_msg):
    login = LoginPage(page, base_url)
    login.open()
    login.login(user, pwd)

    expect(page).to_have_url(login.url)
    expect(login.flash).to_contain_text(expected_msg)


@pytest.mark.web
@pytest.mark.smoke
def test_logout_pom(page, base_url):
    login = LoginPage(page, base_url)
    secure = SecurePage(page, base_url)

    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    secure.logout()

    expect(page).to_have_url(login.url)
    expect(login.flash).to_contain_text("You logged out of the secure area!")
