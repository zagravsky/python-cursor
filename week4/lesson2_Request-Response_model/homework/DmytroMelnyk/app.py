from flask import Flask
import random

app = Flask(__name__)

DEVELOPERS = {
    "Poroshenko": {"first_name": "Petro", "last_name": "Poroshenko", "programming_language": "Java"},
    "Groyisman": {"first_name": "Vova", "last_name": "Groyisman", "programming_language": "Ruby"},
    "Yushchenko": {"first_name": "Victor", "last_name": "Yushchenko", "programming_language": "PHP"}
}


class Developer:

    def __init__(self, first_name: str, last_name: str, programming_language: str):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    dev = Developer('Dmytro', 'Melnyk', 'Python')
    return dev.__str__()


@app.route('/remove_developer')
def remove_developer():
    if DEVELOPERS:
        DEVELOPERS.pop(random.choice(list(DEVELOPERS.keys())))
        return show_devs()
    return 'DEVELOPERS list is empty - There are not devs in list'


@app.route('/show')
def show_devs():
    list_to_print = ['{} {}-{}'.format(v["first_name"], v["last_name"], v["programming_language"]) for _, v in DEVELOPERS.items()]
    return ''.join(i for i in list_to_print)
