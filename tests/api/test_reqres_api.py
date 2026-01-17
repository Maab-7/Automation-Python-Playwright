import os

import pytest
import requests

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")

HEADERS = {
    "x-api-key": API_KEY or "",
    "User-Agent": "qa-automation/1.0",
}


@pytest.fixture(autouse=True)
def require_api_key():
    if not API_KEY:
        pytest.skip("API key not set in environment variable REQRES_API_KEY")


@pytest.mark.api
@pytest.mark.smoke
def test_get_users_page_2():
    r = requests.get(
        f"{BASE_URL}/users", params={"page": 2}, headers=HEADERS, timeout=10
    )
    assert r.status_code == 200

    data = r.json()
    assert data["page"] == 2
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    assert "id" in data["data"][0]
    assert "email" in data["data"][0]


@pytest.mark.api
@pytest.mark.regression
def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS, timeout=10)
    assert r.status_code == 201

    data = r.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    assert "id" in data
    assert "createdAt" in data


@pytest.mark.api
def test_login_success():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    r = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS, timeout=10)
    assert r.status_code == 200

    data = r.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@pytest.mark.api
def test_login_missing_password_should_fail():
    payload = {"email": "eve.holt@reqres.in"}
    r = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS, timeout=10)
    assert r.status_code == 400

    data = r.json()
    assert "error" in data
