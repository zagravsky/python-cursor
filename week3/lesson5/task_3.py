import requests
with open('pictures.jpg','wb') as target:
    file = requests.get('https://dummyimage.com/600x400/000/fff')
    target.write(file.content)