from main import db
from flask import Blueprint

# blueprint for db commands
db_commands = Blueprint("db", __name__)

# create tables in db from models
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created.")

# drop all tables from db
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted.")

# seed tables with temp data
@db_commands.cli.command("seed")
def seed_db():
    from models.Item import Item
    from models.User import User
    from models.Order import Order
    from models.OrderShipping import OrderShipping
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()

    for i in range(3):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)

    admin = User()
    admin.email = "admin@test.com"
    admin.password = bcrypt.generate_password_hash("123456").decode("utf-8")
    admin.admin = True
    db.session.add(admin)

    db.session.commit()

    for i in range(10):
        item = Item()
        item.name = faker.currency_name()
        item.description = faker.paragraph(nb_sentences=3)
        item.price = 53.25
        db.session.add(item)
    
    db.session.commit()

    ordershipping = []

    for i in range(5):
        shipping = OrderShipping()
        shipping.first_name = faker.first_name()
        shipping.last_name = faker.last_name()
        shipping.address = faker.street_address()
        shipping.state = faker.city()
        shipping.zip_code = faker.postcode()
        db.session.add(shipping)
        ordershipping.append(shipping)
    
    db.session.commit()

    orders = []

    for i in range(5):
        order = Order()
        order.shipping_id = random.choice(ordershipping).id
        db.session.add(order)
        orders.append(order)

    db.session.commit()

    print("Tables seeded.")