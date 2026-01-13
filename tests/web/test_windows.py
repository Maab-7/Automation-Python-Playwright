import pytest
from playwright.sync_api import expect

from pages.windows_page import WindowsPage


@pytest.mark.web
@pytest.mark.smoke
# Prueba para verificar la funcionalidad de abrir una nueva ventana
def test_new_window_opens_and_has_text(context, page, base_url):
    p = WindowsPage(page, base_url)
    p.open()

    with context.expect_page() as new_page_info:
        p.click_here.click()

    new_page = new_page_info.value
    expect(new_page.get_by_role("heading", name="New Window")).to_be_visible()
    expect(new_page).to_have_url(f"{base_url.rstrip('/')}/windows/new")
