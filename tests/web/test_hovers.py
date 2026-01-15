import pytest

from pages.hovers_page import HoversPage


@pytest.mark.web
@pytest.mark.smoke
# Esto hacer que en un solo test se prueben varios casos (3 usuarios)
@pytest.mark.parametrize(
    "index,expected",
    [
        (0, "name: user1"),
        (1, "name: user2"),
        (2, "name: user3"),
    ],
)
# Probamos que al hacer hover sobre cada usuario, su caption se muestra correctamente
def test_hover_shows_user_caption(page, base_url, index, expected):
    p = HoversPage(page, base_url)
    p.open()
    # Hacemos hover sobre el usuario en la posición dada
    p.hover_user(index)
    # Verificamos que el caption del usuario sea visible y correcto
    p.expect_user_visible(index, expected)
