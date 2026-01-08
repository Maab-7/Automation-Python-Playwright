# Se importan las clases necesarias desde playwright
from playwright.sync_api import Locator, Page

# Se importa la clase BasePage desde la ubicación correspondiente
from pages.base_page import BasePage


# Definición de la clase CheckboxesPage que hereda de BasePage
class CheckboxesPage(BasePage):
    # Ruta específica para la página de checkboxes
    PATH = "/checkboxes"

    # Inicializador de la clase
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        # Localizadores para los checkboxes en la página, usando selectores CSS.
        # porque playwright no tiene un método específico para checkboxes.
        # Por qué: en esa página no hay IDs/labels; esto es lo más directo.
        self.checkbox_1: Locator = page.locator("input[type='checkbox']").nth(0)
        self.checkbox_2: Locator = page.locator("input[type='checkbox']").nth(1)

    def open(self) -> None:
        # Método para abrir la página de checkboxes
        self.go(self.PATH)
