from flask import request, jsonify, render_template, url_for, flash
from task_2 import app
from task_2.forms import RegistrationForm, LoginForm
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

# app = Flask(__name__)

carbase = [{"Model": "Chevelle Malibu", "Mark": "Chevrolet", "Horsepower": 130, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "Skylark 320", "Mark": "Buick", "Horsepower": 165, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "Satellite", "Mark": "Plymouth", "Horsepower": 150, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "Torino", "Mark": "Ford", "Horsepower": 140, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "DS-21 Pallas", "Mark": "Citroen", "Horsepower": 115, "Year": "1970-01-01", "Origin": "Europe"},
           {"Model": "Mustang gl", "Mark": "Ford", "Horsepower": 86, "Year": "1982-01-01", "Origin": "USA"},
           {"Model": "VW", "Mark": "Pickup", "Horsepower": 52, "Year": "1982-01-01", "Origin": "Europe"}]


@app.route("/")
def mainPage():
    return render_template('mainPage.html')


@app.route("/home")
def home():
    return render_template('home.html', title='Home Page')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# @app.route('/List of product page')
@app.route("/cars", methods=["GET"])
def get_cars():
    return render_template('list_of_products.html', carbase=carbase, title='List of cars Page')
    # return jsonify({"cars": carbase})


@app.route('/cars/<string:car_model>', methods=['GET'])
def get_car(car_model):
    find_car_model = list(filter(lambda x: x["Model"] == car_model, carbase))
    if len(find_car_model) == 0:
        abort(404)
    return render_template('car.html', car=find_car_model[0], title=find_car_model[0]['Model'])
    # return jsonify({'car': find_car_model[0]})


@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html', title='Error'), 404
    # return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/newsfeed')
def redirect_undone():
    return redirect(url_for('error_call'))


@app.route('/error_call')
def error_call():
    abort(404)


@app.route("/cars", methods=["POST"])
def add_car():
    if not request.json or not 'Model' in request.json:
        abort(400)
    carbase.append(request.json)
    return jsonify({"car": request.json}), 201


@app.route('/cars/<string:car_model>', methods=['DELETE'])
def del_car(car_model):
    car = list(filter(lambda t: t['Model'] == car_model, carbase))
    if len(car) == 0:
        abort(404)
    carbase.remove(car[0])
    return jsonify({'result': True})


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)