def test_create_package(client):
    response = client.post("/packages", json={"location": "NY"})
    assert response.status_code == 201