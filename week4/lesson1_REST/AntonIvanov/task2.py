from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender):
    response_data = {"jsonrpc": "2.0"}
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    response_data["result"] = f"We add your member {MEMBERS[name]}"
    return json.dumps(response_data)


def get_member(name):
    member = MEMBERS.get(name)
    response_data = {"jsonrpc": "2.0"}
    if member is None:
        response_data["error"] = {"code": -32602, "message": "Invalid params"}
    else:
        response_data["result"] = MEMBERS.get(name)
    return json.dumps(response_data)


def del_member(name):
    member = MEMBERS.get(name)
    response_data = {"jsonrpc": "2.0"}
    if member is None:
        response_data["error"] = {"code": -32602, "message": "Invalid params"}
    else:
        del MEMBERS[name]
        response_data["result"] = f"We delete member with name: {name}"
    return json.dumps(response_data)


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "delMember": del_member,
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
def get_ping():
    data = json.loads(request.data.decode('utf-8'))
    if data.get('method') == 'ping':
        response_data = {"jsonrpc": "2.0", "result": "ping success!"}
    else:
        response_data = {"error": {"code": -32601, "message": "Method not found"}}
    return json.dumps(response_data)


if __name__ == '__main__':
    with open("settings.json", "r") as f:
        serv_settings = json.load(f)
    app.run(**serv_settings)
