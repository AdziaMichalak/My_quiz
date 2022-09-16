import pytest
from quiz.models import User, Score
from quiz.main import terminator
from quiz.utilities import total_score
from flask_login import current_user


@pytest.fixture
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    scores = Score.query.filter_by(user_id=user.id).all()
    total = total_score(user, scores)
    return User(id=1, total=1, scores=total_score)

def test_terminator():
    
    assert user