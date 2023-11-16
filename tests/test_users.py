from uuid import uuid4
from fastapi.testclient import TestClient

users = {
    "email": "test.cacau@cacau.com",
    "password": "cacau",
    "first_name": "Cacau",
    "last_name": "Cacaueiro",
}


class TestUser:
    def test_create_user(self, client: TestClient) -> None:
        response = client.post("/users/", json=users)
        assert response.status_code == 200
        assert response.json()["email"] == "test.cacau@cacau.com"
        assert response.json()["first_name"] == "Cacau"
        assert response.json()["last_name"] == "Cacaueiro"

    def test_get_all_users(self, client: TestClient) -> None:
        client.post("/users/", json=users)
        response = client.get("/users/")
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_user_by_uuid(self, client: TestClient) -> None:
        user = client.post("/users/", json=users).json()
        uuid = user["uuid"]
        response = client.get(f"/users/?uuid={uuid}")
        assert response.status_code == 200
        assert response.json()[0]["email"] == "test.cacau@cacau.com"
        assert response.json()[0]["first_name"] == "Cacau"
        assert response.json()[0]["last_name"] == "Cacaueiro"

    def test_get_user_by_email(self, client: TestClient) -> None:
        client.post("/users/", json=users)
        response = client.get(f"/users/?email=test.cacau@cacau.com")
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["email"] == "test.cacau@cacau.com"
        assert response.json()[0]["first_name"] == "Cacau"
        assert response.json()[0]["last_name"] == "Cacaueiro"

    def test_update_user(self, client: TestClient) -> None:
        user = client.post("/users/", json=users).json()
        user["first_name"] = "Cacau Modified"
        response = client.put(f"/users/", json=user)
        assert response.status_code == 200
        assert response.json()["first_name"] == "Cacau Modified"
        assert response.json()["last_name"] == "Cacaueiro"

    def test_delete_user(self, client: TestClient) -> None:
        user = client.post("/users/", json=users).json()
        uuid = user["uuid"]
        response = client.delete(f"/users/{uuid}")
        assert response.status_code == 200

def test_delete_user_not_found(client: TestClient) -> None:
    response = client.delete(f"/users/{uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_get_user_by_id_not_found(client: TestClient) -> None:
    response = client.get(f"/users/?uuid={uuid4()}")
    assert response.status_code == 200
    assert response.json() == []

def test_get_user_by_email_not_found(client: TestClient) -> None:
    response = client.get(f"/users/?email=morando@cacau.com")
    assert response.status_code == 200
    assert response.json() == []

def test_update_user_not_found(client: TestClient) -> None:
    user = client.post("/users/", json=users).json()
    user["uuid"] = str(uuid4())
    response = client.put(f"/users/", json=user)
    assert response.status_code == 404
