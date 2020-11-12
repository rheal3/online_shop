from database import cursor, connection

from flask import Flask
app = Flask(__name__)
from items import items
app.register_blueprint(items)


