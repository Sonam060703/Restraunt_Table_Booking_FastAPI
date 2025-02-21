import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_add_table(client):  # Pass it as a function argument
    response = client.post("/admin/tables", json={"seats": 4}, headers={"Authorization": "Bearer <admin_token>"})
    assert response.status_code == 200
    assert response.json()["seats"] == 4
