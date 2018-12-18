from flask import Blueprint, request
from flask.views import MethodView

from service_api.app_database import db
from service_api.model import User
from service_api.shema import user_schema, users_schema

user_api = Blueprint('user', __name__, static_folder='../../static', template_folder='../../template')


class UserView(MethodView):
    """
    User Views
    """

    def get(self):
        character = User.query.all()
        return users_schema.jsonify(character)

    def post(self):
        data = request.get_json()
        new_user = User(**data)

        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)


user_api.add_url_rule('/user', view_func=UserView.as_view('user'))
