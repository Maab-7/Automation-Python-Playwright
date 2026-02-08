from playwright.sync_api import Locator, Page


class LoginPage:
    # URL = "https://the-internet.herokuapp.com/login"
    PATH = "/login"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.username: Locator = page.get_by_label("Username")
        self.password: Locator = page.get_by_label("Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.flash: Locator = page.locator("#flash")

    @property
    def url(self) -> str:
        return f"{self.base_url}{self.PATH}"

    def open(self) -> None:
        self.page.goto(self.url)

    def login(self, user: str, pwd: str) -> None:
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()

    def login_invalid(self, username: str, password: str):
        self.open()
        self.login(username, password)
