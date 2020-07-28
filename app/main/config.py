import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", "the_best_secret_key")

class DevelopmentConfig(Config):  
    DEBUG = True  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "development.db")

class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"

config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig)

key = Config.SECRET_KEY