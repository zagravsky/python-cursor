from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def response(name, method):
    response_data = {"jsonrpc": "2.0"}
    if method == 'add_member':
        response_data["result"] = f"We add your member {MEMBERS.get(name)}"
        return json.dumps(response_data)
    elif method == 'get_member':
        response_data["result"] = f"Member info: {MEMBERS.get(name)}"
        return json.dumps(response_data)
    else:
        response_data["result"] = "Ping successful!"
        return json.dumps(response_data)


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    return response(name, "add_member")


def get_member(name):
    return response(name, "get_member")


METHODS = {
    "getMember": get_member,
    "addMember": add_member
}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})

    result = method_view(**data.get("params"))
    return result


@app.route('/ping', methods=['POST'])
def ping_server():
    return response("", "ping_server")


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1")
