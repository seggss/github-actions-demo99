import json
import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello, world!"}

def test_healthz(client):
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}

def test_add_happy_path(client):
    resp = client.post("/add", data=json.dumps({"a": 2, "b": 3}), content_type="application/json")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5.0

@pytest.mark.parametrize("payload", [
    {}, {"a": 1}, {"b": 2}, {"a": "x", "b": 2}, {"a": 1, "b": "y"},
])
def test_add_bad_input(client, payload):
    resp = client.post("/add", data=json.dumps(payload), content_type="application/json")
    assert resp.status_code == 400
    assert "error" in resp.get_json()
