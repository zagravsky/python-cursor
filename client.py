import requests
import json

host = 'http://127.0.0.1:4001/ping'
jsonrpc_rq = {"jsonrpc": "2.0", "method": "ping"}

try:
    rsp = requests.post(host, json.dumps(jsonrpc_rq))
    if rsp.status_code == 200:
        print("Server work success")
except Exception:
        print("Server down!")
