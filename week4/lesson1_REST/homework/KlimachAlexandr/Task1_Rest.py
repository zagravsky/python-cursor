import json

import flask
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()


@app.route('/user', methods=['POST'])
@app.route('/user/<name>', methods=['GET', 'PATCH', 'DELETE'])
def profile(name: str = None):
    result = {}

    if flask.request.method == 'POST':
        params = json.loads(request.data.decode('utf-8'))
        MEMBERS[params.get("name")] = params
        result = {"status": "OK", "message": f"Add new user {params}"}

    if flask.request.method == 'GET':
        member = MEMBERS.get(name)
        if member is None:
            result = {"status": "Fail", "error": f"Could not find member with name {name}"}
        else:
            result = {"status": "OK", "message": f"We find your user {member}"}

    if flask.request.method == 'PATCH':
        member = MEMBERS.get(name)
        if member is None:
            result = {"status": "Fail", "message": "I dont know about such user. Sorry"}
        else:
            params = json.loads(request.data.decode('utf-8'))
            MEMBERS[name].update(params)
            result = {"status": "Ok", "message": f"This is your new member {MEMBERS.get(name)}"}

    if flask.request.method == 'DELETE':
        if not check_member(name):
            result = {"status": "Fail", "message": "I dont know about such user. Sorry"}
        else:
            del MEMBERS[name]
            result = {"status": "Ok", "message": f"We delete your member bro"}
    return json.dumps(result)


@app.route("/data", methods=['GET'])
def data_members():
    return jsonify(results=MEMBERS)


if __name__ == '__main__':
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    app.run(port=settings['port'], host=settings['host'])
