from quiz.main import index
from quiz.__init__ import create_app


def test_index():
   app = create_app()
   app.config.update({"TESTING": True})
   assert app