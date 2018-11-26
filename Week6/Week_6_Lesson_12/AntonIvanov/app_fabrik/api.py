from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask import current_app
from .app_database import db
from .model import BikeTable
from .schema import bike_schema, bikes_schema
import json


class FabrikApiView(MethodView):
    def get(self):
        deb_status = current_app.config.get("DEBUG")
        test_var = current_app.config.get("TEST_VARIABLE")
        sess_lifetime = current_app.config.get("PERMANENT_SESSION_LIFETIME")
        return f'{test_var} DEBUG = {deb_status}, PERMANENT_SESSION_LIFETIME = {sess_lifetime}'


class BikesView(MethodView):
    def get(self, id=None):
        if id is None:
            bikes = BikeTable.query.all()
            result = bikes_schema.dump(bikes).data
            return jsonify(result)
        else:
            bike = BikeTable.query.filter_by(id=id).first()
            if bike is not None:
                result = bike_schema.dump(bike).data
                return jsonify(result)
        return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})

    def post(self):
        data = request.get_json()
        try:
            new_bike = BikeTable(**data)
            db.session.add(new_bike)
            db.session.commit()
            result = bike_schema.dump(new_bike).data
            return jsonify({"status": "OK", "newbike": result})
        except TypeError as e:
            return jsonify({"status": "Fail", "message": str(e)})

    def delete(self, id: int):
        bike = BikeTable.query.filter_by(id=id).first()
        if bike is not None:
            db.session.delete(bike)
            db.session.commit()
            result = bike_schema.dump(bike).data
            return jsonify({"status": "OK", "deleted_bike": result})
        else:
            return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})

    def put(self, id):
        bike = BikeTable.query.filter_by(id=id).first()
        if bike is not None:
            data = request.get_json()
            brand = data.get("brand")
            name = data.get("name")
            type = data.get("type")
            wheel_size = data.get("wheel_size")
            if brand is not None:
                bike.brand = brand
            if name is not None:
                bike.name = name
            if type is not None:
                bike.type = type
            if wheel_size is not None:
                bike.wheel_size = wheel_size
            db.session.commit()
            result = bike_schema.dump(bike).data
            return jsonify({"status": "OK", "updated_bike": result})
        return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})








#
factory_api = Blueprint('factory_api', __name__, static_folder='static', template_folder='templates')
factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))
# Task1
bike_api = Blueprint('bikes_api', __name__)
bike_api.add_url_rule('/bike', view_func=BikesView.as_view('bikes_api'))
bike_api.add_url_rule('/bike/<int:id>', view_func=BikesView.as_view('bike_api'))
