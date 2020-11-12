from database import cursor, connection
from flask import Blueprint, request, jsonify
items = Blueprint('items', __name__)

@items.route("/shop", methods=["GET"])
def item_index():
    # return all items
    sql = "SELECT * FROM items;"
    cursor.execute(sql)
    items = cursor.fetchall()
    return jsonify(items)

@items.route("/shop", methods=["POST"])
def item_create():
    # create new item
    sql = "INSERT INTO items (name, description, price) VALUES (%s, %s, %s);"
    cursor.execute(sql, (request.json["name"], request.json["description"], request.json["price"]))
    connection.commit()

    sql = "SELECT * FROM items ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    items = cursor.fetchone()
    return jsonify(items)


@items.route("/shop/<int:id>", methods=["GET"])
def item_show(id):
    # return a single item
    sql = "SELECT * FROM items WHERE id = %s;"
    cursor.execute(sql, (id,))
    items = cursor.fetchone()
    return jsonify(items)

@items.route("/shop/<int:id>", methods=["PUT", "PATCH"])
def item_update(id):
    # update single item
    sql = "UPDATE items SET name = %s, description = %s, price = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["name"], request.json["description"], request.json["price"], id))
    connection.commit()

    sql = "SELECT * FROM items WHERE id = %s"
    cursor.execute(sql, (id,))
    items = cursor.fetchone()
    return jsonify(items)

@items.route("/shop/<int:id>", methods=["DELETE"])
def item_delete(id):
    # delete single item
    sql = "SELECT * FROM items WHERE id = %s;"
    cursor.execute(sql, (id,))
    items = cursor.fetchone()

    if items:
        sql = "DELETE FROM items WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(items)

