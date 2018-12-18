from flask import Blueprint, request
from flask.views import MethodView

from service_api.app_database import db
from service_api.model import IdCard
from service_api.shema import id_card_schema, id_cards_schema

id_card = Blueprint('id_card', __name__, static_folder='../../static', template_folder='../../template')


class IdCardView(MethodView):
    """
    IdCard Views
    """

    def get(self):
        character = IdCard.query.all()
        return id_cards_schema.jsonify(character)

    def post(self):
        data = request.get_json()
        new_user = IdCard(**data)

        db.session.add(new_user)
        db.session.commit()
        return id_card_schema.jsonify(new_user)


id_card.add_url_rule('/id_card', view_func=IdCardView.as_view('id_card'))
