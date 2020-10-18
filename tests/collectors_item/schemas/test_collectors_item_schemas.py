from jsonschema import Draft7Validator as d7val
import pytest
from datetime import datetime

from app.main.collectors_item.schemas.collectors_item_schema import (
    get_collectors_item_schema,
    create_collectors_item_schema,
    get_collectors_items_schema,
    update_collectors_item_schema,
)


@pytest.mark.parametrize(
    "create_data",
    [
        (
            {
                "name": "test1",
                "description": "test creation",
                "collectors_item_type": "testtype1",
            }
        ),
        (
            {
                "name": "test1",
                "collectors_item_type": "testtype1",
            }
        ),
    ],
)
def test_valid_create_collectors_item_schema(create_data):
    d7val(create_collectors_item_schema).validate(create_data)


@pytest.mark.parametrize(
    "create_data",
    [
        (
            {
                "description": "test creation",
                "collectors_item_type": "testtype1",
            }
        ),
        (
            {
                "name": "test1",
                "description": "test creation",
            }
        ),
        (
            {
                "description": "test creation",
            }
        ),
    ],
)
def test_invalid_create_collectors_item_schema(create_data):
    assert d7val(create_collectors_item_schema).is_valid(create_data) is False


@pytest.mark.parametrize(
    "update_data",
    [
        (
            {
                "name": "test1",
                "description": "test creation",
                "collectors_item_type": "testtype1",
            }
        ),
        (
            {
                "name": "test1",
                "collectors_item_type": "testtype1",
            }
        ),
        (
            {
                "name": "test1",
            }
        ),
        (
            {
                "collectors_item_type": "testtype1",
            }
        ),
        (
            {
                "description": "test creation",
            }
        ),
    ],
)
def test_valid_update_collectors_item_schema(update_data):
    d7val(update_collectors_item_schema).validate(update_data)


@pytest.mark.parametrize(
    "get_data",
    [
        (
            [
                {
                    "id": 1,
                    "name": "test1",
                    "description": "test creation",
                    "collectors_item_type": "testtype1",
                    "date_added": str(datetime.utcnow()),
                },
                {
                    "id": 2,
                    "name": "test2",
                    "description": "test creation2",
                    "collectors_item_type": "testtype2",
                    "date_added": str(datetime.utcnow()),
                },
            ]
        ),
        ([]),
    ],
)
def test_valid_get_collectors_items_schema(get_data):
    d7val(get_collectors_items_schema).validate(get_data)


@pytest.mark.parametrize(
    "get_data",
    [
        (
            [
                {
                    "name": "test1",
                    "description": "test creation",
                    "collectors_item_type": "testtype1",
                    "date_added": str(datetime.utcnow()),
                },
                {
                    "id": 2,
                    "name": "test2",
                    "description": "test creation2",
                    "collectors_item_type": "testtype2",
                    "date_added": str(datetime.utcnow()),
                },
            ]
        ),
        (
            [
                {
                    "id": 1,
                    "description": "test creation",
                    "collectors_item_type": "testtype1",
                    "date_added": str(datetime.utcnow()),
                },
            ]
        ),
        (
            [
                {
                    "id": 1,
                    "name": "test1",
                    "collectors_item_type": "testtype1",
                    "date_added": str(datetime.utcnow()),
                },
            ]
        ),
        (
            [
                {
                    "id": 1,
                    "name": "test1",
                    "description": "test creation",
                    "date_added": str(datetime.utcnow()),
                },
            ]
        ),
        (
            [
                {
                    "id": 1,
                    "name": "test1",
                    "description": "test creation",
                    "collectors_item_type": "testtype1",
                },
            ]
        ),
    ],
)
def test_invalid_get_collectors_items_schema(get_data):
    assert d7val(get_collectors_items_schema).is_valid(get_data) is False