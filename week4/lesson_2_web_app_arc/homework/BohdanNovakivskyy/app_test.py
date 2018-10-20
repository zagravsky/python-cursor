from flask import Flask

app = Flask(__name__)

developers = [
    {'first_name': "Ivan", 'last_name': 'Pidkova', 'programming_language': 'VBA'},
    {'first_name': "Petro", 'last_name': 'Koloda', 'programming_language': 'C++'},
    {'first_name': "Viktor", 'last_name': 'Maly', 'programming_language': 'Ruby'},
    {'first_name': "Gosha", 'last_name': 'Kuzenko', 'programming_language': 'Python'}
]


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    developer_next = Developer('Gosha', 'Goblin', 'JS')
    return developer_next.__str__


@app.route('/remove_developer')
def remove_developer():
    if len(developers):
        developers.pop()
        return developers
    else:
        return 'No developers in list'
