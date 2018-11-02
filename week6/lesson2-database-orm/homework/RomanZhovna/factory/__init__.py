from flask import Flask

from factory.api.getinfo import bpinfo
from factory.api.moddata import bpmod
from factory.ui.home_page import home
from factory.ui.login import login
from factory.ui.list import player
from factory.config import runtime_config
from factory.flask_db import db, ma
from factory.api.create_db import create_db_api


def run_app():
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_object(runtime_config())
    app.register_blueprint(bpinfo)
    app.register_blueprint(bpmod)
    app.register_blueprint(home)
    app.register_blueprint(login)
    app.register_blueprint(player)
    app.register_blueprint(create_db_api)

    return app
