import json

import flask
from flask import Flask
from flask import request

# Load settings from json file to local variable
our_data = json.load(open("settings.json", "r"))
HOST = our_data['host']
PORT = our_data['port']
DEBUG = our_data['debug']

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()


@app.route('/users', methods=['POST'])
@app.route('/users/<name>', methods=['GET', 'PATCH', 'DELETE'])
def profile(name: str):
    result = {}

# adding new users
    if flask.request.method == 'POST':
        params = json.loads(request.data.decode('utf-8'))
        MEMBERS[params.get('name')] = params
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
            result = {"status": "Fail", "message": "I don't know about such user. Sorry"}
        else:
            params = json.loads(request.data.decode('utf-8'))
            MEMBERS[name].update(params)
            result = {"status": "Ok", "message": f"This is your new member {MEMBERS.get(name)}"}

    if flask.request.method == 'DELETE':
        if not check_member(name):
            result = {"status": "Fail", "message": "I don't know about such user. Sorry"}
        else:
            del MEMBERS[name]
            result = {"status": "Ok", "message": f"We delete your member bro"}
    return json.dumps(result)


@app.route('/users/dump', methods=['POST'])
def dump2file():
    with open('dump.json', 'w') as outfile:
        json.dump(MEMBERS, outfile)
        result = {"status": "Ok", "message": f"Users' dump was saved to the file"}
    return json.dumps(result)


if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=DEBUG)
