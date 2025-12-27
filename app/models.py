from app import db


class Pizza(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    type = db.Column(db.Text,nullable = False)
    price = db.Column(db.Integer,nullable = False)
    image_path = db.Column(db.Text,nullable = False)



class Drink(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    type = db.Column(db.Text,nullable = False)
    price = db.Column(db.Integer,nullable = False)
    image_path = db.Column(db.Text,nullable = False)


class Salad(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.Text, nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=False)
    client = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)