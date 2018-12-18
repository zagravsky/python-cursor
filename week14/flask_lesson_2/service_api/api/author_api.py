from flask import Blueprint, request
from flask.views import MethodView

from service_api.app_database import db
from service_api.model import Author
from service_api.shema import author_schema, authors_schema

author_api = Blueprint('author', __name__, static_folder='../../static', template_folder='../../template')


class AuthorView(MethodView):
    """
    Author Views
    """

    def get(self):
        authors = Author.query.all()
        return authors_schema.jsonify(authors)

    def post(self):
        data = request.get_json()
        new_author = Author(**data)

        db.session.add(new_author)
        db.session.commit()
        return author_schema.jsonify(new_author)


author_api.add_url_rule('/author', view_func=AuthorView.as_view('author'))
