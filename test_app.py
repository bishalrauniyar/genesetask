import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_message(client):
    response = client.get("/")
    data = response.get_json()
    assert data["message"] == "hecking on live 1"

def test_status_check(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"