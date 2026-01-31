# Importa el modulo time para medir el tiempo de respuesta
import time

import pytest
from jsonschema import validate

USER_SCHEMA = {
    "type": "object",
    "required": ["page", "per_page", "total", "total_pages", "data"],
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "email", "first_name", "last_name", "avatar"],
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"},
                },
            },
        },
    },
}


@pytest.mark.api
def test_get_users_schema(api_client):
    r = api_client.get("/users", params={"page": 1})
    assert r.status_code == 200
    validate(instance=r.json(), schema=USER_SCHEMA)


LOGIN_SCHEMA = {
    "type": "object",
    "required": ["token"],
    "properties": {
        "token": {"type": "string"},
    },
}


@pytest.mark.api
def test_login_schema(api_client):
    payload = login_payload("eve.holt@reqres.in", "cityslicka")
    r = api_client.post("/login", json=payload)
    assert r.status_code == 200
    validate(instance=r.json(), schema=LOGIN_SCHEMA)


def login_payload(email: str | None = None, password: str | None = None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if password is not None:
        payload["password"] = password
    return payload


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("page", [1, 2])
def test_get_users_pages(api_client, page):
    r = api_client.get("/users", params={"page": page})
    assert r.status_code == 200

    data = r.json()
    assert data["page"] == page
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "id" in data["data"][0]
    assert "email" in data["data"][0]


@pytest.mark.api
def test_get_users_response_shape(api_client):
    r = api_client.get("/users", params={"page": 1})
    assert r.status_code == 200

    data = r.json()
    assert "page" in data
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    first = data["data"][0]
    assert "id" in first
    assert "email" in first
    assert "first_name" in first
    assert "last_name" in first
    assert "avatar" in first


@pytest.mark.api
@pytest.mark.smoke
def test_login_success_token(api_client):
    payload = login_payload("eve.holt@reqres.in", "cityslicka")
    r = api_client.post("/login", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@pytest.mark.api
@pytest.mark.regression
def test_create_user_basic(api_client):
    payload = {"name": "neo", "job": "the one"}
    r = api_client.post("/users", json=payload)
    assert r.status_code == 201

    data = r.json()
    assert data["name"] == "neo"
    assert data["job"] == "the one"
    assert "id" in data
    assert "createdAt" in data


@pytest.mark.api
@pytest.mark.parametrize(
    "payload, expected_error",
    [
        (login_payload(email="eve.holt@reqres.in"), "Missing password"),
        (login_payload(password="cityslicka"), "Missing email or username"),
    ],
)
def test_login_failure_cases(api_client, payload, expected_error):
    r = api_client.post("/login", json=payload)
    assert r.status_code == 400

    data = r.json()
    assert data["error"] == expected_error


@pytest.mark.api
def test_get_user_not_found(api_client):
    r = api_client.get("/users/23")
    assert r.status_code == 404
    assert r.json() == {}


# Este es un nuevo test para medir el tiempo de respuesta
@pytest.mark.api
def test_get_users_response_time(api_client):
    # Measure the response time for the GET /users endpoint
    # Guarda el tiempo actual con alta precision
    start = time.perf_counter()
    r = api_client.get("/users", params={"page": 1})
    # Calcula el tiempo transcurrido
    elapsed = time.perf_counter() - start

    assert r.status_code == 200
    # Verifica que el tiempo de respuesta sea menor a 2 segundos
    assert elapsed < 2.0
