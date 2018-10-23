from flask import Flask, request, jsonify, render_template, make_response
from werkzeug.exceptions import abort

from api import api

app = Flask(__name__)

app.register_blueprint(api)

carbase = [{"Model": "Chevelle Malibu", "Mark": "Chevrolet", "Horsepower": 130, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "Skylark 320", "Mark": "Buick", "Horsepower": 165, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "Satellite", "Mark": "Plymouth", "Horsepower": 150, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "Torino", "Mark": "Ford", "Horsepower": 140, "Year": "1970-01-01", "Origin": "USA"},
           {"Model": "DS-21 Pallas", "Mark": "Citroen", "Horsepower": 115, "Year": "1970-01-01", "Origin": "Europe"},
           {"Model": "Mustang gl", "Mark": "Ford", "Horsepower": 86, "Year": "1982-01-01", "Origin": "USA"},
           {"Model": "VW", "Mark": "Pickup", "Horsepower": 52, "Year": "1982-01-01", "Origin": "Europe"}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', carbase=carbase)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify({"cars": carbase})


@app.route('/cars/<string:car_model>', methods=['GET'])
def get_car(car_model):
    if len(list(filter(lambda x: x["Model"] == car_model, carbase))) == 0:
        abort(404)
    return jsonify({'car': carbase[0]})


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


if __name__ == '__main__':
    app.run(debug=True)
