import requests
try:
    print("Server is alive.  ", requests.post("http://127.0.0.1:4000/", json={"key": "value"}))
except:
    print("Server is down.")
