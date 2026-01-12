from pathlib import Path

import pytest
from playwright.sync_api import expect

from pages.file_upload_page import FileUploadPage


@pytest.mark.web
@pytest.mark.smoke
def test_file_upload_success(page, base_url):
    p = FileUploadPage(page, base_url)
    p.open()

    file_path = Path("data/sample_upload.txt")
    p.upload(file_path)

    expect(page.get_by_role("heading", name="File Uploaded!")).to_be_visible()
    p.expect_uploaded_filename("sample_upload.txt")


@pytest.mark.web
@pytest.mark.regression
def test_file_upload_requires_file(page, base_url):
    p = FileUploadPage(page, base_url)
    p.open()

    p.upload_button.click()

    expect(page.get_by_role("heading", name="File Uploaded!")).not_to_be_visible()
