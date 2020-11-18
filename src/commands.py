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
    from main import bcrypt
    from faker import Faker

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
    print("Tables seeded.")