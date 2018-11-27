from werkzeug.security import generate_password_hash
from .app_database import db


class UsersTable(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(40))
    age = db.Column(db.INTEGER)
    password_hash = db.Column(db.String(100))

    def __init__(self, username, email, age, password_hash):
        self.username = username
        self.email = email
        self.age = age
        self.password_hash = generate_password_hash(password_hash)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class BrandsTable(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    bikes = db.relationship('BikeTable', backref='brand', passive_deletes='all')

    def __init__(self, name):
        self.name = name


class BikeTable(db.Model):
    __tablename__ = 'bikes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    bike_type = db.Column(db.String(10))
    wheel_size = db.Column(db.String(5))

    def __init__(self, name, brand_id, bike_type, wheel_size):
        self.name = name
        self.brand_id = brand_id
        self.bike_type = bike_type
        self.wheel_size = wheel_size

    def __repr__(self):
        return f"<Bike {self.brand}-{self.name}>"
