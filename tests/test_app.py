import pytest

from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_home_page_loads(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"SprintBoard" in r.data


def test_list_seed_tasks(client):
    tasks = client.get("/api/tasks").get_json()
    assert len(tasks) == 3
    assert all(t["status"] == "To Do" for t in tasks)


def test_create_task(client):
    r = client.post("/api/tasks", json={"title": "Deploy app"})
    assert r.status_code == 201
    assert r.get_json()["title"] == "Deploy app"
    assert len(client.get("/api/tasks").get_json()) == 4


@pytest.mark.parametrize("payload", [{}, {"title": ""}, {"title": "   "}, {"title": "x" * 101}])
def test_create_task_validation(client, payload):
    assert client.post("/api/tasks", json=payload).status_code == 400


def test_update_status(client):
    r = client.patch("/api/tasks/1", json={"status": "In Progress"})
    assert r.status_code == 200
    assert r.get_json()["status"] == "In Progress"


def test_update_invalid_status(client):
    assert client.patch("/api/tasks/1", json={"status": "Blocked"}).status_code == 400


def test_update_missing_task(client):
    assert client.patch("/api/tasks/999", json={"status": "Done"}).status_code == 404


def test_delete_task(client):
    assert client.delete("/api/tasks/1").status_code == 204
    assert client.delete("/api/tasks/1").status_code == 404


def test_summary(client):
    client.patch("/api/tasks/1", json={"status": "Done"})
    s = client.get("/api/summary").get_json()
    assert s["total"] == 3
    assert s["counts"]["Done"] == 1
    assert s["percent_done"] == 33
