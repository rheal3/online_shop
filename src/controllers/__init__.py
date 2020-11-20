from controllers.items_controller import items
from controllers.auth_controller import auth
from controllers.orders_controller import orders

registerable_controllers = [
    auth, 
    items,
    orders
    ]