from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class WindowsPage(BasePage):
    PATH: str = "/windows"

    def __init__(self, page: Page, base_url: str):
        # Initialize the base page
        super().__init__(page, base_url)
        # Define locators
        self.click_here: Locator = page.get_by_role("link", name="Click Here")

    def open(self) -> None:
        self.go(self.PATH)
