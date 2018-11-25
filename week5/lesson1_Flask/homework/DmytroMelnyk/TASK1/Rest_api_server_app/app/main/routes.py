from flask import render_template, make_response, jsonify

from app import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Welcome')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
