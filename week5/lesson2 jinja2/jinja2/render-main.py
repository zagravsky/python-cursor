from jinja2 import Environment, FileSystemLoader, select_autoescape, PackageLoader
from datetime import datetime
from data.data import *
from data.pages import pages


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)
page_template = env.get_template('jinja2-templates/jinja2-main.html')

print(page_template.render(
    date=datetime.now(),
    pages=pages,
    rows=[
        dict(cost=row['quantity'] * row['price'], **row)
        for row in rows
    ],
    total_cost=sum(row['quantity'] * row['price'] for row in rows),
    name='main'
))

