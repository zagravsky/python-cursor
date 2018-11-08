from flask import Blueprint, request
from flask.views import MethodView

from db.db_schema import user_schema, users_schema
from db.db_app import db
from db.db_model import User
user_api = Blueprint('user_api', __name__, static_folder='../../static', template_folder='../../templates')


class UsersView(MethodView):

    def get(self):
        user = User.query.order_by(User.id).all()
        return users_schema.jsonify(user)

    def post(self):
        data = request.get_json()
        new_user = User(**data)

        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)

    def put(self, id):
        data = request.get_json()
        age = data.get("age")

        row = User.query.filter_by(id=id).first()
        row.age = age

        db.session.commit()
        return user_schema.jsonify(row)

    def delete(self, id):
        row = User.query.filter_by(id=id).first()

        db.session.delete(row)
        db.session.commit()
        return user_schema.jsonify(row)


user_api.add_url_rule('/user', view_func=UsersView.as_view('user_api'))
user_api.add_url_rule('/user/<id>', view_func=UsersView.as_view('user_change'))
