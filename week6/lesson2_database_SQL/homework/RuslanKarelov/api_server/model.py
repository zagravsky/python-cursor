from database.data import db


class CarsTable(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80))
    model = db.Column(db.String(120))
    car_body = db.Column(db.String(80))
    fuel = db.Column(db.String(80))
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, name, model, car_body, fuel, price, date):
        self.name = name
        self.model = model
        self.car_body = car_body
        self.fuel = fuel
        self.price = price
        self.date = date
