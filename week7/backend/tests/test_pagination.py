import pytest
from fastapi.testclient import TestClient

def test_pagination_limit_and_skip(client: TestClient):
    for i in range(10):
        client.post("/notes/", json={"title": f"Note {i:02d}", "content": f"Content {i}"})

    response = client.get("/notes/?limit=5&sort=title")
    assert response.status_code == 200
    assert len(response.json()) == 5

    response = client.get("/notes/?skip=5&limit=5&sort=title")
    assert response.status_code == 200
    assert len(response.json()) == 5
    assert response.json()[0]["title"] == "Note 05"

def test_sorting_by_title(client: TestClient):
    client.post("/notes/", json={"title": "Banana", "content": "A fruit"})
    client.post("/notes/", json={"title": "Apple", "content": "A fruit"})
    client.post("/notes/", json={"title": "Cherry", "content": "A fruit"})

    response = client.get("/notes/?sort=title")
    notes = response.json()
    titles = [n["title"] for n in notes]
    assert titles == sorted(titles)

    response = client.get("/notes/?sort=-title")
    notes = response.json()
    titles = [n["title"] for n in notes]
    assert titles == sorted(titles, reverse=True)