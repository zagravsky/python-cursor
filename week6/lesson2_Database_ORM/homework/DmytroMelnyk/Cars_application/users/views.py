from flask import Blueprint, render_template, url_for, flash
from flask.views import MethodView
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import redirect

from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application import bcrypt
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.db.app_database import db
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.models import UserTable
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.users.forms import LoginForm, RegistrationForm

users = Blueprint('users', __name__)


class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('login_page.html', title='Login', form=form)

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = UserTable.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash(f'Hello, {user}', 'success')
                return redirect(url_for('main.home'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login_page.html', title='Login', form=form)


class RegView(MethodView):
    def get(self):
        form = RegistrationForm()
        return render_template('register_page.html', title='Register', form=form)

    def post(self):
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = UserTable(username=form.username.data, userage=form.userage.data, email=form.email.data,
                             password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('users.login'))
        return render_template('register_page.html', title='Register', form=form)


class LogOutView(MethodView):
    def get(self):
        logout_user()
        return redirect(url_for('main.home'))


class AccountView(MethodView):
    @login_required
    def get(self):
        return render_template('account_page.html', title='Account')


users.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])
users.add_url_rule('/register', view_func=RegView.as_view('register'), methods=['GET', 'POST'])
users.add_url_rule('/logout', view_func=LogOutView.as_view('logout'), methods=['GET'])
users.add_url_rule('/account', view_func=AccountView.as_view('account'), methods=['GET'])
