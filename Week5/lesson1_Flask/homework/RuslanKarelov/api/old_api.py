from flask import Blueprint, request
import json

api = Blueprint('home_page', __name__)

with open('database/data.json', 'r') as file:
    data = json.load(file)


def add_data():
    new_data = json.loads(request.data.decode('utf-8'))
    data[list(new_data.keys())[0]] = list(new_data.values())[0]
    return "You added new data"


def delete_data(key):
    for a in data.keys():
        if key == a:
            data.pop(key)
            return f"You delete {key} from your database"
    return "Your data does not exist"


def get_one(key):
    if key in data:
        return json.dumps(data[key])
    else:
        return f"{key} does not exist"


@api.route('/data', methods=['GET', 'POST'])
def all_data():
    if request.method == 'GET':
        return json.dumps(data)
    if request.method == 'POST':
        return add_data()


@api.route('/data/<key>', methods=['GET', 'DELETE'])
def new_data(key):
    if request.method == 'DELETE':
        return delete_data(key)
    if request.method == 'GET':
        return get_one(key)
