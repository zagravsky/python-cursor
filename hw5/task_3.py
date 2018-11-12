C:\>pip install requests

>>> import requests
>>> r = requests.get('https://dummyimage.com/600x400/000/fff')
>>> if r.status_code == 200:
    with open("D:\Python\projects\hw5\sample.jpg", 'wb') as f:
        f.write(r.content)

1780
>>>