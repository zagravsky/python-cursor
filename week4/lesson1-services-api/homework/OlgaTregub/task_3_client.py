import requests
import json


jsonrpc = {
    "jsonrpc": "2.0",
    "method": "addMember",
    "params": {"age": 18, "name": "Kate", "gender": "female"}
}

try:
    my_request = requests.post('http://127.0.0.1:4000/', data=json.dumps(jsonrpc))
    print(my_request.text)
    print(my_request.status_code)
except requests.exceptions.ConnectionError:
    print("500 Internal Server Error")
