import requests

ping = {"jsonrpc": "2.0", "method": "ping"}
addMember = {"jsonrpc": "2.0", "method": "addMember", "params": {"age": 21, "gender": "male", "name": "Roman"}}
getMember = {"jsonrpc": "2.0", "method": "getMember", "params": {"name": "Roman"}}

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

    with open('server_settings.json') as f:
        server_settings = json.load(f)

    server = f"http://{server_settings['host']}:{server_settings['port']}/"
    client(server)