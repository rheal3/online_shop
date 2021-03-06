from main import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.Float())

    def __repr__(self):
        return f"<Item: {self.id}>"