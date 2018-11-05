from db_config import db

class Book(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)