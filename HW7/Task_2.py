from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    result = {"jsonrpc": "2.0", "result" : f'We add your member {MEMBERS[name]}'}
    return json.dumps(result)


def get_member(name):
    result = {"jsonrpc": "2.0", "result": MEMBERS[name]}
    return json.dumps(result)


def response(result):
    response_data = {"jsonrpc": "2.0"}
    response_data['result'] = result
    return json.dumps(response_data)


@app.route ('/ping', methods=['POST'])
def ping():
    return response('I\'m okay')

METHODS = {
    "addMember": add_member,
    "getMember": get_member

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
    settings = json.load(open("settings.json", "r"))
    app.run(port=settings['port2'], host=settings['host'], debug=settings['debug'])
