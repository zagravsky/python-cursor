from flask import Flask
from Developer import Developer


app = Flask(__name__)
dev1 = Developer("Oleg", "Schevchuk", "Java")
dev2 = Developer("Dmytro", "Tuchik", "C++")
dev3 = Developer("Alex", "Lutenko", "Python")
dev4 = Developer("Anton", "Ivanov", "Python")
dev_pack = [dev1, dev2, dev3, dev4]


@app.route('/')
def developer_controller():
    dev = Developer("Anton", "Ivanov", "Python")
    return dev()
    # return 'Hello, World!'


@app.route('/remove_developer/<int:index>')
def remove_developer(index: int):
    try:
        dev_pack.pop(index)
    except IndexError:
        return f"dev_pack has no index {index}"
    if dev_pack:
        resp_string = ''
        for i in dev_pack:
            resp_string += '<p>' + i() + '</p>'
        return resp_string
    else:
        return "Developer list is empty"
