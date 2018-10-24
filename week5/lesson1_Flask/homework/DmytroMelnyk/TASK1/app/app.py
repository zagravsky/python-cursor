from flask import Flask
from config import runtime_config

from apicars.blueprint import apicars

app = Flask(__name__)
app.config.from_object(runtime_config())

app.register_blueprint(apicars, url_prefix='/api')
