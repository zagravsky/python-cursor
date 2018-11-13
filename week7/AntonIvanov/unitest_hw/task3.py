import requests


def get_image(img_url: str):
    file_name = 'task3.png'
    res = requests.get(img_url)
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(res.content)
            return res.status_code
    print(f'File {file_name} downloaded')



if __name__ == "__main__":
    url = "https://dummyimage.com/600x400/000/fff"
    get_image(url)
