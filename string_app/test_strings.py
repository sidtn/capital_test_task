def test_create_string(client):
    response = client.post("/strings", json={"value": "Test String"})
    assert response.status_code == 201
    assert response.json["value"] == "Test String"


def test_get_strings(client):
    client.post("/strings", json={"value": "Test String"})
    response = client.get("/strings")
    assert response.status_code == 200
    assert len(response.json) == 1


def test_update_string(client):
    post_response = client.post("/strings", json={"value": "Old String"})
    string_id = post_response.json["id"]
    response = client.put(
        f"/strings/{string_id}", json={"value": "New String"}
    )
    assert response.status_code == 200
    assert response.json["value"] == "New String"


def test_delete_string(client):
    post_response = client.post("/strings", json={"value": "To Be Deleted"})
    string_id = post_response.json["id"]
    response = client.delete(f"/strings/{string_id}")
    assert response.status_code == 200
    assert response.json["message"] == "String deleted"


def test_search_strings(client):
    client.post("/strings", json={"value": "Hello World"})
    client.post("/strings", json={"value": "Goodbye World"})
    response = client.get("/strings/search?q=Hello")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["value"] == "Hello World"
