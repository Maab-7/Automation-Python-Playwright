from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class DropdownPage(BasePage):
    PATH = "/dropdown"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.dropdown: Locator = page.locator("select#dropdown")

    def open(self) -> None:
        self.go(self.PATH)

    def select(self, option_value: str) -> None:
        self.dropdown.select_option(value=option_value)
