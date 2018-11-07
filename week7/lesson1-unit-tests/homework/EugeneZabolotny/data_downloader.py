import requests


def get_data(url: str):
    with open('img.jpg', 'bw') as file:
        rq = requests.get(url)
        file.write(rq.content)
    return rq


if __name__ == '__main__':
    get_data('https://dummyimage.com/600x400/000/fff')
