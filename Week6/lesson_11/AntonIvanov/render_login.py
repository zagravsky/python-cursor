from jinja2 import Environment, FileSystemLoader, select_autoescape
import data
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)
page_template = env.get_template('jinja2-login.html')

print(page_template.render(links=data.links, name='login'))
