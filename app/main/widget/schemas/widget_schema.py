get_widget_schema =  {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "widget_type": {"type": "string", "minLength": 1},
        "date_added": {"type": "string", "format": "date-time"}
    },
}

get_widgets_schema = {    
    "type": "array",
    "items": get_widget_schema    
}

create_widget_schema = {
     "type": "object",
    "properties": {      
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "widget_type": {"type": "string", "minLength": 1},        
    },
    "required": ["name", "widget_type"]
}

update_widget_schema = {
     "type": "object",
    "properties": {      
        "name": {"type": "string"},
        "description": {"type": "string"},
        "widget_type": {"type": "string"},        
    }
}