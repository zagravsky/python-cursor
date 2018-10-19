from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def response(result):
    response_data = {"jsonrpc": "2.0"}
    response_data['result'] = result
    return json.dumps(response_data)


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    result = f'We add your member {MEMBERS[name]}'
    return response(result)


def get_member(name):
    result = MEMBERS.get(name)
    if result is not None:
        return response(result)
    return json.dumps({"error": {"code": -32602, "message": "Invalid params"}})


def ping(pong):
    return response(pong)


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


@app.route('/ping', methods=['POST'])
def ping():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})
    return response('pong')


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1")
