from flask import Flask
from Developer import Developer
app = Flask(__name__)


@app.route('/')
def developer_controller():
    dev = Developer("Anton", "Ivanov", "Python")
    return dev()
    # return 'Hello, World!'
