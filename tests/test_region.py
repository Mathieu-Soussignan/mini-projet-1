from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# def test_create_and_get_region():
#     params = {"region_name": "North"}
#     response = client.post("/regions/", params=params)
#     assert response.status_code == 200, response.text
#     region_data = response.json()
#     assert "id_region" in region_data
#     region_id = region_data["id_region"]

#     response = client.get(f"/regions/{region_id}")
#     assert response.status_code == 200, response.text
#     fetched = response.json()
#     assert fetched["region_name"] == "North"

# def test_update_and_delete_region():
#     params = {"region_name": "South"}
#     response = client.post("/regions/", params=params)
#     assert response.status_code == 200, response.text
#     region_id = response.json()["id_region"]

#     update_params = {"region_name": "East"}
#     response = client.put(f"/regions/{region_id}", params=update_params)
#     assert response.status_code == 200, response.text
#     updated = response.json()
#     assert updated["region_name"] == "East"

#     response = client.delete(f"/regions/{region_id}")
#     assert response.status_code == 200, response.text

#     response = client.get(f"/regions/{region_id}")
#     assert response.status_code == 404, response.text