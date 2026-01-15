import pytest

from pages.hovers_page import HoversPage


@pytest.mark.web
@pytest.mark.smoke
@pytest.mark.parametrize(
    "index,expected",
    [
        (0, "name: user1"),
        (1, "name: user2"),
        (2, "name: user3"),
    ],
)
def test_hover_shows_user_caption(page, base_url, index, expected):
    p = HoversPage(page, base_url)
    p.open()

    p.hover_user(index)
    p.expect_user_visible(index, expected)
