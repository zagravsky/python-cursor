import requests
import json
jsonrpc_req = {
	"jsonrpc": "2.0",
	"method": "getMember",
	"params":{
		"name":"denis"
	}
}
try:
    my_req = requests.post(' http://127.0.0.1:4000/', data=json.dumps(jsonrpc_req))
    print(f"Your response: {my_req.text}.\nMessage: 'Server is alive'")
except requests.exceptions.ConnectionError:
    print("Message: 'Server is dead'")
