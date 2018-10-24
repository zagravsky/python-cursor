import json

import flask
from flask import Flask
from flask import request


app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'},
    }


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()


@app.route('/', methods=['GET'])
def dump_to_json():
        with open('current_states_of_members.json', 'w') as outfile:
            json.dump(MEMBERS, outfile)
        return '{"status": "OK", "message": "Current list of members dump to json file"}'


@app.route('/user/<name>', methods=['GET', 'PATCH', 'DELETE'])
@app.route('/user', methods=['POST'])
def profile(name=None):
    result = {}

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
            result = {"status": "Ok", "message": "We delete your member bro"}

    return json.dumps(result)


if __name__ == '__main__':

    my_setting = json.load(open("json_setting.json", "r"))
    app.run(port=my_setting[0]['port'], host=my_setting[0]['host'], debug=my_setting[0]['debug_mode'])
