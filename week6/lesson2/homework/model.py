from homework.app_database import db

class Owners(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.INTEGER)
    address = db.Column(db.String(80))
    car_car = db.relationship('aboutCar', backref='carrier')

    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address


class aboutCar(db.Model):
    __tablename__ = 'about_car'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    price = db.Column(db.Integer)
    carrier_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __init__(self, year, price, model):
        self.year = year
        self.price = price
        self.model = model