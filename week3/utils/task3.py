import requests


def save_pic(url: str, filename: str):
    f = open(filename, 'wb')
    f.write(requests.get(url).content)
    f.close()

