from task_2 import app
from flask import request, render_template, url_for, flash, session
from task_2 import bcrypt
from task_2.forms import RegistrationForm, LoginForm, PostForm
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from task_2.dictDB.ourbase import get_db, rewrite_db, get_users_db, rewrite_users_db


@app.route("/")
def mainPage():
    return render_template('index.html', title='Index Page')


@app.route("/home")
def home():
    return render_template('home.html', title='Home Page')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/cars", methods=["GET"])
def get_cars():
    if session.get('logged_in'):
        carbase = get_db()
        return render_template('list_of_products.html', carbase=carbase, title='List of cars Page')
    else:
        session.clear()
        flash('Please, Log In at first!', 'danger')
        return redirect(url_for('login'))


@app.route('/cars/<string:car_model>', methods=['GET'])
def get_car(car_model):
    if session.get('logged_in'):
        carbase = get_db()
        find_car_model = list(filter(lambda x: x["Model"] == car_model, carbase))
        if len(find_car_model) == 0:
            abort(404)
        return render_template('car.html', car=find_car_model[0], title=find_car_model[0]['Model'])
    else:
        session.clear()
        flash('Please, Log In at first!', 'danger')
        return redirect(url_for('login'))


@app.route("/create", methods=['POST', 'GET'])
def create_car():
    if session.get('logged_in'):
        form = PostForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                new_car = {"Model": form.Model.data, "Mark": form.Mark.data, "Horsepower": form.Horsepower.data,
                           "Year": form.Year.data, "Origin": form.Origin.data}
                carbase = get_db()
                carbase.append(new_car)
                rewrite_db(carbase)
                flash(f'New Car {new_car["Model"]} successfully added!', 'success')
                return redirect(url_for('get_cars'))

        return render_template('create_car.html', form=form)
    else:
        session.clear()
        flash('Please, Log In at first!', 'danger')
        return redirect(url_for('login'))


@app.route('/cars/<string:car_model>/delete', methods=['DELETE', 'POST'])
def del_car(car_model):
    if session.get('logged_in'):
        carbase = get_db()
        car = list(filter(lambda t: t['Model'] == car_model, carbase))
        if len(car) == 0:
            abort(404)
        carbase.remove(car[0])
        rewrite_db(carbase)
        flash(f'The {car[0]["Model"]} was successfully deleted!', 'success')
        return redirect(url_for('get_cars'))
    else:
        session.clear()
        flash('Please, Log In at first!', 'danger')
        return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html', title='Error'), 404


@app.route('/newsfeed')
def redirect_undone():
    return redirect(url_for('error_call'))


@app.route('/error_call')
def error_call():
    abort(404)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for("home"))
    users = get_users_db()
    form = LoginForm()
    if form.validate_on_submit():
        for d in users:
            if d["email"] == form.email.data:
                try:
                    bcrypt.check_password_hash(d["password"], form.password.data)
                except:
                    flash('Login Unsuccessful. Please check your password', 'danger')

                session.permanent = True
                session['logged_in'] = True
                session['username'] = d["username"]
                session['_flashes'] = []
                flash(f'You are now logged in as {d["username"]}', 'success')
                return redirect(url_for("home"))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('logged_in'):
        return redirect(url_for("home"))
    users = get_users_db()
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_to_save = {
            "username": form.username.data,
            "userage": form.userage.data,
            "email": form.email.data,
            "password": hashed_password
        }
        if len(users) == 0:
            users.append(user_to_save)
            rewrite_users_db(users)
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        else:
            for d in users:
                if d["username"] == form.username.data:
                    flash('That username is taken. Please choose a different one.', 'danger')
                    return redirect(url_for('register'))
                elif d["email"] == form.email.data:
                    flash('That email is registered. Please choose a different one. Or LogIn', 'danger')
                    return redirect(url_for('login'))
                else:
                    users.append(user_to_save)
                    rewrite_users_db(users)
                    flash('Your account has been created! You are now able to log in', 'success')
                    return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    session.clear()
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))


@app.route("/account")
def account():
    if session.get('logged_in'):
        return render_template('account.html', title='Account')
    else:
        session.clear()
        flash('Please, Log In at first!', 'danger')
        return redirect(url_for('login'))
