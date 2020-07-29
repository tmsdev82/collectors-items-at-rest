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