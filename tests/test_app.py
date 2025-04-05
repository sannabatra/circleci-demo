# test_app.py
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask" in response.data

def test_about():
    tester = app.test_client()
    response = tester.get('/about')
    assert response.status_code == 200
    assert b"about page" in response.data