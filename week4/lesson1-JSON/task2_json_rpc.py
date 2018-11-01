from flask import Flask, request
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
    if MEMBERS.get(name):
        response_data = {"jsonrpc": "2.0", "result": MEMBERS[name]}
        return json.dumps(response_data)
    else:
        return json.dumps({"error": {"code": -32602, "message": f"Member {name} not found!"}})


def ping():
    response_data = {"jsonrpc": "2.0", "result": "It's work for me"}
    return json.dumps(response_data)


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "ping": ping
}

@app.route('/', methods=['GET'])
def root():
    return "Hello, Please make your RPC Request"

@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})

    result = method_view(**data.get("params"))
    return result


if __name__ == '__main__':

    settings = json.load(open('settings.json', 'r'))
    app.run(port=settings['port'], host=settings['host'], debug=settings['debug'])
