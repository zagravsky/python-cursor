from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    result = f'We add your member {MEMBERS[name]}'
    return response(result)


def get_member(name):
    member = MEMBERS.get(name)
    print(name)
    print(member)
    if name == member['name']:
        result = MEMBERS[name]
    else:
        result = {"code": -32602, "message": "Invalid params"}
    return response(result)


def response(result):
    response_data = {"jsonrpc": "2.0"}
    response_data['result'] = result
    return json.dumps(response_data)


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "response": response
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
    return response('pong')


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1")
