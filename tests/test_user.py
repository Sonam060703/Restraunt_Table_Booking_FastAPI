import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_view_tables(client):  # Pass client as a parameter
    response = client.get("/tables")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
