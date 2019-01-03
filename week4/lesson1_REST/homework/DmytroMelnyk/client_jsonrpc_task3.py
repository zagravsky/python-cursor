import socket

import requests
import json


def server_is_live_check(url: str, data: dict) -> str:
    """
    Func that makes request to server from json_rpc_simple_example and check if server is alive
    Args:
        url: sting url
        data: json

    Returns: text confirmation as status ok or error

    """
    try:
        r = requests.post(url, json.dumps(data))
        if r.status_code == 200:
            return "Server Ok"
    except socket.error as e:
        return f"Server down!\n{e}"


if __name__ == "__main__":
    url = 'http://127.0.0.1:4000/'
    data = {"jsonrpc": "2.0", "method": "ping", "params": {}, "id": 3}
    print(server_is_live_check(url, data))
