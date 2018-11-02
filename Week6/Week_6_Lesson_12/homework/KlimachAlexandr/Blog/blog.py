from flask import Blueprint, render_template, abort
from Blog.database.db import MovieTable

blog = Blueprint('blog', __name__)


@blog.route('/')
def home_page():
    return render_template('blog/home.html')


@blog.route('/products')
def products():
    movie_list = MovieTable.query.order_by(MovieTable.movie_title).all()
    return render_template('blog/products.html', data=movie_list)


@blog.route('/products/<int:id>')
def post(id):
    movie = MovieTable.query.filter_by(id=id).first()
    if movie:
        return render_template('blog/post.html', movie=movie)
    abort(404)
