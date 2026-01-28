import pytest


def login_payload(email: str | None = None, password: str | None = None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if password is not None:
        payload["password"] = password
    return payload


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
    payload = login_payload("eve.holt@reqres.in", "cityslicka")
    r = api_client.post("/login", json=payload)
    assert r.status_code == 200

    data = r.json()
    # Verificamos que se haya devuelto un token de autenticación
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@pytest.mark.api
def test_login_missing_password_should_fail(api_client):
    # payload = {"email": "eve.holt@reqres.in"}
    payload = login_payload(email="eve.holt@reqres.in")
    r = api_client.post("/login", json=payload)

    assert r.status_code == 400

    data = r.json()
    # Verificamos que el mensaje de error sea el esperado
    assert "error" in data


# Se utiliza mar.api para categorizar la prueba como una prueba de API
@pytest.mark.api
@pytest.mark.smoke
def test_get_users_page_1(api_client):
    # Hacemos una solicitud GET a la API de ReqRes para la página 1
    r = api_client.get("/users", params={"page": 1})
    # Verificamos que la respuesta tenga un código de estado 200 (OK)
    assert r.status_code == 200
    # Parseamos la respuesta JSON
    data = r.json()
    # Verificamos que la página devuelta sea la 1
    assert data["page"] == 1
    # Verificamos que la lista de usuarios no esté vacía
    assert isinstance(data["data"], list)
    # Verificamos que la lista de usuarios tenga al menos un elemento
    assert len(data["data"]) > 0


@pytest.mark.api
@pytest.mark.smoke
def test_login_success_token(api_client):
    # Probamos el endpoint de login con credenciales válidas
    # payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    payload = login_payload("eve.holt@reqres.in", "cityslicka")
    # Realizamos la solicitud POST al endpoint de login
    r = api_client.post("/login", json=payload)
    # Verificamos que la respuesta tenga un código de estado 200 (OK)
    assert r.status_code == 200

    # Parseamos la respuesta JSON
    data = r.json()
    # Verificamos que se haya devuelto un token de autenticación
    assert "token" in data
    # Verificamos que el token sea una cadena no vacía
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@pytest.mark.api
@pytest.mark.parametrize(
    "payload, expected_error",
    [
        # ({"email": "eve.holt@reqres.in"}, "Missing password"),
        # ({"password": "cityslicka"}, "Missing email or username"),
        (login_payload(email="eve.holt@reqres.in"), "Missing password"),
        (login_payload(password="cityslicka"), "Missing email or username"),
    ],
)
def test_login_failure_cases(api_client, payload, expected_error):
    # Probamos el endpoint de login con diferentes casos de datos faltantes
    r = api_client.post("/login", json=payload)
    # Verificamos que la respuesta tenga un código de estado 400 (Bad Request)
    assert r.status_code == 400

    # Parseamos la respuesta JSON
    data = r.json()
    # Verificamos que el mensaje de error coincida con el esperado
    assert data["error"] == expected_error


@pytest.mark.api
# Usamos parametrize para probar múltiples páginas en una sola función de prueba
@pytest.mark.parametrize("page", [1, 2])
def test_get_users_pages(api_client, page):
    # Hacemos una solicitud GET a la API de ReqRes para la página especificada
    r = api_client.get("/users", params={"page": page})
    # Verificamos que la respuesta tenga un código de estado 200 (OK)
    assert r.status_code == 200
    # Parseamos la respuesta JSON
    data = r.json()
    # Verificamos que la página devuelta sea la esperada
    assert data["page"] == page
    # Verificamos que la lista de usuarios no esté vacía
    assert isinstance(data["data"], list)
    # Verificamos que la lista de usuarios tenga al menos un elemento
    assert len(data["data"]) > 0
    assert "id" in data["data"][0]
    assert "email" in data["data"][0]


@pytest.mark.api
def test_get_user_not_found(api_client):
    # Hacemos una solicitud GET a la API de ReqRes para un usuario inexistente
    r = api_client.get("/users/23")
    # Verificamos que la respuesta tenga un código de estado 404 (Not Found)
    assert r.status_code == 404
    # Verificamos que el cuerpo de la respuesta esté vacío
    assert r.json() == {}


@pytest.mark.api
def test_create_user_basic(api_client):
    payload = {"name": "neo", "job": "the one"}
    r = api_client.post("/users", json=payload)
    assert r.status_code == 201

    data = r.json()
    # Verificamos que los datos devueltos coincidan con los enviados
    assert data["name"] == "neo"
    assert data["job"] == "the one"
    # Verificamos que se hayan generado un id y una marca de tiempo
    assert "id" in data
    # Verificamos que se haya generado una marca de tiempo de creación
    assert "createdAt" in data


@pytest.mark.api
def test_get_users_response_shape(api_client):
    r = api_client.get("/users", params={"page": 1})
    assert r.status_code == 200

    data = r.json()
    # Verificamos la estructura de la respuesta
    assert "page" in data
    # Verificamos que los campos de paginación estén presentes
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    # Verificamos que cada usuario tenga los campos esperados
    first = data["data"][0]
    assert "id" in first
    assert "email" in first
    assert "first_name" in first
    assert "last_name" in first
    assert "avatar" in first
