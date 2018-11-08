from flask import request, Blueprint
from flask.views import MethodView

from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.api.schema import car_schema, cars_schema
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.db.app_database import db
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.models import CarTable

car_api = Blueprint('car_api', __name__)


class CarapiView(MethodView):
    """
    CRUD User View
    """

    def get(self, id=None):
        """
        SELECT * FROM user_table ORDER BY id:
        :return:
        """
        if id is None:
            car = CarTable.query.order_by(CarTable.id).all()

            return cars_schema.jsonify(car)

        else:
            row = CarTable.query.filter_by(id=id).first()

            return car_schema.jsonify(row)

    def post(self):
        data = request.get_json()

        new_user = CarTable(**data)

        db.session.add(new_user)
        db.session.commit()

        return car_schema.jsonify(new_user)

    def put(self, id):
        data = request.get_json()
        username = data.get("username")
        age = data.get('age')
        email = data.get('email')
        password = data.get('password')

        row = CarTable.query.filter_by(id=id).first()
        row.username = username
        row.age = age
        row.email = email
        row.password = password

        db.session.commit()

        return car_schema.jsonify(row)

    def delete(self, id):
        row = CarTable.query.filter_by(id=id).first()

        db.session.delete(row)
        db.session.commit()

        return car_schema.jsonify(row)


car_api.add_url_rule('/api/cars', view_func=CarapiView.as_view('cars_api'))
car_api.add_url_rule('/api/cars/<id>', view_func=CarapiView.as_view('car_api'))
