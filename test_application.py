import pytest
import datetime

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


def test_concat_job(client):
    """Can schedule job"""
    now = datetime.datetime.utcnow()
    one_minute_later = now + datetime.timedelta(minutes=1)
    res = client.post('/scheduler/jobs',
                      json={
                        "id": "test_job",
                        "func": "jobs:concat_two",
                        "args": ["a", "b"],
                        "trigger": "date",
                        "run_date": one_minute_later.isoformat()})
    assert res.status_code == 200
    assert b'next_run_time' in res.data
