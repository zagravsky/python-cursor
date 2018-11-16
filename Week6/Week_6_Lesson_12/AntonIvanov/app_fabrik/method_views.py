from flask import Blueprint, render_template, abort, flash, redirect, url_for, session, request, current_app
from flask.views import MethodView
from werkzeug.security import generate_password_hash
from .forms import RegisterForm, LoginForm
from functools import wraps
from .db import BIKES
from .models import User
import json


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            flash('Login or register to get access to this page')
            return redirect(url_for('home.home'))
        return f(*args, **kwargs)
    return decorated_function


class HomeView(MethodView):
    def get(self):
        return render_template("home.html")


class ProductListView(MethodView):
    @login_required
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
                user_list = USERS['users']
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
            return redirect(url_for('home.home'))
        return render_template('register.html', form=form)


class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('login.html', form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            with open('users.json', 'r') as f:
                user_list = json.load(f)['users']
            user_models_list = [User(i) for i in user_list]
            for user in user_models_list:
                if form.username.data == user.username and user.check_password(form.password.data):
                    session.permanent = True
                    session['username'] = user.username
                    flash('{} is loged in'.format(user.username))
                    return redirect(url_for('home.home'))
            flash("Username or password is incorrect")
        return render_template('login.html', form=form)

class LogoutView(MethodView):
    def get(self):
        session.clear()
        flash('You logged out')
        return redirect(url_for('home.home'))


test_methods_dict = ['Black Box Testing', 'White Box Testing']


class TestView(MethodView):
    def get(self):
        if session.get('mode') == "Test Config":
            return render_template('test_methods.html', values=test_methods_dict)
        mode = session.get('mode')
        return f'You are in {mode} mode. To get access to this page enter in TEST mode'

# Task 2
home = Blueprint('home', __name__, static_folder='static', template_folder='templates')
home.add_url_rule('/', view_func=HomeView.as_view('home'))
#
products = Blueprint('products', __name__, static_folder='static', template_folder='templates')
products.add_url_rule('/products', view_func=ProductListView.as_view('products'))
products.add_url_rule('/products/<string:name>', view_func=ProductListView.as_view('bike'))
# Task 3, 4
register = Blueprint('register', __name__, static_folder='static', template_folder='templates')
register.add_url_rule('/register', view_func=RegisterView.as_view('register'))

login = Blueprint('login', __name__, static_folder='static', template_folder='templates')
login.add_url_rule('/login', view_func=LoginView.as_view('login'))

logout = Blueprint('logout', __name__, static_folder='static', template_folder='templates')
logout.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
#Task 5
test = Blueprint('test', __name__, static_folder='static', template_folder='templates')
test.add_url_rule('/test', view_func=TestView.as_view('test'))
