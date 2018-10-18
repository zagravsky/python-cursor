import requests
import json


jsonrpc = {
    "jsonrpc": "2.0",
    "method": "getMember",
    "params": {"name": "Igor"}
}

try:
    my_req = requests.post(' http://127.0.0.1:4001/', data=json.dumps(jsonrpc))
    print(my_req.status_code)
except requests.exceptions.ConnectionError:
    print("500 Internal Server Error") 