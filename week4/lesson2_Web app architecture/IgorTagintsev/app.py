from flask import Flask

app = Flask(__name__)

dev_list = [
    {'first_name': 'Marshall', 'last_name': 'Mathers', 'programming_language': 'PHP'},
    {'first_name': 'Margaret', 'last_name': 'Thatcher', 'programming_language': 'Java'},
    {'first_name': 'Anthony', 'last_name': 'Hopkins', '': 'C++'},
]

class Developer():
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    dev = Developer('Igor', 'Tagintsev', 'Python')
    return str(dev)


@app.route('/remove_developer')
def remove_developers():
    if len(dev_list) > 1:
        dev_list.pop()
        return '<br>'.join([str(f"{x['first_name']} {x['last_name']} - {x['programming_language']}") for x in dev_list])
    else:
        return 'List is empty'