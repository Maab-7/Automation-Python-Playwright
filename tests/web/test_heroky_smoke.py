import pytest
from playwright.sync_api import expect


@pytest.mark.web
@pytest.mark.smoke
def test_home_loads(page):
    page.goto("https://the-internet.herokuapp.com")
    expect(page.get_by_role("heading", name="Welcome to the-internet")).to_be_visible()


@pytest.mark.web
@pytest.mark.smoke
def test_navigate_to_form_authentication(page):
    page.goto("https://the-internet.herokuapp.com")
    page.get_by_role("link", name="Form Authentication").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()


@pytest.mark.web
@pytest.mark.smoke
def test_login_success(page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    flash = page.locator("#flash")
    expect(flash).to_contain_text("You logged into a secure area!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
