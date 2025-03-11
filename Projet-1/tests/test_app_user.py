import random
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# def test_create_and_get_app_user():
#     unique_email = f"test{random.randint(1,100000)}@example.com"
#     params = {
#         "username": "testuser",
#         "password": "secret",
#         "user_email": unique_email
#     }
#     response = client.post("/app_user/", params=params)
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert "id_user" in data
#     user_id = data["id_user"]

#     response = client.get(f"/app_user/{user_id}")
#     assert response.status_code == 200, response.text
#     get_data = response.json()
#     assert get_data["username"] == "testuser"

def test_update_and_delete_app_user():
    unique_email = f"test{random.randint(1,100000)}@example.com"
    params = {
        "username": "user2",
        "password": "pass",
        "user_email": unique_email
    }
    response = client.post("/app_user/", params=params)
    assert response.status_code == 200, response.text
    user_id = response.json()["id_user"]

    update_params = {"username": "updateduser"}
    response = client.put(f"/app_user/{user_id}", params=update_params)
    assert response.status_code == 200, response.text
    updated = response.json()
    assert updated["username"] == "updateduser"

    response = client.delete(f"/app_user/{user_id}")
    assert response.status_code == 200, response.text

    response = client.get(f"/app_user/{user_id}")
    assert response.status_code == 404, response.text