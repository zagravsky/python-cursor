import json
import requests


rpc_data = {
    "jsonrpc": "2.0",
    "method": "get_Member",
    "params": {"name": "denis"}
}
def check():
    try:
        request_set = requests.post('http://127.0.0.1:4000/', data=json.dumps(rpc_data))
        print(request_set.status_code)
    except requests.exceptions.ConnectionError:
        print("Server doesnt work")


if __name__ == '__main__':

    check()