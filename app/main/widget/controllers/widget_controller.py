from flask import request
from flask_restx import Resource, Namespace, reqparse

from app.main.widget.services import widget_service
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)

api = Namespace(
    "widgets", description="Represents the widgets"
)

@api.route("")
class Widgets(Resource):
    @api.doc("Get widgets")    
    @api.response(200, "Returns a List of widgets")    
    def get(self):
        return widget_service.get_widgets()