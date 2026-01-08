import pytest
from playwright.sync_api import expect

from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage


@pytest.mark.web
@pytest.mark.smoke
# Prueba para verificar que los checkboxes pueden ser marcados y desmarcados
def test_checkboxes_can_be_toggle(page, base_url):
    # Crear instancia de la página de checkboxes y abrirla
    cb = CheckboxesPage(page, base_url)
    cb.open()

    # Asegurar estados (en la pagina, el 2 suele estar checked)
    # Marcar el primer checkbox y desmarcar el segundo
    cb.checkbox_1.check()
    cb.checkbox_2.uncheck()

    # Verificar los estados de los checkboxes
    expect(cb.checkbox_1).to_be_checked()
    expect(cb.checkbox_2).not_to_be_checked()


@pytest.mark.web
# Prueba para verificar que se pueden seleccionar opciones en el dropdown
# usando parametrización para probar múltiples opciones
@pytest.mark.parametrize("option_value", ["1", "2"])
def test_dropdown_select_options(page, base_url, option_value):
    # Crear instancia de la página de dropdown y abrirla
    dd = DropdownPage(page, base_url)
    dd.open()

    # Seleccionar la opción especificada
    dd.select(option_value)

    # Verificar que la opción seleccionada es la correcta
    expect(dd.dropdown).to_have_value(option_value)
