import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_home():
    """ Test Home Route """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API!"}

@pytest.mark.asyncio
async def test_create_item():
    """ Teat Create Item with a valid object """
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "name": "Wireless Mouse",
            "description": "A high-precision wireless mouse with ergonomic design.",
            "price": 29.99,
            "quantity": 10
        }
        response = await client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json()["item"] == payload

@pytest.mark.asyncio
async def test_create_item_missing_field():
    """ Test Create Item using missing field """
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {"name": "Test Item"}
        response = await client.post("/items/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
