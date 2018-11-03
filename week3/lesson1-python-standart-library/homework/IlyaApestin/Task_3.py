import requests

open('image.jpeg', 'wb').write(requests.get('https://dummyimage.com/600x400/000/fff').content)
