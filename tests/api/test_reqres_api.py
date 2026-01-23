import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_get_users_page_2(api_client):
    # En la siguiente línea hacemos una solicitud GET a la API de ReqRes
    # Construyendo la URL con el parámetro de consulta para la página 2
    r = api_client.get("/users", params={"page": 2})
    # Verificamos que la respuesta tenga un código de estado 200 (OK)
    assert r.status_code == 200
    # Parseamos la respuesta JSON
    data = r.json()
    assert data["page"] == 2
    # Verificamos que la lista de usuarios no esté vacía
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "id" in data["data"][0]
    assert "email" in data["data"][0]


@pytest.mark.api
@pytest.mark.regression
def test_create_user(api_client):
    payload = {"name": "morpheus", "job": "leader"}
    r = api_client.post("/users", json=payload)
    assert r.status_code == 201

    data = r.json()
    # Verificamos que los datos devueltos coincidan con los enviados
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    # Verificamos que se hayan generado un id y una marca de tiempo
    assert "id" in data
    assert "createdAt" in data


@pytest.mark.api
def test_login_success(api_client):
    # Probamos el endpoint de login con credenciales válidas
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    r = api_client.post("/login", json=payload)
    assert r.status_code == 200

    data = r.json()
    # Verificamos que se haya devuelto un token de autenticación
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@pytest.mark.api
def test_login_missing_password_should_fail(api_client):
    payload = {"email": "eve.holt@reqres.in"}
    r = api_client.post("/login", json=payload)

    assert r.status_code == 400

    data = r.json()
    # Verificamos que el mensaje de error sea el esperado
    assert "error" in data
