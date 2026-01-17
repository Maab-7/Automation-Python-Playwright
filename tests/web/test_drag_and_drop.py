import pytest

from pages.drag_drop_page import DragDropPage


@pytest.mark.web
@pytest.mark.smoke
def test_drag_a_to_b(page, base_url):
    p = DragDropPage(page, base_url)
    p.open()

    p.drag_a_to_b_simple()
    p.expect_swapped()
