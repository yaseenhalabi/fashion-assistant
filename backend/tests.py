from fastapi.testclient import TestClient
from httpx import AsyncClient
from server import app  

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}


