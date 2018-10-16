import requests as rq

def save_img():
    url = 'https://dummyimage.com/600x400/000/fff'
    r = rq.get(url)
    with open("fff.png", "wb") as pic:
        pic.write(r.content)
