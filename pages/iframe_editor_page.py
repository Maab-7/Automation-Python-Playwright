from playwright.sync_api import FrameLocator, Locator, Page, expect

from pages.base_page import BasePage


class IframeEditorPage(BasePage):
    PATH = "/iframe"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.frame: FrameLocator = page.frame_locator("#mce_0_ifr")
        self.editor_body: Locator = self.frame.locator("body")
        self.readonly_banner_close: Locator = page.locator(
            ".tox-notification__dismiss"
        )  # la X

    def open(self) -> None:
        self.go(self.PATH)

    def close_banner_if_present(self) -> None:
        if self.readonly_banner_close.is_visible():
            self.readonly_banner_close.click()

    def expect_editor_loaded(self) -> None:
        expect(self.editor_body).to_be_visible()
        expect(self.editor_body).to_contain_text("Your content goes here.")
