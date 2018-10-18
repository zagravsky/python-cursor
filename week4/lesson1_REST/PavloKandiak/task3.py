import requests

def ping(data):
	try:
		req = requests.post(arg)
		if req.status_code == 200:
			return "Server work"
	except:
		return "Server not work"
		
if __name__ == "__main__":
	url = 'http://127.0.0.1:4000/ping'
	print(ping(url))