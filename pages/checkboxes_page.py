from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    PATH = "/checkboxes"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.checkbox_1: Locator = page.locator("input[type='checkbox']").nth(0)
        self.checkbox_2: Locator = page.locator("input[type='checkbox']").nth(1)

    def open(self) -> None:
        self.go(self.PATH)
