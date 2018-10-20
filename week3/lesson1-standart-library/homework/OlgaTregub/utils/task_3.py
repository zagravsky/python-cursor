import requests


def save_data (url: str):
    with open ('img.jpg', 'bw') as file:
        file.write(requests.get(url).content)