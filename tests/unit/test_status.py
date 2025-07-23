from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_login_success():
    body = {
        "username": "admin",
        "password": "password"
    }
    response = client.post("/api/v1/auth/login/", json=body)
    assert response.status_code == 200
    assert response.json() == {"access_token": "fake-jwt-token"}


def test_login_failure():
    body = {
        "username": "wrong",
        "password": "user"
    }
    response = client.post("/api/v1/auth/login/", json=body)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"