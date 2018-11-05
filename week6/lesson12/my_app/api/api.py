from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from db_config import db
from model import Book
from shema import book_schema,books_schema

user_api = Blueprint('user_api', __name__, static_folder='../static', template_folder='../template')

@user_api.route('/', methods=["GET", "POST"])
def home():

    if request.method=="POST":
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
        db.session.rollback()
        return redirect("/")
    if request.method=="GET":
        books = None
        books = Book.query.all()
        return render_template("home.html", books=books)

@user_api.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
        db.session.rollback()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")

@user_api.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    db.session.rollback()
    return redirect("/")

@user_api.route('/book/<int:id>')
def get_book(id):
    book = Book.query.filter_by(id=id).first()

    return book_schema.jsonify(book)



@user_api.route("/books")
def get_books():
    books = Book.query.order_by(Book.title).all()
    return books_schema.jsonify(books)