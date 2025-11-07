import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app
from src.app import app

def test_create_task():
    client = app.test_client()
    response = client.post('/tasks', json={'titulo': 'Teste'})
    assert response.status_code == 201
    assert response.json['titulo'] == 'Teste'
