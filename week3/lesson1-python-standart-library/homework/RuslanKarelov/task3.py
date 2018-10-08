import requests as rq

url = 'https://dummyimage.com/600x400/000/fff'
image = open('image.png', 'wb')
data = rq.get(url)
image.write(data.content)
image.close()
