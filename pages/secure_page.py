from playwright.sync_api import Locator, Page


class SecurePage:
    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, page: Page):
        self.page = page
        self.logout_link: Locator = page.get_by_role("link", name="Logout")
        self.flash: Locator = page.locator("#flash")

    def logout(self) -> None:
        self.logout_link.click()
