from flask import Blueprint, render_template, url_for, flash
from flask.views import MethodView
from flask_login import login_required
from werkzeug.utils import redirect

from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.cars.forms import AddCarForm
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.db.app_database import db
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.models import CarTable

cars = Blueprint('cars', __name__)


class AddNewCarsView(MethodView):
    @login_required
    def get(self):
        form = AddCarForm()
        return render_template('create_car.html', form=form)

    @login_required
    def post(self):
        form = AddCarForm()
        if form.validate_on_submit():
            new_car = CarTable(model=form.model.data, mark=form.mark.data, horsepower=form.horsepower.data,
                               year=form.year.data, origin=form.origin.data)
            db.session.add(new_car)
            db.session.commit()
            flash(f'New Car {new_car.mark} {new_car.model} successfully added!', 'success')
            return redirect(url_for('cars.get_cars'))

        return render_template('create_car.html', form=form)


class CarsView(MethodView):
    @login_required
    def get(self):
        cars = CarTable.query.order_by(CarTable.id).all()
        return render_template('list_of_products.html', carbase=cars, title='List of cars Page')


class CarView(MethodView):
    @login_required
    def get(self, car_model):
        car = CarTable.query.filter_by(model=car_model).first()
        return render_template('car_page.html', car=car, title=f'{car.model} {car.mark} Page')


cars.add_url_rule('/cars/<string:car_model>', view_func=CarView.as_view('get_car'), methods=['GET'])
cars.add_url_rule('/cars', view_func=CarsView.as_view('get_cars'), methods=['GET'])
cars.add_url_rule('/create', view_func=AddNewCarsView.as_view('create_car'), methods=['GET', 'POST'])
