from datetime import datetime
import json
from app.main import _db
from app.main.widget.models.widget_model import WidgetModel
from app.utils import loggers

logger = loggers.get_basic_logger(__name__)

def get_widgets():
    logger.debug(">>>>")

    try:
        widget_results = _db.session.query(WidgetModel).all()

        serialized_widgets = []
        for widget_result in widget_results:
            serialized_widget = widget_result.serialize()
            serialized_widgets.append(serialized_widget)

        return serialized_widgets, 200
    except Exception as e:
        logger.exception(e)
        response_object = {
            "status": "failed",
            "message": "an error occurred"
        }
        return response_object, 500

def create_widget(widget_data):
    logger.debug(">>>> widget_data: {}".format(json.dumps(widget_data, indent=2)))
    try:
        new_widget = WidgetModel(
            name=widget_data.get("name"),
            description=widget_data.get("description"),
            widget_type=widget_data.get("widget_type"),
            date_added=datetime.utcnow()
        )

        _db.session.add(new_widget)
        _db.session.commit()

        serialized_widget = new_widget.serialize()

        return serialized_widget, 201
        
    except Exception as e:
        logger.exception(e)
        _db.session.rollback()

        response_object = {
            "status": "failed",
            "message": "failed to create widget"
        }
        return response_object, 500

def update_widget_by_id(widget_id, widget_data):
    logger.debug(">>>> widget_id {}, widget_data: {}".format(widget_id,json.dumps(widget_data, indent=2)))
    try:
        widget_to_update = _db.session.query(WidgetModel).filter(WidgetModel.id == widget_id).first()

        if not widget_to_update:
            error_msg = "widget with id {} not found.".format(widget_id)
            logger.error(error_msg)
            response_object = {
                "status": "failed",
                "message": error_msg
            }
            return response_object, 404

        # allow for partial update by checking each attribute one by one
        if widget_data.get("name"):
            widget_to_update.name = widget_data.get("name")
        
        if widget_data.get("description"):
            widget_to_update.description = widget_data.get("description")
        
        if widget_data.get("widget_type"):
            widget_to_update.description = widget_data.get("widget_type")
        
        _db.session.commit()

        serialized_widget = widget_to_update.serialize()

        return serialized_widget, 200
        
    except Exception as e:
        logger.exception(e)
        _db.session.rollback()

        response_object = {
            "status": "failed",
            "message": "failed to update widget"
        }
        return response_object, 500

def delete_widget_by_id(widget_id):
    logger.debug(">>>> widget_id {}".format(widget_id))
    try:
        widget_to_delete = _db.session.query(WidgetModel).filter(WidgetModel.id == widget_id).first()

        if not widget_to_delete:
            warning_msg = "widget with id {} not found.".format(widget_id)
            logger.warning(error_msg)
            response_object = {
                "status": "success",
                "message": warning_msg
            }
            return response_object, 200
        
        _db.session.delete(widget_to_delete)
        _db.session.commit()

        response_object = {
            "status": "success",
            "message": "widget with id {} successfully deleted".format(widget_id)
        }

        return response_object, 200
        
    except Exception as e:
        logger.exception(e)
        _db.session.rollback()

        response_object = {
            "status": "failed",
            "message": "failed to delete widget with id {}".format(widget_id)
        }
        return response_object, 500