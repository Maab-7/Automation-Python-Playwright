# Se importa la clase Page desde playwright para interactuar con la página web
from playwright.sync_api import Page


# Definición de la clase BasePage que servirá como clase base para todas las páginas
class BasePage:
    # Inicializador de la clase que recibe una instancia de Page y la URL base
    def __init__(self, page: Page, base_url: str):
        self.page = page
        # Se asegura de que la URL base no termine con una barra
        self.base_url = base_url.rstrip("/")

    def go(self, path: str) -> None:
        # Método para navegar a una ruta específica en la aplicación web
        # Concatena la URL base con la ruta proporcionada y navega a esa URL
        self.page.goto(f"{self.base_url}{path}")
