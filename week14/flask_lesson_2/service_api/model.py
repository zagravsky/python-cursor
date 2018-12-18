from service_api.app_database import db

# ======================= Many to Many Relationship ======================= #
books_char_relation = db.Table('books_char_relation',
                               db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                               db.Column('character_id', db.Integer, db.ForeignKey('character.id'))
                               )


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)


user_books_relation = db.Table('user_books_ralation',
                               db.Column('user_id', db.Integer, db.ForeignKey('user_table.id')),
                               db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
                               )


class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', secondary=user_books_relation, backref=db.backref('users'), lazy='dynamic')


# ======================= One to Many Relationship ======================= #

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='author')
    city = db.Column(db.String)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    characters = db.relationship('Character', secondary=books_char_relation, backref=db.backref('characters'),
                                 lazy='dynamic')


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='genre')


# ======================= One to One Relationship ======================= #

class IdCard(db.Model):
    __tablename__ = 'id_card'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    count_of_books = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    user = db.relationship('User', backref=db.backref('user'))
