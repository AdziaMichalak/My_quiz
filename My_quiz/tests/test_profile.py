import pytest
from quiz.models import User
from quiz.main import profile
from quiz.utilities import total_score



@pytest.fixture
def user():
    return User(id=1, total=1, scores=total_score)

def test_profile():
    assert user