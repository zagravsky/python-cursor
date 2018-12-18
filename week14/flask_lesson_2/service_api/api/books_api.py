from flask import Blueprint, request, jsonify
from flask.views import MethodView
from sqlalchemy import func

from service_api.app_database import db

from service_api.model import Book, Character, Author, Genre
from service_api.shema import book_schema, books_schema

books_api = Blueprint('books', __name__, static_folder='../../static', template_folder='../../template')


class BooksView(MethodView):
    """
    Books Views
    """

    def get(self):
        page = request.args.get('page')
        per_page = request.args.get('per_page')

        if not (page or per_page):
            books = Book.query.all()
        else:
            books = Book.query.paginate(per_page=int(per_page), page=int(page)).items

        return books_schema.jsonify(books)

    def post(self):
        data = request.get_json()
        author = data.get("author")
        genre = data.get("genre")
        name = data.get("book_name")

        new_genre = Genre.query.filter_by(name=genre).first()
        if not new_genre:
            new_genre = Genre(name=genre)
            db.session.add(new_genre)

        new_author = Author.query.filter_by(name=author).first()
        if not new_author:
            new_author = Author(name=author)
            db.session.add(new_author)

        new_book = Book(name=name, author=new_author, genre=new_genre)

        db.session.add(new_book)
        db.session.commit()
        return book_schema.jsonify(new_book)


class AddCharacter(MethodView):

    def post(self):
        data = request.get_json()
        book_name = data.get('book_name')
        character = data.get('character')

        book = Book.query.filter_by(name=book_name).first()
        new_character = Character(name=character)

        db.session.add(new_character)
        book.characters.append(new_character)
        db.session.commit()

        return "Sucsessfuly"


class GetBooksFilteredByGenre(MethodView):

    def get(self):
        books = db.session.query(Book.name, Genre.name, Author.name) \
            .join(Genre, Book.genre_id == Genre.id).filter_by(name="fantasy") \
            .join(Author, Book.author_id == Author.id).order_by(Author.name).all()
        return jsonify(books)


class GetBritishAuthors(MethodView):

    def get(self):
        books = db.session.query(Book.name).join(Author, Book.author_id == Author.id).filter_by(city="England").all()
        return jsonify(books)


class GetBookOfOneOfTwoAuthors(MethodView):

    def get(self):
        books = db.session.query(Book.name) \
            .join(Author, Book.author_id == Author.id) \
            .filter((Author.name == "Lewis Carroll") | (Author.name == "Dan Brown")).all()
        return jsonify(books)


class GetCountOfAuthorBooks(MethodView):

    def get(self):
        books_count = db.session.query(Book).join(Author, Book.author_id == Author.id).filter_by(
            name="Dan Brown").count()
        return jsonify(books_count)


books_api.add_url_rule('/books', view_func=BooksView.as_view('books'))
books_api.add_url_rule('/add_character', view_func=AddCharacter.as_view('add_character'))
books_api.add_url_rule('/get_british_authors', view_func=GetBritishAuthors.as_view('get_british_authors'))
books_api.add_url_rule('/get_books_filtered_by_genre',
                       view_func=GetBooksFilteredByGenre.as_view('get_books_filtered_by_genre'))
books_api.add_url_rule('/get_book_of_one_of_two_authors',
                       view_func=GetBookOfOneOfTwoAuthors.as_view('get_book_of_one_of_two_authors'))
books_api.add_url_rule('/get_count_of_author_books',
                       view_func=GetCountOfAuthorBooks.as_view('get_count_of_author_books'))
