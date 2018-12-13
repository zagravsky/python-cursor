from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from data.datacheck import *
from data.pages import pages


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)
page_template = env.get_template('jinja2-templates/jinja2-check.html')

print(page_template.render(
    date=datetime.now(),
    pages=pages,
    rows=[
        dict(cost=row['quantity'] * row['price'], **row)
        for row in rows
    ],
    total_cost=sum(row['quantity'] * row['price'] for row in rows),
    name='check'
))
