from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_get_smoker():
    # Création d'un enregistrement pour smoker
    response = client.post("/smoker/", params={"is_smoker": "yes"})
    assert response.status_code == 200
    data = response.json()
    assert "id_smoker" in data
    smoker_id = data["id_smoker"]
    
    # Récupération de l'enregistrement créé
    response = client.get(f"/smoker/{smoker_id}")
    assert response.status_code == 200
    data_get = response.json()
    assert data_get["is_smoker"] == "yes"

def test_update_and_delete_smoker():
    # Création d'un enregistrement de test pour smoker
    response = client.post("/smoker/", params={"is_smoker": "no"})
    smoker_id = response.json()["id_smoker"]
    
    # Mise à jour du statut fumeur
    response = client.put(f"/smoker/{smoker_id}", params={"is_smoker": "yes"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["is_smoker"] == "yes"
    
    # Suppression de l'enregistrement
    response = client.delete(f"/smoker/{smoker_id}")
    assert response.status_code == 200
    
    # Vérification de la suppression
    response = client.get(f"/smoker/{smoker_id}")
    assert response.status_code == 404