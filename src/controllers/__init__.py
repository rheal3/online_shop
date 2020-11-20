from controllers.items_controller import items
from controllers.auth_controller import auth
from controllers.orders_controller import orders
from controllers.order_shipping_controller import order_shipping

registerable_controllers = [
    auth, 
    items,
    orders,
    order_shipping
]