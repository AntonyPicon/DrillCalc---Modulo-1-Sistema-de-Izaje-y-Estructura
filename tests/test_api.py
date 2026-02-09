import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app

@pytest.mark.asyncio
async def test_calculate_endpoint_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "hook_load": 250000,
            "lines": 12,
            "sheaves": 15,
            "friction_factor": 1.04,
            "wire_strength": 120000
        }
        response = await ac.post("/module-1/calculate", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "efficiency" in data
        assert "fast_line_tension" in data
        assert data["alert_level"] == "SAFE"

@pytest.mark.asyncio
async def test_calculate_endpoint_validation_error():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "hook_load": -100,  # Invalid load
            "lines": 12,
            "sheaves": 15,
            "friction_factor": 1.04,
            "wire_strength": 120000
        }
        response = await ac.post("/module-1/calculate", json=payload)
        assert response.status_code == 422  # Pydantic validation error
