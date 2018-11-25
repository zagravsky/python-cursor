from flask import Blueprint, jsonify, request, render_template
from werkzeug.exceptions import abort

from app.ourdb.ourdb import carbase

apicars = Blueprint('apicars', __name__, template_folder='templates')


@apicars.route('/')
def api_visualisation():
    return render_template('apicars/home.html', carbase=carbase)


@apicars.route("/cars", methods=["GET"])
def get_cars():
    return jsonify({"cars": carbase})


@apicars.route('/cars/<string:car_model>', methods=['GET'])
def get_car(car_model):
    car = list(filter(lambda x: x["Model"] == car_model, carbase))
    if len(car) == 0:
        abort(404)
    return jsonify({'car': car[0]})


@apicars.route("/cars", methods=["POST"])
def add_car():
    if request.method == "POST":
        new_car = {
            "Horsepower": request.form.get("Horsepower"),
            "Mark": request.form.get("Mark"),
            "Model": request.form.get("Model"),
            "Origin": request.form.get("Origin"),
            "Year": request.form.get("Year")
        }
        carbase.append(new_car)
        return jsonify({"cars": carbase})


@apicars.route('/cars/<string:car_model>/delete', methods=['GET'])
def del_car(car_model):
    car = list(filter(lambda t: t['Model'] == car_model, carbase))
    if len(car) == 0:
        abort(404)
    carbase.remove(car[0])
    return jsonify({'result': True})
