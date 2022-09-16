
from quiz.__init__ import create_app


def test_create_app():
    app = create_app()
    app.config.update({"TESTING": True})
    assert app
