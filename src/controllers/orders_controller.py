from models.Order import Order
from schemas.OrderSchema import order_schema, orders_schema
from main import db
from flask import Blueprint, request, jsonify

orders = Blueprint("orders", __name__, url_prefix="/orders")

# admin authorization ?? auth only user who created and admin..
@orders.route("/", methods=["GET"])
def order_index():
    # return all orders
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders))

@orders.route("/", methods=["POST"])
def order_create():
    # create new order
    order_fields = order_schema.load(request.json)

    new_order = Order()
    new_order.date_ordered = order_fields["date_ordered"]
    new_order.shipped = order_fields["shipped"]

    db.session.add(new_order)
    db.session.commit()

    return jsonify(order_schema.dump(new_order))

@orders.route("/<int:id>", methods=["GET"])
def order_show(id):
    # return single order
    order = Order.query.get(id)
    return jsonify(order_schema.dump(order))
