from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_sex():
    # Création d'un enregistrement de sex
    response = client.post("/sex/", params={"type": "male"})
    assert response.status_code == 200
    sex_data = response.json()
    assert "sex_id" in sex_data
    sex_id = sex_data["sex_id"]
    
    # Récupération de l'enregistrement créé
    response = client.get(f"/sex/{sex_id}")
    assert response.status_code == 200
    fetched_data = response.json()
    assert fetched_data["type"] == "male"

def test_update_and_delete_sex():
    # Création d'un enregistrement à mettre à jour et supprimer
    response = client.post("/sex/", params={"type": "female"})
    assert response.status_code == 200
    sex_id = response.json()["sex_id"]
    
    # Mise à jour
    response = client.put(f"/sex/{sex_id}", params={"type": "other"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["type"] == "other"
    
    # Suppression
    response = client.delete(f"/sex/{sex_id}")
    assert response.status_code == 200
    
    # Vérification de la suppression
    response = client.get(f"/sex/{sex_id}")
    assert response.status_code == 404