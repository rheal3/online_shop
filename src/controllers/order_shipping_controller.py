from models.Order import Order
from schemas.OrderSchema import order_schema, orders_schema
from models.OrderShipping import OrderShipping
from schemas.OrderShippingSchema import order_shipping_schema, orders_shipping_schema
from main import db
from flask import Blueprint, request, jsonify

order_shipping = Blueprint("order_shipping", __name__, url_prefix="/order_shipping")

@order_shipping.route("/", methods=["POST"])
def shipping_create():
    # create new order
    shipping_fields = order_shipping_schema.load(request.json) 

    new_shipping = OrderShipping()
    new_shipping.address = shipping_fields["address"]
    new_shipping.state = shipping_fields["state"]
    new_shipping.zip_code = shipping_fields["zip_code"]
    new_shipping.first_name = shipping_fields["first_name"]
    new_shipping.last_name = shipping_fields["last_name"]


    db.session.add(new_shipping)    
    db.session.commit()

    return jsonify(order_shipping_schema.dump(new_shipping))
