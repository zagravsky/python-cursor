from flask import Blueprint, render_template, url_for, abort, session, redirect

from db.db_app import db
from db.db_model import User, Flower, News
from forms import LoginForms, Sign_inForm
from datetime import timedelta


pages_view = Blueprint('pages_view', __name__, template_folder='templates', static_folder='static')


@pages_view.route("/homework_home")
def home_page():
    session_id = session.get('username', 'UNKNOWN USER')
    news_data = News.query.all()
    return render_template('home.html', data=news_data, session_id=session_id)


@pages_view.route('/list_of_flowers')
def list_of_flowers_page():
    flowers = Flower.query.all()
    return render_template('list_of_flowers.html', data=flowers, title='List of flowers',
                           session_id=session['username'])


@pages_view.route("/list_of_flowers/flower/<string:flower_name>")
def flower_page(flower_name):
    flower = Flower.query.filter_by(flower_name=flower_name).first()
    return render_template('flower.html', flower_name=flower.flower_name, flower_image=flower.flower_image,
                            flower_meaning=flower.flower_description, title='Flower', session_id=session['username'])


@pages_view.route("/flower_error")
def test_redirect():
    abort(404, "Value error")


@pages_view.errorhandler(404)
def error_404(error):
    return render_template("error_404.html")


@pages_view.route('/')
@pages_view.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForms()
    if login_form.validate_on_submit():
        log_user = User.query.filter_by(name=login_form.username.data).first()
        if log_user.password == login_form.password.data:
                session['username'] = login_form.username.data
                return redirect(url_for('pages_view.home_page'))
        else:
            redirect(url_for('page_view.sign_in'))
    return render_template("login.html", title="Login", form=login_form)


@pages_view.before_request
def make_session_permanent():
    session.permanent = True
    pages_view.permanent_session_lifetime = timedelta(minutes=1)


@pages_view.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('pages_view.login'))


@pages_view.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    sign_in_form = Sign_inForm()
    login_form = LoginForms()
    if sign_in_form.validate_on_submit():

        new_user = User(name=sign_in_form.s_username.data, age=sign_in_form.s_age.data,
                        email=sign_in_form.s_email.data, password=sign_in_form.s_password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('pages_view.login', title="Login", form=login_form))

    return render_template("sign_in.html", title="Sign_in", form=sign_in_form)
