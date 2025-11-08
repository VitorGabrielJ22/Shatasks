from src.app import app

def test_create_task_with_due_date():
    client = app.test_client()
    res = client.post("/tasks", json={
        "title": "Nova tarefa",
        "due_date": "2025-11-15"
    })
    data = res.get_json()
    
    assert res.status_code == 201
    assert data["title"] == "Nova tarefa"
    assert data["due_date"] == "2025-11-15"

def test_list_tasks():
    client = app.test_client()
    res = client.get("/tasks")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)
