from main import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    shipping_id = db.Column(db.Integer, db.ForeignKey("ordershipping.id"))
    date_ordered = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    shipped = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return f"<Order {self.id}>"