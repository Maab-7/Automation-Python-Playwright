from os import sync
from playwright.sync_api import sync_playwright, expect

def test_homepage_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        expect(page).to_have_title("Example Domain")
        browser.close()

        