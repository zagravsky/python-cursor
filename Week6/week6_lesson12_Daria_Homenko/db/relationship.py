from flask import Blueprint
from flask.views import MethodView

from db.db_schema import user_schema
from db.db_model import User

one_to_many = Blueprint('one_to_many', __name__, static_folder='../../static', template_folder='../../templates')


class RelationshipView(MethodView):
    def get(self):
        users = User.query.first()
        print(users.news[1].title)
        return user_schema.jsonify(users)


one_to_many.add_url_rule('/one_to_many', view_func=RelationshipView.as_view('one_to_many'))
