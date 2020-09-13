from datetime import datetime
import json
from app.main import _db
from app.main.collectors_item.models.collectors_item_model import CollectorsItemModel
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)

def get_collectors_items():
    logger.debug(">>>>")

    try:
        collectors_item_results = _db.session.query(CollectorsItemModel).all()

        serialized_collectors_items = []
        for collectors_item_result in collectors_item_results:
            serialized_collectors_item = collectors_item_result.serialize()
            serialized_collectors_items.append(serialized_collectors_item)

        return serialized_collectors_items, 200
    except Exception as e:
        logger.exception(e)
        response_object = {
            "status": "failed",
            "message": "an error occurred"
        }
        return response_object, 500

def create_collectors_item(collectors_item_data):
    logger.debug(">>>> collectors_item_data: {}".format(json.dumps(collectors_item_data, indent=2)))
    try:
        new_collectors_item = CollectorsItemModel(
            name=collectors_item_data.get("name"),
            description=collectors_item_data.get("description"),
            collectors_item_type=collectors_item_data.get("collectors_item_type"),
            date_added=datetime.utcnow()
        )

        _db.session.add(new_collectors_item)
        _db.session.commit()

        serialized_collectors_item = new_collectors_item.serialize()

        return serialized_collectors_item, 201
        
    except Exception as e:
        logger.exception(e)
        _db.session.rollback()

        response_object = {
            "status": "failed",
            "message": "failed to create collectors_item"
        }
        return response_object, 500

def update_collectors_item_by_id(collectors_item_id, collectors_item_data):
    logger.debug(">>>> collectors_item_id {}, collectors_item_data: {}".format(collectors_item_id,json.dumps(collectors_item_data, indent=2)))
    try:
        collectors_item_to_update = _db.session.query(CollectorsItemModel).filter(CollectorsItemModel.id == collectors_item_id).first()

        if not collectors_item_to_update:
            error_msg = "collectors_item with id {} not found.".format(collectors_item_id)
            logger.error(error_msg)
            response_object = {
                "status": "failed",
                "message": error_msg
            }
            return response_object, 404

        # allow for partial update by checking each attribute one by one
        if collectors_item_data.get("name"):
            collectors_item_to_update.name = collectors_item_data.get("name")
        
        if collectors_item_data.get("description"):
            collectors_item_to_update.description = collectors_item_data.get("description")
        
        if collectors_item_data.get("collectors_item_type"):
            collectors_item_to_update.description = collectors_item_data.get("collectors_item_type")
        
        _db.session.commit()

        serialized_collectors_item = collectors_item_to_update.serialize()

        return serialized_collectors_item, 200
        
    except Exception as e:
        logger.exception(e)
        _db.session.rollback()

        response_object = {
            "status": "failed",
            "message": "failed to update collectors_item"
        }
        return response_object, 500

def delete_collectors_item_by_id(collectors_item_id):
    logger.debug(">>>> collectors_item_id {}".format(collectors_item_id))
    try:
        collectors_item_to_delete = _db.session.query(CollectorsItemModel).filter(CollectorsItemModel.id == collectors_item_id).first()

        if not collectors_item_to_delete:
            warning_msg = "collectors_item with id {} not found.".format(collectors_item_id)
            logger.warning(error_msg)
            response_object = {
                "status": "success",
                "message": warning_msg
            }
            return response_object, 200
        
        _db.session.delete(collectors_item_to_delete)
        _db.session.commit()

        response_object = {
            "status": "success",
            "message": "collectors_item with id {} successfully deleted".format(collectors_item_id)
        }

        return response_object, 200
        
    except Exception as e:
        logger.exception(e)
        _db.session.rollback()

        response_object = {
            "status": "failed",
            "message": "failed to delete collectors_item with id {}".format(collectors_item_id)
        }
        return response_object, 500