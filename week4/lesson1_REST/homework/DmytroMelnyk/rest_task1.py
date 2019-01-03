import json
import flask
from flask import Flask
from flask import request
import os

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()


def output_DB_members(dict_members: dict):
    """
    Func that write current states of members to json file
    Args:
        dict_members: dict of MEMBERS

    Returns: None

    """
    DB_path = os.getcwd() + '/utils/DB_members.json'
    with open(DB_path, 'w') as f:
        json.dump(dict_members, f)


@app.route('/dump', methods=['GET'])
def dumptofile():
    """
    Route that will dump current states of members to json file
    Returns: Text confirmation of success at console

    """
    output_DB_members(MEMBERS)
    return 'Date was wrote to DB_members file'


@app.route('/')
def index():
    return "<h4>To GET data from DB use route  '/user/name' </h4>"


@app.route('/user', methods=['POST'])
@app.route('/user/<name>', methods=['GET', 'PATCH', 'DELETE'])
def profile(name=None):
    result = {}

    if flask.request.method == 'POST':
        params = json.loads(request.data.decode('utf-8'))
        for key, val in params.items():
            MEMBERS[key] = val
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


if __name__ == '__main__':
    settings_path = os.getcwd() + '/utils/settings.json'
    with open(settings_path) as f:
        data = json.load(f)
        for d in data:
            port, host, debug = dict.values(d)
    app.run(port=port, host=host, debug=debug)
