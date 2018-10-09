import requests
from requests import Response

link = "https://dummyimage.com/600x400/000/fff"

req = requests.get(link)

with open('image_for_task_3.png', 'wb') as file:
    file.write(req.content)
	