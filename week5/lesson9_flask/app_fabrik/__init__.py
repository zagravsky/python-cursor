from flask import Flask

from app_fabrik.api import factory_api
from app_fabrik.config import runtime_config
from app_fabrik.task1 import api

def run_app():
    app = Flask(__name__)
    app.config.from_object(runtime_config())
    app.register_blueprint(factory_api)
    app.register_plueprint(api)

    return app
