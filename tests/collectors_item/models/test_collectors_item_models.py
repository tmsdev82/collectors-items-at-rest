from datetime import datetime

from app.main import _db
from app.main.collectors_item.models import collectors_item_model
from tests.base import BaseTestCase


class TestCollectorsItemModel(BaseTestCase):
    def test_create_collectors_item(self):
        collectors_item_dbo = collectors_item_model.CollectorsItemModel(
            name="test_collectors_item",
            description="collectors_item for testing",
            collectors_item_type="ccc2",
            date_added=datetime.utcnow(),
        )

        _db.session.add(collectors_item_dbo)
        _db.session.commit()

        self.assertFalse(collectors_item_dbo.id is None)
    
    def test_serialize_collectors_item(self):
        date_added = datetime.utcnow()
        collectors_item_dbo = collectors_item_model.CollectorsItemModel(
            name="test_collectors_item",
            description="collectors_item for testing",
            collectors_item_type="ccc2",
            date_added=date_added,
        )

        _db.session.add(collectors_item_dbo)
        _db.session.commit()

        serialized_collectors_item = collectors_item_dbo.serialize()

        self.assertEqual(serialized_collectors_item["id"], collectors_item_dbo.id)
        self.assertEqual(serialized_collectors_item["name"], collectors_item_dbo.name)
        self.assertEqual(serialized_collectors_item["description"], collectors_item_dbo.description)
        self.assertEqual(serialized_collectors_item["collectors_item_type"], collectors_item_dbo.collectors_item_type)
        self.assertEqual(serialized_collectors_item["date_added"], str(date_added))

        collectors_item_dbo = collectors_item_model.CollectorsItemModel(
            name="test_collectors_item2",            
            collectors_item_type="ccc2",
            date_added=date_added,
        )

        _db.session.add(collectors_item_dbo)
        _db.session.commit()

        serialized_collectors_item = collectors_item_dbo.serialize()
        self.assertEqual(serialized_collectors_item["id"], collectors_item_dbo.id)
        self.assertEqual(serialized_collectors_item["name"], collectors_item_dbo.name)
        self.assertEqual(serialized_collectors_item["description"], "")
        self.assertEqual(serialized_collectors_item["collectors_item_type"], collectors_item_dbo.collectors_item_type)
        self.assertEqual(serialized_collectors_item["date_added"], str(date_added))