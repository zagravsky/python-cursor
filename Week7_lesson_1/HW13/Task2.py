from requests import get


def img_download(url="https://dummyimage.com/600x400/000/fff"):
    response = get(url)
    with open('file.png', 'wb') as img:
        img.write(response.content)
    return response.content
