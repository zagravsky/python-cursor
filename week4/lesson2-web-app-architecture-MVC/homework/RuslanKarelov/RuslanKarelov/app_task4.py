from RuslanKarelov.Developers_task3 import Developer
from flask import Flask

app = Flask(__name__)


@app.route('/')
def developer_controler():
    dev1 = Developer("Reslan", "Karelov", "Python")
    return f"{dev1.first_name} {dev1.last_name} - {dev1.programing_language}"


