from flask import Flask
from flask import request
import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'Denis'},
    'eugene': {'age': 32, 'gender': 'male', 'name': 'Eugene'}
}


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()


@app.route('/user', methods=['POST'])
@app.route('/user/<name>', methods=['GET', 'PATCH', 'DELETE'])
def profile(name: str = None):
    result = {}

    if request.method == 'POST':
        params = json.loads(request.data.decode('utf-8'))
        MEMBERS[params.get('name')] = params
        result = {"status": "OK", "message": f"Add new user {params}"}

    if request.method == 'GET':
        member = MEMBERS.get(name)
        if member is None:
            result = {"status": "Fail", "error": f"Could not find member with name {name}"}
        else:
            result = {"status": "OK", "message": f"We find your user {member}"}

    if request.method == 'PATCH':
        member = MEMBERS.get(name)
        if member is None:
            result = {"status": "Fail", "message": "I don't know about such user. Sorry"}
        else:
            params = json.loads(request.data.decode('utf-8'))
            MEMBERS[name].update(params)
            result = {"status": "Ok", "message": f"This is your new member {MEMBERS.get(name)}"}

    if request.method == 'DELETE':
        if not check_member(name):
            result = {"status": "Fail", "message": "I don't know about such user. Sorry"}
        else:
            del MEMBERS[name]
            result = {"status": "Ok", "message": f"We delete your member bro"}
    return json.dumps(result)


@app.route('/users', methods=['GET'])
def profiles():
    if request.method == 'GET':
        with open('members.json', 'w') as outfile:
            json.dump(MEMBERS, outfile, indent=4)
    result = {"status": "Ok", "message": f"All members are dumped"}
    return json.dumps(result)


if __name__ == '__main__':
    with open('settings.json') as f:
        SETTINGS = json.load(f)

    app.run(host=SETTINGS['host'], port=SETTINGS['port0'], debug=SETTINGS['debug_mode'])
