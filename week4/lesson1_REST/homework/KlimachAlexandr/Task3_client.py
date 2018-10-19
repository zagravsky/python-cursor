import requests

ping = {"jsonrpc": "2.0", "method": "ping"}


def check(server):
    try:
        print(requests.post(server, json=ping).json())
    except requests.exceptions.ConnectionError:
        print('Server not work')


if __name__ == "__main__":
    url = 'http://127.0.0.1:4000/ping'
    check(url)
