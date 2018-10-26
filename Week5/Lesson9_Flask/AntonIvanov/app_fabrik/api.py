from flask import Blueprint, render_template, request, jsonify
from flask.views import MethodView

from flask import current_app
from .db import BIKES

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

factory_api = Blueprint('factory_api', __name__, static_folder='static', template_folder='templates')
factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))

test_api = Blueprint('test_api', __name__, static_folder='static', template_folder='templates')
test_api.add_url_rule('/test', view_func=TestView.as_view('test_api'))

home_api = Blueprint('home_api', __name__, static_folder='static',template_folder='templates')
home_api.add_url_rule('/', view_func=HomeView.as_view('home_api'))