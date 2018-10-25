import requests
import shutil

data = 'https://dummyimage.com/600x400/000/fff'

r = requests.get(data, stream=True)
if r.status_code == 200:
    with open('imp.png', 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)