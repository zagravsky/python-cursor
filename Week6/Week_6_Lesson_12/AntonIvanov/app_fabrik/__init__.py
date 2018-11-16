from flask import Flask
from .api import factory_api, bike_api
from .method_views import home, products, page_not_found, register, login, logout, test
from .config import runtime_config


def run_app():
    app = Flask(__name__)
    app.config.from_object(runtime_config())
    app.register_blueprint(factory_api)
    app.register_blueprint(bike_api)
    app.register_blueprint(home)
    app.register_blueprint(products)
    app.register_error_handler(404, page_not_found)
    app.register_blueprint(register)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(test)
    return app
