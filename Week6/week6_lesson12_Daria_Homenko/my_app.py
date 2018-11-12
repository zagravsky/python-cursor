from flask import Flask

from flask_bcrypt import Bcrypt
from config import runtime_config
from api.view import pages_view, error_404
from db.db_creation import create_db
from db.relationship import one_to_many
from api.user_api import user_api
from api.flower_api import flower_api

from db.db_app import db, ma


def run_app():
    app = Flask(__name__)

    db.init_app(app)
    ma.init_app(app)
    app.config.from_object(runtime_config())
    app.register_blueprint(pages_view)
    app.secret_key = runtime_config().SECRET_KEY
    app.register_blueprint(create_db)
    app.register_blueprint(one_to_many)
    app.register_blueprint(user_api)
    app.register_blueprint(flower_api)
    app.register_error_handler(404, error_404)
    Bcrypt(app)
    return app
