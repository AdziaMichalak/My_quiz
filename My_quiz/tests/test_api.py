import pytest
from quiz.__init__ import create_app
import mock
from quiz.models import User


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

@mock.patch("quiz.db_manager.get_all_users", return_value=[User(id=1)])
def test_api(get_all, client):
    response = client.get("/")
    assert response.status_code == 200
    assert get_all.call_count == 1