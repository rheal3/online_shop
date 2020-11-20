from models.Order import Order
from schemas.OrderSchema import order_schema, orders_schema
from models.OrderShipping import OrderShipping
from schemas.OrderShippingSchema import order_shipping_schema, orders_shipping_schema
from main import db
from flask import Blueprint, request, jsonify

orders = Blueprint("orders", __name__, url_prefix="/orders")

# admin authorization ?? auth only user who created and admin..
@orders.route("/", methods=["GET"])
def order_index():
    # return all orders
    orders = (Order.query.all(), OrderShipping.query.all())
    return jsonify(orders_schema.dump(orders))

@orders.route("/", methods=["POST"])
def order_create():
    # create new order
    order_fields = order_schema.load(request.json) 

    shipping_id = request.args["shipping_id"]
    shipping_id = OrderShipping.query.filter_by(id=shipping_id).first()

    new_order = Order()
    new_order.date_ordered = order_fields["date_ordered"]
    new_order.shipped = order_fields["shipped"]

    shipping_id.orders.append(new_order)
    db.session.commit()

    return jsonify(order_schema.dump(new_order))

@orders.route("/<int:id>", methods=["GET"])
def order_show(id):
    # return single order
    order = Order.query.get(id)
    return jsonify(order_schema.dump(order))

@orders.route("/shipping", methods=["POST"])
def shipping_create():
    # create new shipping details
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
