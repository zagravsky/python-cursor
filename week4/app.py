from flask import Flask
import random

app = Flask(__name__)


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.language = programming_language

    def __str__(self):
        return '<p>{} {} - {}</p>'.format(self.first_name, self.last_name, self.language)


class Dev_group:
    list_of_members = []

    def __add__(self, member):
        self.list_of_members.append(member)
        return self

list_dev = []

list_dev.append(Developer("Jek", "Readle", "Python"))
list_dev.append(Developer("Igor", "Sirko", "Java"))
list_dev.append(Developer("Dmutro", "Kolisnuk", "Ruby"))


@app.route('/')
def developer_controller():
    Tom = Developer("Tom", "Readle", "Ruby")
    return Tom.__str__()


@app.route('/all_dev')
def view_list():
    if len(list_dev) == 0:
        return 'List is empty'
    else:
        return ''.join(map(lambda member: str(member), list_dev))


@app.route('/all_dev/remove_developer')
def remove_developer_controller():
    list_dev.remove(random.choice(list_dev))
    if len(list_dev) == 0 :
        return 'List is empty. You deleted last member'
    else:
        return ''.join(map(lambda member: str(member), list_dev))

