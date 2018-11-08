from flask import Blueprint, request
from flask.views import MethodView

from db.db_schema import flower_schema, flowers_schema
from db.db_app import db
from db.db_model import Flower
flower_api = Blueprint('flower_api', __name__, static_folder='../../static', template_folder='../../templates')


class FlowersView(MethodView):

    def get(self):
        flower = Flower.query.order_by(Flower.id).all()
        return flowers_schema.jsonify(flower)

    def post(self):
        data = request.get_json()
        new_flower = Flower(**data)

        db.session.add(new_flower)
        db.session.commit()
        return flower_schema.jsonify(new_flower)

    def put(self, id):
        data = request.get_json()
        flower_description = data.get("flower_description")

        row = Flower.query.filter_by(id=id).first()
        row.flower_description = flower_description

        db.session.commit()
        return flower_schema.jsonify(row)

    def delete(self, id):
        row = Flower.query.filter_by(id=id).first()

        db.session.delete(row)
        db.session.commit()
        return flower_schema.jsonify(row)


flower_api.add_url_rule('/flower', view_func=FlowersView.as_view('flower_api_api'))
flower_api.add_url_rule('/flower/<id>', view_func=FlowersView.as_view('flower_change'))
