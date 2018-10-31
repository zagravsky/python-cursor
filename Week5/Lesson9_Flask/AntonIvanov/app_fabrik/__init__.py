from flask import Flask
from .api import factory_api, home_api, bike_api, products_api, page_not_found, register
from .config import runtime_config
from flask_login import LoginManager


def run_app():
    app = Flask(__name__)
    login = LoginManager(app)
    app.config.from_object(runtime_config())
    app.register_blueprint(factory_api)
    app.register_blueprint(bike_api)
    app.register_blueprint(home_api)
    app.register_blueprint(products_api)
    app.register_error_handler(404, page_not_found)
    app.register_blueprint(register)
    return app
