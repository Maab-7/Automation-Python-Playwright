import pytest

from pages.iframe_editor_page import IframeEditorPage


@pytest.mark.web
@pytest.mark.smoke
def test_can_access_iframe_editor_readonly(page, base_url):
    p = IframeEditorPage(page, base_url)
    p.open()
    p.close_banner_if_present()
    p.expect_editor_loaded()
