def test_create_package(client):
    response = client.post("/packages", json={"location": "Salta"})
    assert response.status_code == 201
    assert response.json["location"] == "Salta"