from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    def __init__(self, page: Page, base_url: str, example: int):
        super().__init__(page, base_url)
        self.example = example

        self.start_button: Locator = page.get_by_role("button", name="Start")
        self.loading: Locator = page.locator("#loading")
        self.finish: Locator = page.locator("#finish")
        self.hello: Locator = page.get_by_role("heading", name="Hello World!")

    @property
    def path(self) -> str:
        return f"/dynamic_loading/{self.example}"

    def open(self) -> None:
        self.go(self.path)

    def start(self) -> None:
        self.start_button.click()

    def wait_until_finished(self) -> None:
        # Loader desaparece cuando termina la carga
        expect(self.loading).to_be_hidden(timeout=10000)
        # Resultado visible
        expect(self.finish).to_be_visible(timeout=10000)
