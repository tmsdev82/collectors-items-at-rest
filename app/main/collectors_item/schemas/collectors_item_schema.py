get_collectors_item_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "collectors_item_type": {"type": "string", "minLength": 1},
        "date_added": {"type": "string", "format": "date-time"},
    },
    "required": ["id", "name", "description", "collectors_item_type", "date_added"],
}

get_collectors_items_schema = {"type": "array", "items": get_collectors_item_schema}

create_collectors_item_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "collectors_item_type": {"type": "string", "minLength": 1},
    },
    "required": ["name", "collectors_item_type"],
}

update_collectors_item_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "collectors_item_type": {"type": "string"},
    },
}