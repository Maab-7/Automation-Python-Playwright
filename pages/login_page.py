from playwright.sync_api import Locator, Page


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input: Locator = page.get_by_label("Username")
        self.password_input: Locator = page.get_by_label("Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.flash_message: Locator = page.locator("#flash")

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, user: str, pwd: str) -> None:
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()
