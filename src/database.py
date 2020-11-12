from dotenv import load_dotenv
load_dotenv()
import os
import psycopg2

connection = psycopg2.connect(
    database="online_shop", 
    user="admin", 
    password=os.getenv("DB_PASSWORD"), 
    host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name VARCHAR, description TEXT, price INT);")
connection.commit()