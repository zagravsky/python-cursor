import requests


def download_something(url: str):
    r = requests.get(url)
    return r.content


if __name__ == "__main__":
    with open("picture.png", "wb") as f:
        f.write(download_something('https://dummyimage.com/600x400/000/fff'))
