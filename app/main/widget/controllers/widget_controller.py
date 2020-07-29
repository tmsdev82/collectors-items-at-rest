from flask import request
from flask_restx import Resource, Namespace, reqparse

from app.main.widget.services import widget_service
from app.main.widget.schemas import widget_schema
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)

api = Namespace(
    "widgets", description="Represents the widgets"
)

get_widgets_dto = api.schema_model("GetWidgets", widget_schema.get_widgets_schema)
get_widget_dto = api.schema_model("GetWidget", widget_schema.get_widget_schema)
create_widget_dto = api.schema_model("CreateWidget", widget_schema.create_widget_schema)

@api.route("")
class Widgets(Resource):
    @api.doc("Get widgets")    
    @api.response(200, "Success", get_widgets_dto)    
    def get(self):
        return widget_service.get_widgets()
    
    @api.doc("Create a widget")    
    @api.expect(create_widget_dto, validate=True)
    @api.response(201, "Success", get_widget_dto)    
    def post(self):
        widget_data = request.get_json()
        return widget_service.create_widget(widget_data=widget_data)