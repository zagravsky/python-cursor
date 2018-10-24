from flask import Flask
from config import Configuration

from apicars.blueprint import apicars

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(apicars, url_prefix='/api')
