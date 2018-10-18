import requests
import json
import re


def server_checks():
    url = "http://127.0.0.1:4000"
    data = {"jsonrpc": "2.0",
               "method": "getMember",
               "params": {
                   "name": "Petya"
               }
             }
    r = requests.post(url, data=json.dumps(data))
    if re.match('2', str(r.status_code)):
        print("Your server is alive")
    elif re.match('3', str(r.status_code)):
        print("Redirecting occurred")
    elif re.match('4', str(r.status_code)):
        print("Client error")
    else:
        print("Server broken")


if __name__ == '__main__':
    server_checks()
