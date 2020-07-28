from flask_restx import Api
from flask import Blueprint

from app.main.widget.controllers.widget_controller import api as widget_namespace

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="Widgets at rest backend", version="0.1.0", description="RESTful API for managing widgets.")

api.add_namespace(widget_namespace)