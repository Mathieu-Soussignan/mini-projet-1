# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# def create_test_sex_region_smoker():
#     # Créer un enregistrement pour Sex
#     sex_response = client.post("/sex/", params={"type": "male"})
#     assert sex_response.status_code == 200, sex_response.text
#     sex_id = sex_response.json()["id_sex"]

#     # Créer un enregistrement pour Region
#     region_response = client.post("/regions/", params={"region_name": "TestRegion"})
#     assert region_response.status_code == 200, region_response.text
#     region_id = region_response.json()["id_region"]

#     # Créer un enregistrement pour Smoker
#     smoker_response = client.post("/smoker/", params={"is_smoker": "no"})
#     assert smoker_response.status_code == 200, smoker_response.text
#     smoker_id = smoker_response.json()["id_smoker"]

#     return sex_id, region_id, smoker_id

# def test_create_and_get_patient():
#     sex_id, region_id, smoker_id = create_test_sex_region_smoker()
#     params = {
#         "last_name": "Doe",
#         "first_name": "John",
#         "age": 30,
#         "bmi": 22.5,
#         "patient_email": "john.doe@example.com",
#         "children": 2,
#         "charges": 123.45,
#         "sex_id": sex_id,
#         "region_id": region_id,
#         "smoker_id": smoker_id,
#         "user_id": None
#     }
#     response = client.post("/patients/", params=params)
#     assert response.status_code == 200, response.text
#     patient = response.json()
#     assert "id_patient" in patient
#     patient_id = patient["id_patient"]

#     response = client.get(f"/patients/{patient_id}")
#     assert response.status_code == 200, response.text
#     fetched = response.json()
#     assert fetched["first_name"] == "John"
#     assert fetched["last_name"] == "Doe"

# def test_update_and_delete_patient():
#     sex_id, region_id, smoker_id = create_test_sex_region_smoker()
#     params = {
#         "last_name": "Smith",
#         "first_name": "Alice",
#         "age": 40,
#         "bmi": 28.0,
#         "patient_email": "alice.smith@example.com",
#         "children": 3,
#         "charges": 200.0,
#         "sex_id": sex_id,
#         "region_id": region_id,
#         "smoker_id": smoker_id,
#         "user_id": None
#     }
#     response = client.post("/patients/", params=params)
#     assert response.status_code == 200, response.text
#     patient_id = response.json()["id_patient"]

#     update_params = {"last_name": "Johnson"}
#     response = client.put(f"/patients/{patient_id}", params=update_params)
#     assert response.status_code == 200, response.text
#     updated = response.json()
#     assert updated["last_name"] == "Johnson"

#     response = client.delete(f"/patients/{patient_id}")
#     assert response.status_code == 200, response.text

#     response = client.get(f"/patients/{patient_id}")
#     assert response.status_code == 404, response.text