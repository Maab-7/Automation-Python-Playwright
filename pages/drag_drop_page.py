from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage

# Estas importaciones permiten
# Locator para guardar referencias a elementos de la página
# Page La pestaña del navegador
# expect para realizar aserciones en los tests
# BasePage es la clase base que contiene funcionalidades comunes para todas las páginas


class DragDropPage(BasePage):
    PATH = "/drag_and_drop"

    def __init__(self, page: Page, base_url: str):
        # Inicializamos la página base, heredando sus funcionalidades
        super().__init__(page, base_url)
        # Definimos los selectores necesarios
        # Localiza los contenedores de las columnas A y B
        self.column_a: Locator = page.locator("#column-a")
        self.column_b: Locator = page.locator("#column-b")
        self.header_a: Locator = page.locator("#column-a header")
        self.header_b: Locator = page.locator("#column-b header")

    def open(self) -> None:
        self.go(self.PATH)

    def drag_a_to_b_simple(self) -> None:
        # Realizamos la acción de arrastrar la columna A a la columna B
        # drag_to es un método de Locator que simula el arrastre de un elemento a otro
        self.column_a.drag_to(self.column_b)

    def expect_swapped(self) -> None:
        # Verificamos que las columnas se hayan intercambiado correctamente
        expect(self.header_a).to_contain_text("B")
        expect(self.header_b).to_contain_text("A")
