from app import app
from flask import request, jsonify, render_template, make_response
from werkzeug.exceptions import abort
from ourdb.ourdb import carbase


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', carbase=carbase)


@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify({"cars": carbase})


@app.route('/cars/<string:car_model>', methods=['GET'])
def get_car(car_model):
    car = list(filter(lambda x: x["Model"] == car_model, carbase))
    if len(car) == 0:
        abort(404)
    return jsonify({'car': car[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
