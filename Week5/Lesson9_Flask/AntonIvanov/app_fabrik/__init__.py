from flask import Flask
from .api import factory_api, test_api, home_api ,bike_api
from .config import runtime_config

def run_app():
    app = Flask(__name__)
    app.config.from_object(runtime_config())
    app.register_blueprint(factory_api)
    app.register_blueprint(bike_api)
    app.register_blueprint(test_api)
    app.register_blueprint(home_api)
    return app
