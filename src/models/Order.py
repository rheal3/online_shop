from main import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    date_ordered = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    shipped = db.Column(db.Boolean(), default=False)