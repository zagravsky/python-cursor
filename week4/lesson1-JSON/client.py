import requests

url = "http://127.0.0.1:4001"
payload = "{\"jsonrpc\": \"2.0\", \"method\": \"getMember\", \"params\": {\"name\": \"denis\"}}"

try:
    response = requests.request("POST", url, data=payload)
    print("Server is UP")
except requests.exceptions.ConnectionError:
    print("Server is DOWN")