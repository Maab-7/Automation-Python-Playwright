import pytest

from pages.js_alerts_page import JSAlertsPage


@pytest.mark.web
@pytest.mark.smoke
def test_js_alert_accept(page, base_url):
    p = JSAlertsPage(page, base_url)
    p.open()

    page.once("dialog", lambda d: d.accept())
    p.js_alert_btn.click()

    p.expect_result_contains("You successfully clicked an alert")


@pytest.mark.web
def test_js_confirm_cancel(page, base_url):
    p = JSAlertsPage(page, base_url)
    p.open()

    page.once("dialog", lambda d: d.dismiss())
    p.js_confirm_btn.click()

    p.expect_result_contains("You clicked: Cancel")


@pytest.mark.web
@pytest.mark.regression
def test_js_prompt_input(page, base_url):
    p = JSAlertsPage(page, base_url)
    p.open()

    page.once("dialog", lambda d: d.accept("Hola"))
    p.js_prompt_btn.click()

    p.expect_result_contains("You entered: Hola")
