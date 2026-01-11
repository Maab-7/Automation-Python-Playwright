from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class JSAlertsPage(BasePage):
    PATH = "/javascript_alerts"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.result: Locator = page.locator("#result")

        self.js_alert_btn: Locator = page.get_by_role(
            "button", name="Click for JS Alert"
        )
        self.js_confirm_btn: Locator = page.get_by_role(
            "button", name="Click for JS Confirm"
        )
        self.js_prompt_btn: Locator = page.get_by_role(
            "button", name="Click for JS Prompt"
        )

    def open(self) -> None:
        self.go(self.PATH)

    def expect_result_contains(self, text: str) -> None:
        expect(self.result).to_contain_text(text)
