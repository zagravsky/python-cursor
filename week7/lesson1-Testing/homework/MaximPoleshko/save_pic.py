import requests as rq


def save_img(url: str):
    r = rq.get(url)
    return r.content


if __name__ == '__main__':
    with open("picture.png", "wb") as pic:
        pic.write(save_img('https://dummyimage.com/600x400/000/fff'))