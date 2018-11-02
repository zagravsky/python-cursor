from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class MovieTable(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_title = db.Column(db.String(80))
    year = db.Column(db.Integer)
    country = db.Column(db.String(80))
    info = db.Column(db.Text)

    def __init__(self, movie_title, year, country, info):
        self.movie_title = movie_title
        self.year = year
        self.country = country
        self.info = info


class UserTable(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(255))
    age = db.Column(db.Integer)
    email = db.Column(db.String(180))

    def __init__(self, name, password, age, email):
        self.name = name
        self.password = password
        self.age = age
        self.email = email


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'movie_title', 'year', 'country')


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
