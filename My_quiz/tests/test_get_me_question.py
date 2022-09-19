import mock
import pytest

from quiz import db
from quiz.client import get_me_question
from quiz.utilities import check_answers, total_score
from quiz.models import User

class MockScore:
    def __init__(self, score):
        self.score = score

@pytest.fixture
def user():
    return User(id=1, total=0)


@pytest.fixture
def score():
    return MockScore(score=10)


@mock.patch.object(db.session, "add")
@mock.patch.object(db.session, "commit")
def test_process(add, commit, user, score):
    question = get_me_question()
    assert question["difficulty"] == "easy"

    answer = "My answer"
    check_answers(answer, question, user)
    add.assert_called_once()
    commit.assert_called_once()


    scores = [score, score]
    total = total_score(user, scores)
    assert total == (score.score + score.score)