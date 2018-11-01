from flask import render_template
from app.app import app, time


@app.route("/")
def index():

    return render_template('index.html', time=time, title='Python')

@app.route("/C++")
def route_to_c_plus():
    return render_template('C_plus.html', time=time, title='C++')
