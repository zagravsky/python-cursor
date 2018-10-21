from flask import Flask
import random
from random import choice

app = Flask(__name__)

Developers = [{"first_name": "Paul", "last_name": "Allen", "programming_language": "BASIC"},
              {"first_name": "Mark", "last_name": "Zuckerberg", "programming_language": "C++"},
              {"first_name": "Viktoriia", "last_name": "Frolova", "programming_language": "Python"}
              ]


class Developer():

    def __init__(self, first_name: str, last_name: str, programming_language: str):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    dev = Developer("Viktoriia", "Frolova", "Python")
    return dev.__str__()


@app.route('/remove_developer')
def remove_developer():
    if len(Developers) == 0:
        return "Sorry, this list is empty"
    else:
        Developers.remove(choice(Developers))
        return str(list(map(lambda dev: str(dev), Developers)))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
