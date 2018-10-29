from datetime import timedelta
from flask import Flask
from task_2.config import runtime_config
from task_2.ourblueprint.blueprint import carposts
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(runtime_config)
app.config["SECRET_KEY"] = "5f31c532e88134d18c12517d3c70a80a"
app.register_blueprint(carposts, url_prefix='/blog')
bcrypt = Bcrypt(app)
app.permanent_session_lifetime = timedelta(minutes=5)

from task_2 import routes
