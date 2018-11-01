from flask import Flask
from datetime import datetime


time = datetime.now()

app = Flask(__name__, template_folder='../templates', static_folder='../static')