from main import ma
from models.Item import Item
from marshmallow.validate import Length, Regexp

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
    
    name = ma.String(required=True, validate=Length(min=1))
    description = ma.String(required=True, validate=Length(min=1))
    price = ma.Float(required=True) # validate=Regexp(r"^[0-9]+(\.[0-9]{0,2})?") << how do I put this in?

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)