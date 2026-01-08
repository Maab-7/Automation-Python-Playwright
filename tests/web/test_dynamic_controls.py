import pytest
from playwright.sync_api import expect

from pages.dynamic_controls_page import DynamicControlsPage


@pytest.mark.web
@pytest.mark.smoke
# Prueba para verificar que el checkbox puede ser removido y agregado dinámicamente
def test_remove_and_add_checkbox(page, base_url):
    # Crear instancia de la página de controles dinámicos y abrirla
    dc = DynamicControlsPage(page, base_url)
    dc.open()

    # Remove
    page.get_by_role("button", name="Remove").click()
    expect(dc.message).to_have_text("It's gone!")
    expect(page.locator("#checkbox")).not_to_be_visible()

    # Add
    page.get_by_role("button", name="Add").click()
    expect(dc.message).to_have_text("It's back!")
    expect(page.locator("#checkbox")).to_be_visible()


@pytest.mark.web
@pytest.mark.smoke
def test_enable_and_disable_input(page, base_url):
    # Crear instancia de la página de controles dinámicos y abrirla
    dc = DynamicControlsPage(page, base_url)
    dc.open()

    # Enable
    page.get_by_role("button", name="Enable").click()
    expect(dc.message).to_have_text("It's enabled!")
    expect(dc.input_field).to_be_enabled()

    # Disable
    page.get_by_role("button", name="Disable").click()
    expect(dc.message).to_have_text("It's disabled!")
    expect(dc.input_field).to_be_disabled()
