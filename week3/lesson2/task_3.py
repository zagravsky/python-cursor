import requests

response = requests.get('https://dummyimage.com/600x400/000/fff', stream = True)
if response.status_code == 200:
    with open("/home/bob/Downloads/task_3", 'wb') as img:
        img.write(response.content)
