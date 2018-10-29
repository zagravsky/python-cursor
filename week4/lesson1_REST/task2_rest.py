import json

import flask
from flask import Flask
from flask import request


app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_Member(name, age, gender ):
    MEMBERS[name] = {"age": age, "gender": gender, "name": name}
    resp_data = {"jsonrpc": "2.0", "result": f"Your member {MEMBERS[name]} added"}
    return json.dumps(resp_data)


def get_Member(name):
    resp_data = {"jsonrpc": "2.0", "result": MEMBERS[name]}
    return json.dumps(resp_data)


METHODS = {
    "get_Member": get_Member,
    "add_Member": add_Member
}


@app.route('/', methods=['POST'])
def profile():
    param_data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(param_data.get('method'))
    if not method_view:
        return json.dumps('BlaBlaBla')
    else:
        return method_view(**param_data.get('params'))


@app.route('/ping', methods=['POST'])
def ping():
    param_data = json.loads(request.data.decode('utf-8'))
    print(param_data.get('method'))
    if param_data.get('method') == 'ping':
        return json.dumps({"jsonrpc": "2.0", "result": 'ppping'})
    else:
        return json.dumps("error")


if __name__ == '__main__':
    app.run(port=4000, host='127.0.0.1', debug=True)
