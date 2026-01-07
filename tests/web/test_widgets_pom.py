import pytest
from playwright.sync_api import expect

from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage


@pytest.mark.web
@pytest.mark.smoke
def test_checkboxes_can_be_toggle(page, base_url):
    cb = CheckboxesPage(page, base_url)
    cb.open()

    # Asegurar estados (en la pagina, el 2 suele estar checked)

    cb.checkbox_1.check()
    cb.checkbox_2.uncheck()

    expect(cb.checkbox_1).to_be_checked()
    expect(cb.checkbox_2).not_to_be_checked()


@pytest.mark.web
@pytest.mark.parametrize("option_value", ["1", "2"])
def test_dropdown_select_options(page, base_url, option_value):
    dd = DropdownPage(page, base_url)
    dd.open()

    dd.select(option_value)

    expect(dd.dropdown).to_have_value(option_value)
