from flask_testing import TestCase
from app.main import _db
from app import blueprint
from app.main import create_app

class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app("test")
        app.register_blueprint(blueprint)
        app.app_context().push()
        return app

    def setUp(self):      
        _db.create_all()
      
    def tearDown(self):
        _db.session.remove()
        _db.drop_all()