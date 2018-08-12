import pytest

from application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    client = application.test_client()
    yield client


def test_hello_world(client):
    """Index returns hello world"""
    res = client.get('/')
    assert b'Hello World!' in res.data
