import requests
import os


def dowlnoad_from_url(u: str):
    """
    Using requests library, download image from url and save it as a file on your device.
    :param u: url
    """
    filename = os.getcwd()+'/downloadedfile'
    r = requests.get(u, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    return r.content


if __name__ == '__main__':
    url = 'https://dummyimage.com/600x400/000/fff'
    dowlnoad_from_url(url)
