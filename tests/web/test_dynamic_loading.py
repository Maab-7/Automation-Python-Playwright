import pytest
from playwright.sync_api import expect

from pages.dynamic_loading_page import DynamicLoadingPage


@pytest.mark.web
@pytest.mark.smoke
def test_dynamic_loading_example1_smoke(page, base_url):
    dl = DynamicLoadingPage(page, base_url, example=1)
    dl.open()

    dl.start()
    dl.wait_until_finished()

    expect(dl.hello).to_be_visible()


@pytest.mark.web
@pytest.mark.regression
@pytest.mark.parametrize("example", [1, 2])
def test_dynamic_loading_examples_regression(page, base_url, example):
    dl = DynamicLoadingPage(page, base_url, example=example)
    dl.open()

    dl.start()

    # Validar que el loader aparece
    expect(dl.loading).to_be_visible()

    dl.wait_until_finished()
    expect(dl.hello).to_be_visible()
