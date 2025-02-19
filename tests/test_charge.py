from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_charge():
    response = client.post("/charges/", params={"price": 123.45})
    assert response.status_code == 200
    charge_data = response.json()
    assert "charge_id" in charge_data
    charge_id = charge_data["charge_id"]
    
    response = client.get(f"/charges/{charge_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["price"] == 123.45

def test_update_and_delete_charge():
    response = client.post("/charges/", params={"price": 200.00})
    assert response.status_code == 200
    charge_id = response.json()["charge_id"]
    
    response = client.put(f"/charges/{charge_id}", params={"price": 250.00})
    assert response.status_code == 200
    updated = response.json()
    assert updated["price"] == 250.00
    
    response = client.delete(f"/charges/{charge_id}")
    assert response.status_code == 200
    
    response = client.get(f"/charges/{charge_id}")
    assert response.status_code == 404