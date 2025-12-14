from utils.api_client import APIClient

def test_create_post():
    payload={
        "title": "automation test",
        "body": "pytest api automation",
        "userId": 1
    }

    response = APIClient.post("/posts", payload)
    assert response.status_code == 201
    assert response.json()["title"] == "automation test"