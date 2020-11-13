from flask_sqlalchemy import SQLAlchemy
import os

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://admin:{os.getenv('DB_PASSWORD')}@localhost:5432/online_shop"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    db = SQLAlchemy(app)
    return db

# from dotenv import load_dotenv
# load_dotenv()
# import psycopg2
# connection = psycopg2.connect(
#     database="online_shop", 
#     user="admin", 
#     password=os.getenv("DB_PASSWORD"), 
#     host="localhost", port=5432)

# cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name VARCHAR, description TEXT, price INT);")
# connection.commit()