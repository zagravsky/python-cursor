from flask import Flask
from config import configuration
from api.api import api

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config.from_object(configuration())
app.secret_key = configuration().KEY

app.register_blueprint(api, url_prefix='/api')



