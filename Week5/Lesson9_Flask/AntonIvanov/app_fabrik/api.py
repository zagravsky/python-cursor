from flask import Blueprint, render_template, request, jsonify, abort, flash, redirect, url_for
from flask.views import MethodView
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegisterForm
from .db import BIKES
from .models import User
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

class RegisterView(MethodView):
    def get(self):
        form = RegisterForm()
        return render_template('register.html', form=form)
    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            user = User(
                {
                    'username': form.username.data,
                    'email': form.email.data,
                    'age': form.age.data,
                    'password_hash': generate_password_hash(form.password.data)
                }
            )
            with open('users.json', 'r') as f:
                USERS = json.load(f)
                user_list= USERS['users']
            if user.username in [elem['username'] for elem in user_list]:
                flash(f'username {user.username} is exists')
                return render_template('register.html', form=form)
            USERS['users'].append({
                'username': user.username,
                'email': user.email,
                'age': user.age,
                'password_hash': user.password_hash
            })
            flash('{} is registered'.format(user.username))
            with open('users.json', 'w') as f:
                json.dump(USERS, f)
            return redirect(url_for('home_api.home_api'))
        return render_template('register.html', form=form)

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
register = Blueprint('register', __name__, static_folder='static', template_folder='templates')
register.add_url_rule('/register', view_func=RegisterView.as_view('register'))
