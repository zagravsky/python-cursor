from flask import Flask
from HW_9.config import runtime_config
from HW_9.api import api


app = Flask(__name__)

app.config.from_object(runtime_config())
app.register_blueprint(api)
app.secret_key = runtime_config().SECRET_KEY
