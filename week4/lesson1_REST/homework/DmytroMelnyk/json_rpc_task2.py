from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender, id):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    return json.dumps(success_resp(get_member.__name__, id, MEMBERS[name]))


def get_member(id, name=None):
    return json.dumps(success_resp(add_member.__name__, id, MEMBERS[name]))


def ping(id):
    return json.dumps(success_resp(ping.__name__, id))


def success_resp(*arg):
    response_data = {"jsonrpc": "2.0", "id": arg[1]}
    if arg[0] == 'get_member':
        response_data["result"] = f"We find your member {arg[2]}"
    elif arg[0] == 'add_member':
        response_data["result"] = f"We add your member {arg[2]}"
    elif arg[0] == 'ping':
        response_data["result"] = "Server is working now"
    return response_data


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "ping": ping
}


@app.route('/', methods=['POST'])
def handle():



    try:
        data = json.loads(request.data.decode('utf-8'))
        data.keys()
    except json.decoder.JSONDecodeError:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": None})
    except AttributeError:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request JSON-RPC"}, "id": None})

    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": data.get('id')})

    result = method_view(id=data.get("id"), **data.get("params"))
    return result


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1", debug=True)
