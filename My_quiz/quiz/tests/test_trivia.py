from quiz.client import get_me_question


def test_trivia():
    question = get_me_question()
    assert question