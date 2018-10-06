import requests

url = 'https://dummyimage.com/600x400/000/fff'

r = requests.get(url)

with open("image.png", "wb") as code:
    code.write(r.content)
