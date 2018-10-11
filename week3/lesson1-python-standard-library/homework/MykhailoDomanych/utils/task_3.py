import requests


def get_img(url: str):
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        open('image.png', 'wb').write(r.content)
