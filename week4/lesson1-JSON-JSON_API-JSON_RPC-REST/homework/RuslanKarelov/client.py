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
    print(my_req.text)
    print("Server is alive")
except requests.exceptions.ConnectionError:
    print("Server is dead")
