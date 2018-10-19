import requests

def download_image(url: str):
    with open('fff.png', 'bw') as image:
        response = requests.get(url)
        image.write(response.content)

download_image('https://dummyimage.com/600x400/000/fff')
