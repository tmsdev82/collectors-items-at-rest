from flask import request
from flask_restx import Resource, Namespace, reqparse

from app.main.collectors_item.services import collectors_item_service
from app.main.collectors_item.schemas import collectors_item_schema
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)

api = Namespace(
    "collectors_items", description="Represents the collectors_items"
)

get_collectors_items_dto = api.schema_model("GetCollectorsItems", collectors_item_schema.get_collectors_items_schema)
get_collectors_item_dto = api.schema_model("GetCollectorsItem", collectors_item_schema.get_collectors_item_schema)
create_collectors_item_dto = api.schema_model("CreateCollectorsItem", collectors_item_schema.create_collectors_item_schema)
update_collectors_item_dto =  api.schema_model("UpdateCollectorsItem", collectors_item_schema.update_collectors_item_schema)
@api.route("")
class CollectorsItems(Resource):
    @api.doc("Get collectors_items")    
    @api.response(200, "Success", get_collectors_items_dto)    
    def get(self):
        return collectors_item_service.get_collectors_items()
    
    @api.doc("Create a collectors_item")    
    @api.expect(create_collectors_item_dto, validate=True)
    @api.response(201, "Success", get_collectors_item_dto)    
    def post(self):
        collectors_item_data = request.get_json()
        return collectors_item_service.create_collectors_item(collectors_item_data=collectors_item_data)

@api.route("/<collectors_item_id>")
class CollectorsItemById(Resource):
    @api.doc("Update a collectors_item by id")    
    @api.expect(update_collectors_item_dto, validate=True)
    @api.response(200, "Success", get_collectors_item_dto)    
    def put(self, collectors_item_id):
        collectors_item_data = request.get_json()
        return collectors_item_service.update_collectors_item_by_id(collectors_item_id=collectors_item_id,collectors_item_data=collectors_item_data)
    
    @api.doc("Delete a collectors_item by id")        
    @api.response(200, "Successs message")
    def delete(self, collectors_item_id):
        return collectors_item_service.delete_collectors_item_by_id(collectors_item_id=collectors_item_id)