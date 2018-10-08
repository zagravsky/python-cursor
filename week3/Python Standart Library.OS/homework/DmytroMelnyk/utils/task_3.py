# Task 3
#
# Using requests library, download image from this url https://dummyimage.com/600x400/000/fff
# and save it as a file on your device.

import requests


def dowlnoad_from_url(u: str):
    """
    Using requests library, download image from url and save it as a file on your device.
    :param u: url
    """

    r = requests.get(u, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
        print('Download file complete!')


if __name__ == '__main__':
    url = 'https://dummyimage.com/600x400/000/fff'
    filename = '/mnt/48D443B7D443A5D2/Users/Melnyk.D/OneDrive/Python_Projects_education/python-cursor/week3/Python ' \
               'Standart Library.OS/homework/DmytroMelnyk/utils/downloadedfile '

    dowlnoad_from_url(url)