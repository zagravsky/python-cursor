from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask import current_app
from .db import BIKES
import json


class FabrikApiView(MethodView):
    def get(self):
        deb_status = current_app.config.get("DEBUG")
        test_var = current_app.config.get("TEST_VARIABLE")
        sess_lifetime = current_app.config.get("PERMANENT_SESSION_LIFETIME")
        return f'{test_var} DEBUG = {deb_status}, PERMANENT_SESSION_LIFETIME = {sess_lifetime}'


class BikesView(MethodView):
    def get(self, name=None):
        if name is None:
            return jsonify(BIKES)
        elif name in [elem['name'] for elem in BIKES]:
            for i, elem in enumerate(BIKES):
                if elem['name'] == name:
                    return jsonify(BIKES[i])
        else:
            return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})

    def post(self):
        params = json.loads(request.data.decode('utf-8'))
        BIKES.append(params)
        return jsonify({"status": "OK", "message": f"Add new bikes {params}"})

    def delete(self, name: str):
        if name in [elem['name'] for elem in BIKES]:
            for i, elem in enumerate(BIKES):
                if elem['name'] == name:
                    return jsonify(BIKES.pop(i))
        else:
            return jsonify({"status": "Fail", "message": "I don't know about such bike. Sorry"})


#
factory_api = Blueprint('factory_api', __name__, static_folder='static', template_folder='templates')
factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))
# Task1
bike_api = Blueprint('bikes_api', __name__)
bike_api.add_url_rule('/bike', view_func=BikesView.as_view('bikes_api'))
bike_api.add_url_rule('/bike/<string:name>', view_func=BikesView.as_view('bike_api'))
