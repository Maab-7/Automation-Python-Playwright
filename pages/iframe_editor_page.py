from playwright.sync_api import FrameLocator, Locator, Page, expect

from pages.base_page import BasePage


class IframeEditorPage(BasePage):
    PATH = "/iframe"

    def __init__(self, page: Page, base_url: str):
        # Inicializamos la página base, heredando sus funcionalidades
        super().__init__(page, base_url)
        # Usamos FrameLocator para interactuar con el iframe del editor
        # Definimos los selectores necesarios
        # Desde aqui podemos interactuar con el iframe y sus elementos
        self.frame: FrameLocator = page.frame_locator("#mce_0_ifr")
        self.editor_body: Locator = self.frame.locator("body")
        # Selector para cerrar el banner de solo lectura
        self.readonly_banner_close: Locator = page.locator(
            ".tox-notification__dismiss"
        )  # la X

    def open(self) -> None:
        self.go(self.PATH)

    def close_banner_if_present(self) -> None:
        # Cerramos el banner de solo lectura si está presente
        if self.readonly_banner_close.is_visible():
            self.readonly_banner_close.click()

    def expect_editor_loaded(self) -> None:
        # Verificamos que el editor dentro del iframe esté cargado correctamente
        expect(self.editor_body).to_be_visible()
        # Verificamos que el contenido inicial del editor sea el esperado
        expect(self.editor_body).to_contain_text("Your content goes here.")

    def clear_text(self) -> None:
        self.close_banner_if_present()
        self.editor_body.click()
        # Contenteditable: select-all + delete
        # Cleaning the editor content using both Control and
        # Meta keys for cross-platform compatibility
        self.editor_body.press("Control+A")
        self.editor_body.press("Backspace")
        self.editor_body.press("Meta+A")
        self.editor_body.press("Backspace")

    def type_text(self, text: str) -> None:
        # Close the banner if it's present before typing
        self.close_banner_if_present()
        # Clear existing text and type new text into the editor
        self.editor_body.evaluate("node => node.innerText = ''")
        # Set the new text directly using JavaScript to ensure it works
        # even if the editor is in read-only mode
        self.editor_body.evaluate("(node, text) => node.innerText = text", text)

    def get_text(self) -> str:
        # Get the current text from the editor body
        return self.editor_body.inner_text()
