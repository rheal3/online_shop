from models.Item import Item
from models.User import User
from main import db
from schemas.ItemSchema import item_schema, items_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

items = Blueprint('items', __name__, url_prefix="/shop")

@items.route("/", methods=["GET"])
def item_index():
    # return all items
    items = Item.query.all()
    return jsonify(items_schema.dump(items))

@items.route("/", methods=["POST"])
@jwt_required
def item_create():
    # create new item
    item_fields = item_schema.load(request.json)
    
    admin = User.query.get(get_jwt_identity())

    if not admin.admin:
        return abort(401, description="Invalid user action.")

    new_item = Item()
    new_item.name = item_fields["name"]
    new_item.description = item_fields["description"]
    new_item.price = round(item_fields["price"], 2)

    db.session.add(new_item)
    db.session.commit()

    return jsonify(item_schema.dump(new_item))

@items.route("/<int:id>", methods=["GET"])
def item_show(id):
    # return a single item
    item = Item.query.get(id)
    return jsonify(item_schema.dump(item))

@items.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def item_update(id):
    # update single item
    admin = User.query.get(get_jwt_identity())

    if not admin.admin:
        return abort(401, description="Invalid user action.")

    items = Item.query.filter_by(id=id)
    item_fields = item_schema.load(request.json)
    items.update(item_fields)
    db.session.commit()

    return jsonify(item_schema.dump(items[0]))

@items.route("/<int:id>", methods=["DELETE"])
@jwt_required
def item_delete(id):
    # delete single item
    admin = User.query.get(get_jwt_identity())

    if not admin.admin:
        return abort(401, description="Invalid user action.")
        
    item = Item.query.get(id)

    if not item:
        return "deleted"
    db.session.delete(item)
    db.session.commit()

    return jsonify(item_schema.dump(item))
