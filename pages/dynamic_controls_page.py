from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    PATH = "/dynamic_controls"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

        self.toggle_button: Locator = page.get_by_role("button", name="Remove")
        self.message: Locator = page.locator("#message")

        self.checkbox: Locator = page.locator("#checkbox input[type='checkbox']")

        self.input_field: Locator = page.locator("#input-example input")
        self.enable_button: Locator = page.get_by_role("button", name="Enable")

    def open(self) -> None:
        self.go(self.PATH)

    def remove_checkbox(self) -> None:
        # Si esta en modo "Add", cambia el locator del boton
        if self.page.get_by_role("button", name="Add").is_visible():
            self.toggle_button = self.page.get_by_role("button", name="Add")
        self.page.get_by_role("button", name="Remove").click()
        expect(self.message).to_have_text("It's gone!")

    def add_checkbox(self) -> None:
        self.page.get_by_role("button", name="Add").click()
        expect(self.checkbox).to_be_visible()
        expect(self.message).to_have_text("It's back!")

    def enable_input(self) -> None:
        self.page.get_by_role("button", name="Enable").click()
        expect(self.input_field).to_be_enabled()
        expect(self.message).to_have_text("It's enabled!")

    def disable_input(self) -> None:
        self.page.get_by_role("button", name="Disable").click()
        expect(self.input_field).to_be_disabled()
        expect(self.message).to_have_text("It's disabled!")
