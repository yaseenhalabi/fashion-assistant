from fastapi.testclient import TestClient
from httpx import AsyncClient
from server import app  

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}


def test_getProducts():
    response = client.get("/api/getProducts/2")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert len(response.json()[0]) == 9 


def test_getProductMatches():
    tagged_sample = [
        {
            "url": "grailed.com/whatever",
            "image": "imagefromgrailed",
            "price": "55",
            "tags": "Bomber Jacket",
            "size": "US M",
            "color": "Red",
            "condition": "Used",
            "description": "this is a description",
            "rating": "5"
        }
    ] 
    response = client.post("/api/getProductMatches/2", json=tagged_sample)
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert len(response.json()[0]) == 9 

