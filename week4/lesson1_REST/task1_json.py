import json

from flask import Flask


app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()

@app.route('/users', methods=['GET'])
def users():
    with open('some_data.json', 'w') as users_f:
        json.dump(MEMBERS, users_f, skipkeys=True)
    msg_back = {"status": "Ok", "message": f"All members is dumped"}
    return json.dumps(msg_back)


if __name__ == '__main__':
    with open('setting.json', 'r') as param_file:
        params = json.load(param_file)
    app.run(port =params['port'] , host=params['host'], debug=params['debug_mode'])