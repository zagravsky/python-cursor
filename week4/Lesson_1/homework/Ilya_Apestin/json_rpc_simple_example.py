from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    return succ_val_resp(f"We add your member {MEMBERS[name]}")


def get_member(name):
    if name not in MEMBERS:
        return response(-32602, "Invalid params")
    else:
        result = f"Here is your member {MEMBERS[name]}"
    return json.dumps(result)


def succ_val_resp(result):
    response_data = {"jsonrpc": "2.0"}
    response_data["result"] = result
    return json.dumps(response_data)


def response(code: int, error: str):
    response_data = {"jsonrpc": "2.0"}
    if code == -32602:
        error += "Invalid method parameter(s)."
    elif code == -32601:
        error += "The method does not exist / is not available."
    response_data["Error code"] = code
    response_data["Message"] = error
    return json.dumps(response_data)


def ping(running):
    return succ_val_resp(f"Server is {running}.")


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "Ping": ping
}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return response(-32601, "Method not found")

    result = method_view(**data.get("params"))
    return result


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1")
