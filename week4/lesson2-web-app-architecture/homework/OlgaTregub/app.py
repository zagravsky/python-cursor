from flask import Flask

app = Flask(__name__)

dev_list = [
    {'first_name': 'Albert', 'last_name': 'Einstein', 'programming_language': 'Fortran'},
    {'first_name': 'Thomas', 'last_name': 'Edison', 'programming_language': 'Pascal'},
    {'first_name': 'Lady', 'last_name': 'Gaga', 'programming_language': 'HTML'}
]


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


def list_of_dev(devlist):
    joined = [f"{dev['first_name']} {dev['last_name']} - {dev['programming_language']}" for dev in devlist]
    return '<br>'.join(joined)


@app.route('/')
def developer_controller():
    dev = Developer('Olga', 'Tregub', 'Python')
    return str(dev)


@app.route('/developers')
def developers():
    return list_of_dev(dev_list)


@app.route('/remove_developer')
def remove_developers():
    if not dev_list:
        return "Developer's list is empty"
    else:
        dev_list.pop()
        return "Developer's list is empty" if not dev_list else list_of_dev(dev_list)
