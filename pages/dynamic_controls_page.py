from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    PATH = "/dynamic_controls"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

        self.toggle_button: Locator = page.get_by_role("button", name="Remove")
        # Apunta al mensaje que aparece despues de cada accion
        self.message: Locator = page.locator("#message")
        # Apunta al checkbox dentro del contenedor del checkbox
        self.checkbox: Locator = page.locator("#checkbox input[type='checkbox']")
        # Apunta al campo de input dentro del contenedor del input
        self.input_field: Locator = page.locator("#input-example input")
        self.enable_button: Locator = page.get_by_role("button", name="Enable")
        # Se usa Locators porque son mas eficientes para multiples interacciones

    # Metodo para abrir la pagina de controles dinamicos
    def open(self) -> None:
        self.go(self.PATH)

    # En cada accion el patron es hacer click en el boton
    #  para verificar el cambio de estado
    def remove_checkbox(self) -> None:
        # Si esta en modo "Add", cambia el locator del boton
        if self.page.get_by_role("button", name="Add").is_visible():
            self.toggle_button = self.page.get_by_role("button", name="Add")
        self.page.get_by_role("button", name="Remove").click()
        # Playwright espera automaticamente a que las acciones asincronas terminen.
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
