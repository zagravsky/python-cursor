from flask import Blueprint, request
from flask.views import MethodView

from service_api.app_database import db
from service_api.model import Genre
from service_api.shema import genre_schema, genres_schema

genre_api = Blueprint('genre', __name__, static_folder='../../static', template_folder='../../template')


class GenreView(MethodView):
    """
    Genre Views
    """

    def get(self):
        character = Genre.query.all()
        return genres_schema.jsonify(character)

    def post(self):
        data = request.get_json()
        new_genre = Genre(**data)

        db.session.add(new_genre)
        db.session.commit()
        return genre_schema.jsonify(new_genre)


genre_api.add_url_rule('/genre', view_func=GenreView.as_view('genre'))
