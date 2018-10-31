from flask import Blueprint, render_template
import json
home = Blueprint('home', __name__, template_folder='./templates', static_folder='./static')


@home.route('/')
def home_page():
    return render_template('home.html')

@home.route('/list')
def list_of_product():
    with open('database/data.json', 'r') as file:
        data = json.load(file)
    return render_template('listWithMin.html', data=data)


@home.route('/list/<path:dat>')
def data(dat):
    with open('database/data.json', 'r') as file:
        data = json.load(file)
    for key in data.keys():
        if dat == key:
            return render_template('mineral.html', data=data[dat])
    return "Error"
