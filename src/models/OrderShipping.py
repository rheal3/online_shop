from main import db

class OrderShipping(db.Model):
    __tablename__ = "ordershipping"

    id = db.Column(db.Integer, primary_key=True)
    orders = db.relationship("Order", backref="shipping")
    # user = db.relationship("User", backref="user")
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    address = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Shipping To: {self.firstname} {self.lastname}>"