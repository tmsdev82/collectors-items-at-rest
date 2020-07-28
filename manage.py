import os

from app.main import create_app
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)
app_environment = os.getenv("FLASK_APP_ENV", "dev")
logger.info("Creating app for environment: {}".format(app_environment))
logger.info("Logging level is set to: {}".format(os.getenv("LOGGING_LEVEL", "DEBUG")))
app = create_app(app_environment)

if __name__ == "__main__":
    app.run(threaded=True)