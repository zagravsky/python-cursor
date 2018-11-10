import requests as rq


def get_image():
    r = rq.get('https://dummyimage.com/600X400/000/fff')
    return r.content
