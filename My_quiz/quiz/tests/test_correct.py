import pytest
from quiz.models import User, Score
from quiz.main import correct
from flask_login import current_user
from quiz.utilities import check_answers, total_score
from flask import session, request


@pytest.fixture
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    scores = Score.query.filter_by(user_id=user.id).all()
    total = total_score(user, scores)
    return User(id=1, total=1, scores=total_score)


def test_correct():
    
    assert check_answers

