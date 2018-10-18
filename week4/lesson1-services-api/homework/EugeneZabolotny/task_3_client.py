import requests

ping = {"jsonrpc": "2.0", "method": "ping"}
addMember = {"jsonrpc": "2.0", "method": "addMember", "params": {"age": 32, "gender": "male", "name": "Eugene"}}
getMember = {"jsonrpc": "2.0", "method": "getMember", "params": {"name": "Eugene"}}


def client(origin):
    try:
        print(requests.post(origin + "ping", json=ping).json())
    except requests.exceptions.ConnectionError:
        print('Server is dead')
    else:
        print(requests.post(origin, json=addMember).json())
        print(requests.post(origin, json=getMember).json())


if __name__ == '__main__':
    import json

    with open('settings.json') as f:
        SETTINGS = json.load(f)

    server = f"http://{SETTINGS['host']}:{SETTINGS['port1']}/"
    client(server)
