import pytest


@pytest.mark.ui
def test_login_success_ui(logged_in_page):
    page, login, secure = logged_in_page
    assert page.url == secure.url
