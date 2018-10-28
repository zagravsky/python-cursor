from flask import Blueprint, render_template, abort
from Blog.database.db import get_db

blog = Blueprint('blog', __name__)


@blog.route('/')
def home_page():
    return render_template('blog/home.html')


@blog.route('/products')
def products():
    db = get_db()
    return render_template('blog/products.html', data=db)


@blog.route('/products/<int:id>')
def post(id):
    db = get_db()
    for movie, info in db['data'].items():
        if info.get('id') == id:
            return render_template('blog/post.html', movie=movie, info=info)
    abort(404)
