# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# def test_create_and_get_sex():
#     params = {"type": "male"}
#     response = client.post("/sex/", params=params)
#     assert response.status_code == 200, response.text
#     sex_data = response.json()
#     assert "id_sex" in sex_data
#     sex_id = sex_data["id_sex"]

#     response = client.get(f"/sex/{sex_id}")
#     assert response.status_code == 200, response.text
#     fetched_data = response.json()
#     assert fetched_data["type"] == "male"

# def test_update_and_delete_sex():
#     params = {"type": "female"}
#     response = client.post("/sex/", params=params)
#     assert response.status_code == 200, response.text
#     sex_id = response.json()["id_sex"]

#     update_params = {"type": "other"}
#     response = client.put(f"/sex/{sex_id}", params=update_params)
#     assert response.status_code == 200, response.text
#     updated = response.json()
#     assert updated["type"] == "other"

#     response = client.delete(f"/sex/{sex_id}")
#     assert response.status_code == 200, response.text

#     response = client.get(f"/sex/{sex_id}")
#     assert response.status_code == 404, response.text