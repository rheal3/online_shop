from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), nullable=True)
    # shipping = db.Column(db.Integer, db.ForeignKey("ordershipping.id"))
    # shipping = db.relationship("OrderShipping", backref="ordershipping.id")

    def __repr__(self):
        return f"<User {self.id}: {self.email}>"