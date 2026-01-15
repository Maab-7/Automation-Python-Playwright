from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class HoversPage(BasePage):
    PATH = "/hovers"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.figures: Locator = page.locator(".figure")

    def open(self) -> None:
        self.go(self.PATH)

    def hover_user(self, index: int) -> None:
        self.figures.nth(index).hover()

    def user_caption(self, index: int) -> Locator:
        return self.figures.nth(index).locator(".figcaption")

    def expect_user_visible(self, index: int, expected_name: str) -> None:
        caption = self.user_caption(index)
        expect(caption).to_be_visible()
        expect(caption).to_contain_text(expected_name)
        expect(caption.get_by_role("link", name="View profile")).to_be_visible()
