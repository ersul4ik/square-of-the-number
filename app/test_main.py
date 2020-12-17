from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_should_return_error_when_number_is_less_than_zero():
    response = client.get('/square', params={'number': -1})
    assert response.status_code == 400
    assert response.json() == {'msg': 'The number should be greater than 0'}


def test_should_return_error_when_number_is_not_integer():
    response = client.get('/square', params={'number': 4.3})
    assert response.status_code == 422
    assert response.json() == {'msg': 'value is not a valid integer'}


def test_should_return_square_when_number_is_valid():
    response = client.get('/square', params={'number': 4})
    assert response.status_code == 200
    assert response.json() == {'msg': 'success', 'result': 2}
