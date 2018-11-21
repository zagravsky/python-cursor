from werkzeug.security import generate_password_hash, check_password_hash
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
        self.password_hash = password_hash

    def __repr__(self):
        return '<User {}>'.format(self.username)

class BikeTable(db.Model):
    __tablename__ = 'bikes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    brand = db.Column(db.String(20))
    type = db.Column(db.String(10))
    wheel_size = db.Column(db.String(5))

    def __init__(self, name, brand, type, wheel_size):
        self.name = name
        self.brand = brand
        self.type = type
        self.wheel_size = wheel_size

    def __repr__(self):
        return f"<Bike {self.brand}-{self.name}>"
