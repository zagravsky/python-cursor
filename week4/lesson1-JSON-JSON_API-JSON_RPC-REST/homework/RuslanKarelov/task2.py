from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


ERRORS = json.load(open('jsonrpc_errors.json', 'r'))


def succses_valid_response(result):
    response_data = {"jsonrpc": "2.0"}
    response_data["result"] = result
    return json.dumps(response_data)


def error_valid_response(error):
    response_data = {"jsonrpc": "2.0"}
    response_data["error"] = error
    return json.dumps(response_data)


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    result = f"We add your member {MEMBERS[name]}"
    return succses_valid_response(result)


def get_member(name):
    member = MEMBERS.get(name)
    if member is None:
        error = f"Your member {name} does not exist"
        return error_valid_response(error)
    else:
        result = f"We found your member {MEMBERS[name]}"
        return succses_valid_response(result)


METHODS = {
    "getMember": get_member,
    "addMember": add_member
}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))

    if not method_view:
        return error_valid_response(ERRORS["Method not found"])

    result = method_view(**data.get("params"))
    return result


@app.route('/ping', methods=['POST'])
def check_server():
    if not request.data:
        return error_valid_response(ERRORS["Server error"])
    else:
        return succses_valid_response(f"Server is alive")


if __name__ == '__main__':
    our_settings = json.load(open('json_settings.json', 'r'))
    app.run(port=our_settings["port"], host=our_settings["host"], debug=our_settings["debug_mode"])
