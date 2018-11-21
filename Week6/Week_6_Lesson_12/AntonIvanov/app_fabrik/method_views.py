from flask import Blueprint, render_template, abort, flash, redirect, url_for, session, request, current_app
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegisterForm, LoginForm
from functools import wraps
from .app_database import db
from .model import UsersTable, BikeTable


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
        bike_names = BikeTable.query.with_entities(BikeTable.name).order_by(BikeTable.name).all()
        bike_names = [i[0] for i in bike_names]
        if name is None:
            print(bike_names)
            return render_template("products.html", data=bike_names)
        elif name in bike_names:
            query = BikeTable.query.filter_by(name=name).first()
            return render_template("bike.html", data=query)
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
            query = UsersTable.query.filter_by(username=form.username.data).first()
            if query is None:
                user = UsersTable(form.username.data, form.email.data, form.age.data,
                                  generate_password_hash(form.password.data))
                db.session.add(user)
                db.session.commit()
                flash(f'{user.username} is registered')
                return redirect(url_for('home.home'))
            else:
                flash(f'username {form.username.data} is exists')
                return render_template('register.html', form=form)
        return render_template('register.html', form=form)


class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('login.html', form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            query = UsersTable.query.filter_by(username=form.username.data).first()
            if query and check_password_hash(query.password_hash, form.password.data):
                session.permanent = True
                session['username'] = form.username.data
                flash(f'{form.username.data} is logged in')
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
# Task 5
test = Blueprint('test', __name__, static_folder='static', template_folder='templates')
test.add_url_rule('/test', view_func=TestView.as_view('test'))
