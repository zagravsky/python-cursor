import requests
import json


def serv_live(u, d):
    try:
        r = requests.post(url, json.dumps(data))
        if r.status_code == 200:
            return "Server Ok"
    except Exception as e:
        return "Server down! ", '\n', e


if __name__ == "__main__":
    url = 'http://127.0.0.1:4000/'
    data = {"jsonrpc": "2.0", "method": "ping", "params": {}, "id": 3}
    print(serv_live(url, data))
