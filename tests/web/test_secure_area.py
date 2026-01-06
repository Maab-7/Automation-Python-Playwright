import pytest
from playwright.sync_api import expect


@pytest.mark.web
@pytest.mark.smoke
def test_secure_area_shows_logout(logged_in_page):
    page, _, secure = logged_in_page
    expect(secure.logout_link).to_be_visible()
    expect(secure.flash).to_contain_text("You logged into a secure area!")


@pytest.mark.web
@pytest.mark.regression
def test_logout_from_secure_area(logged_in_page):
    page, login, secure = logged_in_page

    secure.logout()

    expect(page).to_have_url(login.url)
    expect(login.flash).to_contain_text("You logged out of the secure area!")
