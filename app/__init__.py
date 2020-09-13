from flask_restx import Api
from flask import Blueprint

from app.main.collectors_item.controllers.collectors_item_controller import api as collectors_item_namespace

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="CollectorsItems at rest backend", version="0.1.0", description="RESTful API for managing collectors_items.")

api.add_namespace(collectors_item_namespace)