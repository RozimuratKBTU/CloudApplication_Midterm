import json
import pytest
from main import app


def test_greet():
    client = app.test_client()
    response = client.post('/api/greet', json={'name': 'Test'})
    data = json.loads(response.data)
    assert 'message' in data


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Главная страница должна загружаться"""
    response = client.get('/')
    assert response.status_code == 200


def test_create_meeting(client, monkeypatch):
    # Заглушка, чтобы не делать реальный запрос в Cloud Function
    def fake_notify(title, date, time, description):
        return True

    monkeypatch.setattr('main.send_notification', fake_notify)

    response = client.post('/create', data={
        'title': 'Test Meeting',
        'date': '2025-10-20',
        'time': '12:00',
        'description': 'Test description'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Test Meeting' in response.data or b'meetings' in response.data


def test_greet_api(client, monkeypatch):
    """Тест API /api/greet"""

    class FakeResponse:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {'message': 'Hello from test!'}

    # Подменяем requests.post, чтобы не обращаться к реальному URL
    monkeypatch.setattr('requests.post', lambda *a, **kw: FakeResponse())

    response = client.post('/api/greet', json={'name': 'Rozimurat'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
