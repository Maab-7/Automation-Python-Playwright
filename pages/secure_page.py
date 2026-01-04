from playwright.sync_api import Locator, Page


class SecurePage:
    # URL = "https://the-internet.herokuapp.com/secure"
    PATH = "/secure"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.logout_link: Locator = page.get_by_role("link", name="Logout")
        self.flash: Locator = page.locator("#flash")

    @property
    def url(self) -> str:
        return f"{self.base_url}{self.PATH}"

    def logout(self) -> None:
        self.logout_link.click()
