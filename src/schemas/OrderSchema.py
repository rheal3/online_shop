from main import ma
from models.Order import Order
from schemas.OrderShippingSchema import OrderShippingSchema
from datetime import datetime

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

    date_ordered = ma.Date(format='%Y-%m-%d', missing=datetime.now())
    shipped = ma.Boolean(missing=False)
    shipping = ma.Nested(OrderShippingSchema)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)