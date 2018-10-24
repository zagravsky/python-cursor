from flask import Flask
from flask import request


import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def success_valid_response(jsonrpc_result):
    response_data = {"jsonrpc": "2.0"}
    response_data["result"] = jsonrpc_result
    return json.dumps(response_data)


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    return success_valid_response(f"We add your member {MEMBERS[name]}")


def get_member(name):
    if name in MEMBERS:
        return success_valid_response(f"We find your member {name}")
    else:
        return success_valid_response(f"Could not find member with name {name}")


@app.route('/ping', methods=['POST'])
def ping():
    return success_valid_response('Server works success')


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "ping": ping
}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))

    if not method_view:
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})

    result = method_view(**data.get("params"))
    return result


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1")
