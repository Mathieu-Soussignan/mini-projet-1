import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_region():
    response = client.post("/regions/", params={"region_name": "North"})
    assert response.status_code == 200
    region_data = response.json()
    assert "region_id" in region_data
    region_id = region_data["region_id"]
    
    response = client.get(f"/regions/{region_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["region_name"] == "North"

def test_update_and_delete_region():
    response = client.post("/regions/", params={"region_name": "South"})
    assert response.status_code == 200
    region_id = response.json()["region_id"]
    
    response = client.put(f"/regions/{region_id}", params={"region_name": "East"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["region_name"] == "East"
    
    response = client.delete(f"/regions/{region_id}")
    assert response.status_code == 200
    
    response = client.get(f"/regions/{region_id}")
    assert response.status_code == 404