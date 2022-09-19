import pytest
from quiz.models import User, Score
from quiz.main import terminator
from quiz.utilities import total_score
from flask_login import current_user


@pytest.fixture
def user():
    return User(id=1, total=1, scores=total_score)

def test_terminator():
    assert user