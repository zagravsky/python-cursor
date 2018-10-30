from flask import Blueprint, render_template, request, jsonify, abort, flash, redirect, url_for
from flask.views import MethodView
from flask import current_app
from .forms import LoginForm
from .db import BIKES, USERS
import json


class FabrikApiView(MethodView):
    def get(self):
        deb_status = current_app.config.get("DEBUG")
        test_var = current_app.config.get("TEST_VARIABLE")
        return f'{test_var} DEBUG={deb_status}'


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


class HomeView(MethodView):
    def get(self):
        return render_template("home.html")

class ProductListView(MethodView):
    def get(self, name=None):
        bike_names = [elem['name'] for elem in BIKES]
        if name is None:
            return render_template("products.html", data=bike_names)
        elif name in bike_names:
            for i, elem in enumerate(BIKES):
                if elem['name'] == name:
                    return render_template("bike.html", data=BIKES[i])
        else:
            return abort(404)

def page_not_found(e):
    return render_template("error404.html"), 404

class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('login.html', form=form)
    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            flash('{}, remember me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('home_api.home_api'))
        return render_template('login.html', form=form)

#
factory_api = Blueprint('factory_api', __name__, static_folder='static', template_folder='templates')
factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))
# Task1
bike_api = Blueprint('bikes_api', __name__)
bike_api.add_url_rule('/bike', view_func=BikesView.as_view('bikes_api'))
bike_api.add_url_rule('/bike/<string:name>', view_func=BikesView.as_view('bike_api'))
# Task 2
home_api = Blueprint('home_api', __name__, static_folder='static',template_folder='templates')
home_api.add_url_rule('/', view_func=HomeView.as_view('home_api'))
#
products_api = Blueprint('products_api', __name__, static_folder='static', template_folder='templates')
products_api.add_url_rule('/products', view_func=ProductListView.as_view('products_api'))
products_api.add_url_rule('/products/<string:name>', view_func=ProductListView.as_view('bike'))
# Task 3
login_api = Blueprint('login_api', __name__, static_folder='static', template_folder='templates')
login_api.add_url_rule('/login', view_func=LoginView.as_view('login_api'))
