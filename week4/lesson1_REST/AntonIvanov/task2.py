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

def get_ping(name):
    response_data = {"jsonrpc": "2.0"}
    response_data["result"] = f"Hi {name}. Success!"
    return json.dumps(response_data)


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "delMember": del_member,
    "ping": get_ping
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
    serv_settings = json.load(open("settings.json", "r"))
    app.run(**serv_settings)
