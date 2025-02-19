from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def create_test_sex_and_region():
    # Créer un enregistrement de sex
    sex_response = client.post("/sex/", params={"type": "male"})
    sex_id = sex_response.json()["sex_id"]
    # Créer un enregistrement de region
    region_response = client.post("/regions/", params={"region_name": "TestRegion"})
    region_id = region_response.json()["region_id"]
    return sex_id, region_id

def test_create_and_get_utilisateur():
    sex_id, region_id = create_test_sex_and_region()
    response = client.post("/utilisateurs/", params={
        "user_name": "Test User",
        "age": 30,
        "bmi": 22.5,
        "children": 2,
        "smoker": "no",
        "sex_id": sex_id,
        "region_id": region_id
    })
    assert response.status_code == 200
    utilisateur = response.json()
    assert "user_id" in utilisateur
    user_id = utilisateur["user_id"]
    
    response = client.get(f"/utilisateurs/{user_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["user_name"] == "Test User"

def test_update_and_delete_utilisateur():
    sex_id, region_id = create_test_sex_and_region()
    response = client.post("/utilisateurs/", params={
        "user_name": "User to Update",
        "age": 40,
        "bmi": 28.0,
        "children": 3,
        "smoker": "yes",
        "sex_id": sex_id,
        "region_id": region_id
    })
    user_id = response.json()["user_id"]
    
    response = client.put(f"/utilisateurs/{user_id}", params={"user_name": "Updated User"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["user_name"] == "Updated User"
    
    response = client.delete(f"/utilisateurs/{user_id}")
    assert response.status_code == 200
    
    response = client.get(f"/utilisateurs/{user_id}")
    assert response.status_code == 404