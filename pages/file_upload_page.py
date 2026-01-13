from pathlib import Path

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class FileUploadPage(BasePage):
    PATH = "/upload"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.file_input: Locator = page.locator("#file-upload")
        self.upload_button: Locator = page.locator("#file-submit")
        self.uploaded_files: Locator = page.locator("#uploaded-files")
        self.heading: Locator = page.get_by_role("heading", name="File Uploader")

    def open(self) -> None:
        self.go(self.PATH)

    def upload(self, file_path: Path) -> None:
        # Establece el archivo para cargar y hace clic en el botón de carga
        self.file_input.set_input_files(str(file_path))
        self.upload_button.click()

    def expect_uploaded_filename(self, name: str) -> None:
        expect(self.uploaded_files).to_have_text(name)
