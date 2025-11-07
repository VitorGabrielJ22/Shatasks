import pytest
from src.app import app

def test_create_task():
    client = app.test_client()
    response = client.post('/tasks', json={'titulo': 'Teste'})
    assert response.status_code == 201
    assert response.json['titulo'] == 'Teste'
