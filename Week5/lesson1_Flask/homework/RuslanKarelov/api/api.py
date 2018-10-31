from flask import Blueprint, request, jsonify
from flask.views import MethodView
import json

api = Blueprint('api', __name__)

with open('database/data.json', 'r') as file:
    data = json.load(file)


class MyApi(MethodView):
    def get(self, mineral=None):
        if mineral is None:
            return jsonify(data)
        elif mineral in data:
            return jsonify(data[mineral])
        else:
            return "KeyError"
        
    def post(self):
        added_data = json.loads(request.data.decode('utf-8'))
        data[list(added_data.keys())[0]] = list(added_data.values())[0]
        with open('database/data.json', 'w') as file:
            json.dump(data, file)
        return "Success"

    def delete(self, mineral):
        if mineral in data:
            data.pop(mineral)
            with open('database/data.json', 'w') as file:
                json.dump(data, file)
            return "Success"
        else:
            return "Not found"


test = MyApi.as_view('test_api')
api.add_url_rule('/data/', view_func=test, methods=['GET', 'POST'])
api.add_url_rule('/data/<mineral>', view_func=test, methods=['GET', 'DELETE'])