from utils.api_client import APIClient

def test_get_users_status_code():
    response = APIClient.get("/users")
    assert response.status_code == 200


def test_get_users_response_body():
    response = APIClient.get("/users")
    data = response.json()
    assert len(data) > 0
    assert "username" in data[0]