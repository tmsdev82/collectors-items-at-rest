from datetime import datetime

from app.main import _db
from app.main.widget.models import widget_model
from tests.base import BaseTestCase


class TestWidgetModel(BaseTestCase):
    def test_create_widget(self):
        widget_dbo = widget_model.WidgetModel(
            name="test_widget",
            description="widget for testing",
            widget_type="ccc2",
            date_added=datetime.utcnow(),
        )

        _db.session.add(widget_dbo)
        _db.session.commit()

        self.assertFalse(widget_dbo.id is None)
    
    def test_serialize_widget(self):
        date_added = datetime.utcnow()
        widget_dbo = widget_model.WidgetModel(
            name="test_widget",
            description="widget for testing",
            widget_type="ccc2",
            date_added=date_added,
        )

        _db.session.add(widget_dbo)
        _db.session.commit()

        serialized_widget = widget_dbo.serialize()

        self.assertEqual(serialized_widget["id"], widget_dbo.id)
        self.assertEqual(serialized_widget["name"], widget_dbo.name)
        self.assertEqual(serialized_widget["description"], widget_dbo.description)
        self.assertEqual(serialized_widget["widget_type"], widget_dbo.widget_type)
        self.assertEqual(serialized_widget["date_added"], str(date_added))

        widget_dbo = widget_model.WidgetModel(
            name="test_widget2",            
            widget_type="ccc2",
            date_added=date_added,
        )

        _db.session.add(widget_dbo)
        _db.session.commit()

        serialized_widget = widget_dbo.serialize()
        self.assertEqual(serialized_widget["id"], widget_dbo.id)
        self.assertEqual(serialized_widget["name"], widget_dbo.name)
        self.assertEqual(serialized_widget["description"], "")
        self.assertEqual(serialized_widget["widget_type"], widget_dbo.widget_type)
        self.assertEqual(serialized_widget["date_added"], str(date_added))