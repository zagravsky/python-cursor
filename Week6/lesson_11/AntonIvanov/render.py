from jinja2 import Environment, FileSystemLoader, select_autoescape
from filters import format_datetime
import data


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)
env.filters['datetime'] = format_datetime
page_template = env.get_template('jinja2-book.html')

print(page_template.render(
    date=data.today,
    rows=[
        dict(cost=row['quantity'] * row['price'], **row)
        for row in data.rows
    ],
    total_cost=sum(row['quantity'] * row['price'] for row in data.rows),
    links=data.links,
    name='book'
))
