import json
from datetime import datetime

from tests.base import BaseTestCase
from app.main.collectors_item.models import collectors_item_model
from app.main import _db


def create_dummy_collectors_items(date_added):
    collectors_item_dbo = collectors_item_model.CollectorsItemModel(
        name="test_collectors_item",
        description="collectors_item for testing",
        collectors_item_type="ccc2",
        date_added=date_added,
    )

    _db.session.add(collectors_item_dbo)
    _db.session.commit()


def get_collectors_items(self):
    return self.client.get("/collectors_items", content_type="application/json")


def create_collectors_item(self, collectors_item_data):
    return self.client.post(
        "/collectors_items",
        data=json.dumps(collectors_item_data),
        content_type="application/json",
    )


def update_collectors_item(self, collectors_item_id, collectors_item_data):
    return self.client.put(
        "/collectors_items/{}".format(collectors_item_id),
        data=json.dumps(collectors_item_data),
        content_type="application/json",
    )


def delete_collectors_item(self, collectors_item_id):
    return self.client.delete(
        "/collectors_items/{}".format(collectors_item_id),
        content_type="application/json",
    )


class TestCollectorsItemController(BaseTestCase):
    def test_create_collectors_items(self):
        collectors_item_data = {
            "name": "test1",
            "description": "test creation",
            "collectors_item_type": "testtype1",
        }
        with self.client:
            response = create_collectors_item(self, collectors_item_data)
            self.assertEqual(response.status_code, 201)

            actual_result = json.loads(response.data.decode())
            self.assertEqual(actual_result["id"], 1)
            self.assertEqual(actual_result["name"], "test1")
            self.assertEqual(actual_result["description"], "test creation")
            self.assertEqual(actual_result["collectors_item_type"], "testtype1")

    def test_get_collectors_items(self):
        date_added = datetime.utcnow()
        create_dummy_collectors_items(date_added)
        with self.client:
            response = get_collectors_items(self)
            self.assertEqual(response.status_code, 200)
            expected_result = [
                {
                    "id": 1,
                    "name": "test_collectors_item",
                    "description": "collectors_item for testing",
                    "collectors_item_type": "ccc2",
                    "date_added": str(date_added),
                }
            ]

            actual_result = json.loads(response.data.decode())
            self.assertEqual(actual_result, expected_result)

    def test_update_collectors_items(self):
        date_added = datetime.utcnow()
        create_dummy_collectors_items(date_added)
        with self.client:
            update_item_data = {
                "name": "updated_name",
                "description": "updated description",
                "collectors_item_type": "updated_type",
            }
            response = update_collectors_item(self, 1, update_item_data)
            self.assertEqual(response.status_code, 200)

            actual_result = json.loads(response.data.decode())
            self.assertEqual(actual_result["id"], 1)
            self.assertEqual(actual_result["name"], "updated_name")
            self.assertEqual(actual_result["description"], "updated description")
            self.assertEqual(actual_result["collectors_item_type"], "updated_type")

    def test_update_collectors_items_no_items(self):
        date_added = datetime.utcnow()
        with self.client:
            update_item_data = {
                "name": "updated_name",
                "description": "updated description",
                "collectors_item_type": "updated_type",
            }
            response = update_collectors_item(self, 1, update_item_data)
            self.assertEqual(response.status_code, 404)

            actual_result = json.loads(response.data.decode())
            self.assertEqual(actual_result["status"], "failed")

    def test_delete_collectors_item(self):
        date_added = datetime.utcnow()
        create_dummy_collectors_items(date_added)
        with self.client:

            response = delete_collectors_item(self, 1)
            self.assertEqual(response.status_code, 200)

            actual_result = json.loads(response.data.decode())
            self.assertEqual(actual_result["status"], "success")

    def test_delete_collectors_item_no_items(self):
        date_added = datetime.utcnow()
        with self.client:

            response = delete_collectors_item(self, 1)
            self.assertEqual(response.status_code, 200)

            actual_result = json.loads(response.data.decode())
            self.assertEqual(actual_result["status"], "success")
