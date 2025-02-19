import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def create_test_utilisateur_and_charge():
    # Créer un enregistrement de sex et region pour l'utilisateur
    sex_response = client.post("/sex/", params={"type": "male"})
    sex_id = sex_response.json()["sex_id"]
    region_response = client.post("/regions/", params={"region_name": "TestRegion"})
    region_id = region_response.json()["region_id"]
    
    # Créer l'utilisateur
    user_response = client.post("/utilisateurs/", params={
        "user_name": "Transaction User",
        "age": 35,
        "bmi": 24.0,
        "children": 1,
        "smoker": "no",
        "sex_id": sex_id,
        "region_id": region_id
    })
    user_id = user_response.json()["user_id"]
    
    # Créer une charge
    charge_response = client.post("/charges/", params={"price": 150.00})
    charge_id = charge_response.json()["charge_id"]
    
    return user_id, charge_id

def test_create_and_get_transaction():
    user_id, charge_id = create_test_utilisateur_and_charge()
    response = client.post("/transactions/", params={"user_id": user_id, "charge_id": charge_id})
    assert response.status_code == 200
    transaction = response.json()
    assert "transaction_id" in transaction
    transaction_id = transaction["transaction_id"]
    
    response = client.get(f"/transactions/{transaction_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["user_id"] == user_id
    assert fetched["charge_id"] == charge_id

def test_update_and_delete_transaction():
    user_id, charge_id = create_test_utilisateur_and_charge()
    response = client.post("/transactions/", params={"user_id": user_id, "charge_id": charge_id})
    transaction_id = response.json()["transaction_id"]
    
    # Pour la mise à jour, créons un nouvel utilisateur
    sex_response = client.post("/sex/", params={"type": "female"})
    new_sex_id = sex_response.json()["sex_id"]
    region_response = client.post("/regions/", params={"region_name": "NewRegion"})
    new_region_id = region_response.json()["region_id"]
    new_user_response = client.post("/utilisateurs/", params={
        "user_name": "New Transaction User",
        "age": 29,
        "bmi": 21.0,
        "children": 0,
        "smoker": "no",
        "sex_id": new_sex_id,
        "region_id": new_region_id
    })
    new_user_id = new_user_response.json()["user_id"]
    
    response = client.put(f"/transactions/{transaction_id}", params={"user_id": new_user_id})
    assert response.status_code == 200
    updated = response.json()
    assert updated["user_id"] == new_user_id
    
    # Suppression de la transaction
    response = client.delete(f"/transactions/{transaction_id}")
    assert response.status_code == 200
    
    response = client.get(f"/transactions/{transaction_id}")
    assert response.status_code == 404