from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class HoversPage(BasePage):
    PATH = "/hovers"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        # Definimos el selector para las figuras de usuario
        # Desde aqui podemos interactuar con las figuras y sus captions
        # Devuelve una lista de elementos que representan las figuras de usuario
        self.figures: Locator = page.locator(".figure")

    def open(self) -> None:
        self.go(self.PATH)

    def hover_user(self, index: int) -> None:
        # Realizamos hover sobre la figura del usuario en la posición dada
        # Seleccionamos la figura por su índice y aplicamos hover
        self.figures.nth(index).hover()

    def user_caption(self, index: int) -> Locator:
        # Devuelve el caption del usuario en la posición dada
        return self.figures.nth(index).locator(".figcaption")

    def expect_user_visible(self, index: int, expected_name: str) -> None:
        caption = self.user_caption(index)
        # Verificamos que el caption del usuario sea visible
        # y contenga el nombre esperado
        expect(caption).to_be_visible()
        # Verificamos que el caption contenga el nombre esperado
        expect(caption).to_contain_text(expected_name)
        # Verificamos que el enlace "View profile" esté visible dentro del caption
        expect(caption.get_by_role("link", name="View profile")).to_be_visible()
