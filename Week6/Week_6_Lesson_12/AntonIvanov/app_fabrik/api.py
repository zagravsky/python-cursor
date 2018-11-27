from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask import current_app
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from .app_database import db
from .model import BikeTable, BrandsTable
from .schema import bike_schema, bikes_schema


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
            return bikes_schema.jsonify(bikes)
        else:
            bike = BikeTable.query.filter_by(id=id).first()
            if bike is not None:
                result = bike_schema.dump(bike).data
                result['brand_name'] = bike.brand.name
                return jsonify(result)
        return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})

    def post(self):
        data = request.get_json()
        brand = BrandsTable.query.filter_by(name=data['brand']).first()
        if brand is None:
            brand = BrandsTable(data['brand'])
            db.session.add(brand)
        new_bike = BikeTable(data['name'], brand.id, data['bike_type'], data['wheel_size'])
        db.session.add(new_bike)
        db.session.commit()
        print(new_bike.brand.name)
        result = bike_schema.dump(new_bike).data
        return jsonify({"status": "OK", "new_bike": result})

    def delete(self, id: int):
        # bike = BikeTable.query.filter_by(id=id).first()
        # if bike is not None:
        #     db.session.delete(bike)
        #     db.session.commit()
        #     result = bike_schema.dump(bike).data
        #     return jsonify({"status": "OK", "deleted_bike": result})
        # else:
        #     return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})
        try:
            bike = BikeTable.query.filter_by(id=id).one()
            print(bike)
            db.session.delete(bike)
            db.session.commit()
            result = bike_schema.dump(bike).data
            return jsonify({"status": "OK", "deleted_bike": result})
        except MultipleResultsFound as e:
            return jsonify({"status": "Fail", "message": e})
        except NoResultFound as e:
            return jsonify({"status": "Fail", "message": e})

    def put(self, id):
        bike = BikeTable.query.filter_by(id=id).first()
        if bike is not None:
            data = request.get_json()
            brand_id = data.get("brand_id")
            name = data.get("name")
            bike_type = data.get("bike_type")
            wheel_size = data.get("wheel_size")
            if brand_id is not None:
                bike.brand_id = brand_id
            if name is not None:
                bike.name = name
            if bike_type is not None:
                bike.bike_type = bike_type
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
