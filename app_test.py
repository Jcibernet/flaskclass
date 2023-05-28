import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_user_route(client: FlaskClient):
    response = client.post('/users', json={'name': 'Juan', 'email': 'juan@gmail.com'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data
    assert data['message'] == 'User created: Juan (juan@gmail.com)'

def test_get_user_route(client: FlaskClient):
    client.post('/users', json={'name': 'Juan', 'email': 'juan@gmail.com'})

    response = client.get('/users/Juan')
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data
    assert data['message'] == 'User found: Juan (Juan@gmail.com)'

def test_get_user_route_user_not_found(client: FlaskClient):
    response = client.get('/users/NonExistingUser')
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data
    assert data['message'] == 'User not found'