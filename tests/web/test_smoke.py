from playwright.sync_api import expect

# Importa expect para aserciones


def test_homepage_title(page):
    # Verifica el título de la página de inicio
    expect(page).to_have_title("Example Domain")
