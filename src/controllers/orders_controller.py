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

    shipping = OrderShipping.query.get(orders)

    new_order = Order()
    new_order.date_ordered = order_fields["date_ordered"]
    new_order.shipped = order_fields["shipped"]

    db.session.add(new_order)
    db.session.commit()

    return jsonify(order_schema.dump(new_order))


    # shipping_fields = orders_shipping_schema.load(request.json)
    # shipping = OrderShipping()
    # shipping.address = shipping_fields["address"]
    # shippping.state = shipping_fields["state"]
    # shipping.zip_code = shipping_fields["zip_code"]
    # shipping.first_name = shipping_fields["first_name"]
    # shipping.last_name = shipping_fields["last_name"]

    # db.session.add(shipping)
    # return jsonify(orders_shipping_schema(shipping))



@orders.route("/<int:id>", methods=["GET"])
def order_show(id):
    # return single order
    order = Order.query.get(id)
    return jsonify(order_schema.dump(order))
