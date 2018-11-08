from flask_login import UserMixin

from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application import login_manager
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.db.app_database import db


@login_manager.user_loader
def load_user(user_id):
    return UserTable.query.get(int(user_id))


class UserTable(db.Model, UserMixin):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    userage = db.Column(db.Integer)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # :TODO загрукза аватарки
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, userage, email, password):
        self.username = username
        self.userage = userage
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User {self.username}'


class CarTable(db.Model):
    __tablename__ = "cars_table"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    model = db.Column(db.String(80), nullable=False)
    mark = db.Column(db.String(80), nullable=False)
    horsepower = db.Column(db.Integer)
    year = db.Column(db.String(10))
    origin = db.Column(db.String(80))

    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # :TODO загрукза авто картинки

    def __init__(self, model, mark, horsepower, year, origin):
        self.model = model
        self.mark = mark
        self.horsepower = horsepower
        self.year = year
        self.origin = origin

    def __repr__(self):
        return f'<{self.model} {self.mark}>'
