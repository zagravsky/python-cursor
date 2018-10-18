from random import randint
from flask import Flask

app = Flask(__name__)

dev_list = [
    {'first_name': 'Guido', 'last_name': 'van Rossum', 'programming_language': 'Python'},
    {'first_name': 'James', 'last_name': 'Gosling', 'programming_language': 'Java'},
    {'first_name': 'Dennis', 'last_name': 'Ritchie', 'programming_language': 'C'},
]


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __repr__(self):
        return f"{self.first_name} {self.last_name} - {self.programming_language}"


def pretty_dev_list(lst):
    joined = [f"{dev['first_name']} {dev['last_name']} - {dev['programming_language']}" for dev in lst]
    return '\n'.join(joined)


@app.route('/')
def developer_controller():
    dev = Developer('Eugene', 'Zabolotny', 'Python')
    return str(dev)


@app.route('/developers')
def developers():
    return pretty_dev_list(dev_list)


@app.route('/remove_developer')
def remove_developer():
    if dev_list:
        del dev_list[randint(0, len(dev_list) - 1)]
        if dev_list:
            return pretty_dev_list(dev_list)
        else:
            return "Developer's list is empty"
