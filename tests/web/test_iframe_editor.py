import pytest

from pages.iframe_editor_page import IframeEditorPage


@pytest.mark.web
@pytest.mark.smoke
def test_can_access_iframe_editor_readonly(page, base_url):
    p = IframeEditorPage(page, base_url)
    p.open()
    p.close_banner_if_present()
    p.expect_editor_loaded()


@pytest.mark.ui
def test_iframe_editor_write_text(page, base_url):
    # Using fixtures of page and base_url to create an instance of the IframeEditorPage
    editor = IframeEditorPage(page, base_url)
    # Open the iframe editor page
    editor.open()

    # Clear any existing text and type new text into the editor
    editor.clear_text()
    editor.type_text("Hola desde Playwright!")

    # Assert that the text we typed is present in the editor
    assert "Hola desde Playwright!" in editor.get_text()
