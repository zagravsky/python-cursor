import requests
import json


def server_checks():
    url = "http://127.0.0.1:4000/ping"
    data = {"jsonrpc": "2.0", "method": "ping_server"}
    try:
        print(requests.post(url, data=json.dumps(data)))
    except requests.exceptions.ConnectionError:
        print("Server broken")


if __name__ == '__main__':
    server_checks()
