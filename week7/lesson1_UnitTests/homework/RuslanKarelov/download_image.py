import requests


def image(url: str):
    with open('Image.png', 'wb') as image:
        data = requests.get(url)
        image.write(data.content)
    return data.content
    

if __name__ == "__main__":
    image('https://dummyimage.com/600x400/000/fff')
