from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.main.config import config_by_name
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)
_db = SQLAlchemy()

def create_app(config_name):
    logger.debug(">>>> config_name: {}".format(config_name))

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    _db.init_app(app)    
    CORS(app)

    return app