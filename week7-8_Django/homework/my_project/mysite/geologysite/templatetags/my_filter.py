from django import template
from bs4 import BeautifulSoup
register = template.Library()


@register.filter
def img_path(text):
    soup = BeautifulSoup(text, 'html.parser')
    img = soup.find('img')
    if img is None:
        return ""
    else:
        return img['src']
