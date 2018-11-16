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
        self.usename = username
        self.email = email
        self.age = age
        self.password_hash = password_hash


class User:
    def __init__(self,user):
        self.username = user['username']
        self.password_hash = user['password_hash']
        self.email = user['email']
        self.age = user['age']

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
