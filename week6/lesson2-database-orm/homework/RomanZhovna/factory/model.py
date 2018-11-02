from factory.flask_db import db


class PlayersTable(db.Model):
    __tablename__ = 'players_table'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    age = db.Column(db.INTEGER)
    club = db.Column(db.String(50))

    def __init__(self, full_name, age, club):
        self.full_name = full_name
        self.age = age
        self.club = club
