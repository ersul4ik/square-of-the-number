from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_should_return_error_when_number_is_less_than_zero():
    response = client.get('/square', params={'number': -1})
    assert response.status_code == 400
    assert response.json() == {'msg': 'The number should be greater than 0'}
