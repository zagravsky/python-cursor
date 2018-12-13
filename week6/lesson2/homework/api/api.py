from flask import Blueprint, request, json
from flask.views import MethodView

from homework.app_database import db

from homework.shema import owner_schema, owners_schema
from homework.model import Owners

user_api = Blueprint('user_api', __name__, static_folder='../../static', template_folder='../../template')

class UserView(MethodView):

    def get(self):
        user = Owners.query.order_by(Owners.id).all()
        return owners_schema.jsonify(user)

    def post(self):
        data = json.loads(request.data.decode())  # request.get_json() не работал, как в курсе
        new_user = Owners(**data)

        db.session.add(new_user)
        db.session.commit()
        return owner_schema.jsonify(data)

user_api.add_url_rule('/user', view_func=UserView.as_view('user_api'))
user_api.add_url_rule('/user/<name>', view_func=UserView.as_view('user_change'))