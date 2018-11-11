from flask import Blueprint, request
from flask.views import MethodView

from database.data import db

from api_server.model import CarsTable
from api_server.schema import cars_schema, car_schema


api = Blueprint('api_server', __name__, template_folder='./templates', static_folder='./static')


class UserView(MethodView):

    def get(self):
        cars = CarsTable.query.order_by(CarsTable.id).all()
        return cars_schema.jsonify(cars)

    def post(self):
        data = request.get_json()
        new_data = CarsTable(**data)

        db.session.add(new_data)
        db.session.commit()
        return car_schema.jsonify(new_data)

    def put(self, id):
        data = request.get_json()
        new_price = data.get("price")

        element_from_db = CarsTable.query.filter_by(id=id).first()
        element_from_db.price = new_price
        db.session.commit()
        return car_schema.jsonify(element_from_db)

    def delete(self, id):
        data = CarsTable.query.filter_by(id=id).first()

        db.session.delete(data)
        db.session.commit()
        return f"Your data {car_schema.jsonify(data)} was deleted"


class CreateDataBase(MethodView):

    def post(self):
        db.create_all()
        db.session.commit()
        return "Database are created"


view = UserView.as_view('api_server')
api.add_url_rule('/cars', view_func=view, methods=['GET', 'POST'])
api.add_url_rule('/create', view_func=CreateDataBase.as_view('create_db'), methods=['POST'])
api.add_url_rule('/cars/<id>', view_func=view, methods=['DELETE', 'PUT'])
