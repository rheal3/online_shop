from main import ma
from models.OrderShipping import OrderShipping

class OrderShippingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderShipping

    address = ma.String(required=True)
    state = ma.String(required=True)
    zip_code = ma.Integer(required=True)
    first_name = ma.String(required=True)
    last_name = ma.String(required=True)

order_shipping_schema = OrderShippingSchema()
orders_shipping_schema = OrderShippingSchema()
