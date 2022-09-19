import pytest
from quiz.client import get_me_question
from flask import request 



@pytest.fixture()
def open_trivia():
    resp = request.get(url)
    with open("trivia/") as f:
        return resp.json()

def test_api_trivia():
    assert (open_trivia)