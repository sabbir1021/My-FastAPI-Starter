from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/v1/auth/login/", json={
        "username": "admin",
        "password": "password"
    })

    assert response.status_code == 200
    json_data = response.json()
    assert "access_token" in json_data
    assert isinstance(json_data["access_token"], str)

def test_login_failure_integration():
    response = client.post("/api/v1/auth/login/", json={
        "username": "wrong",
        "password": "incorrect"
    })

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}
