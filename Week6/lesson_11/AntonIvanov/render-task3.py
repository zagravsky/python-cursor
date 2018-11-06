from jinja2 import Environment, FileSystemLoader, select_autoescape
from filters import format_datetime
import data
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)
env.filters['datetime'] = format_datetime
page_template = env.get_template('jinja2-task3.html')
print(page_template.render(
    date=data.today,
    articles=data.articles,
    links=data.links,
    name='task3'
))
