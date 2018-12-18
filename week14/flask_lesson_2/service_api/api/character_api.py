from flask import Blueprint, request
from flask.views import MethodView

from service_api.app_database import db
from service_api.model import Character
from service_api.shema import character_schema, characters_schema

character_api = Blueprint('character', __name__, static_folder='../../static', template_folder='../../template')


class CharacterView(MethodView):
    """
    Character Views
    """

    def get(self):
        character = Character.query.all()
        return characters_schema.jsonify(character)

    def post(self):
        data = request.get_json()
        new_character = Character(**data)

        db.session.add(new_character)
        db.session.commit()
        return character_schema.jsonify(new_character)


character_api.add_url_rule('/character', view_func=CharacterView.as_view('character'))
