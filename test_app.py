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
    assert data["message"] == "Hello Genese Solution! My CI/CD task is running!. Now I am updating the code to test the CI/CD pipeline."

def test_status_check(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"