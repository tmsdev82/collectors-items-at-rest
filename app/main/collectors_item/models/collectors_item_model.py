from app.main import _db

class CollectorsItemModel(_db.Model):
    __tablename__ = "collectors_items"
    id = _db.Column(_db.Integer, primary_key=True, autoincrement=True)
    name = _db.Column(_db.String(255), unique=True, nullable=False)
    description = _db.Column(_db.String(255), unique=False, nullable=True)
    collectors_item_type = _db.Column(_db.String(50), unique=False, nullable=False)
    date_added = _db.Column(_db.DateTime, nullable=False)

    def serialize(self):
        description = self.description
        if not description:
            description = ""
        serialized = {
            "id": self.id,
            "name": self.name,
            "description": description,
            "collectors_item_type": self.collectors_item_type,
            "date_added": str(self.date_added)
        }

        return serialized
