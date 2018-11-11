import requests


def get_pic(url: str):
    req = requests.get(url)
    return req.content


if __name__ == "__main__":
    with open("picture.png", "wb") as f:
        f.write(get_pic('https://via.placeholder.com/300x300.png'))
