from flask import Blueprint, render_template, request, jsonify
from flask.views import MethodView
from flask import current_app
from .db import BIKES
import json


class FabrikApiView(MethodView):
    def get(self):
        deb_status = current_app.config.get("DEBUG")
        test_var = current_app.config.get("TEST_VARIABLE")
        return  f'{test_var} DEBUG={deb_status}'

class TestView(MethodView):
    def get(self):
        return render_template("test.html")

class HomeView(MethodView):
    def get(self):
        return render_template("home.html",data=BIKES)

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


factory_api = Blueprint('factory_api', __name__, static_folder='static', template_folder='templates')
factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))

bike_api = Blueprint('bikes_api', __name__)
bike_api.add_url_rule('/bike', view_func=BikesView.as_view('bikes_api'))
bike_api.add_url_rule('/bike/<string:name>', view_func=BikesView.as_view('bike_api'))

test_api = Blueprint('test_api', __name__, static_folder='static', template_folder='templates')
test_api.add_url_rule('/test', view_func=TestView.as_view('test_api'))

home_api = Blueprint('home_api', __name__, static_folder='static',template_folder='templates')
home_api.add_url_rule('/', view_func=HomeView.as_view('home_api'))