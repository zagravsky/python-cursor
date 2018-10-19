import requests

ping = {"jsonrpc": "2.0", "method": "ping"}
addMember = {"jsonrpc": "2.0", "method": "addMember", "params": {"name": "Viktor", "age": 19, "gender": "male" }}
getMember = {"jsonrpc": "2.0", "method": "getMember", "params": {"name": "Viktor"}}

def send_request(source):
    try:
        print("Try to ping server...")
        result = requests.post(source + "ping", json=ping).json()
        print(result)
    except requests.exceptions.ConnectionError:
        print('Server is unavailable')
    else:
        print("---Add member---")
        print(requests.post(source, json=addMember).json())
        print("---Get Dvoeshnik---")
        print(requests.post(source, json=getMember).json())

if __name__ == '__main__':
    import json
    with open('settings.json') as file:
        settings = json.load(file)
    url = f"http://{settings['host']}:{settings['port2']}/"
    send_request(url)