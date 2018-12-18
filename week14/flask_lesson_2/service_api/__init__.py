from flask import Flask

from service_api.api.character_api import character_api
from service_api.api.author_api import author_api
from service_api.api.books_api import books_api
from service_api.api.genre_api import genre_api
from service_api.api.id_card_api import id_card
from service_api.api.user_api import user_api
from service_api.app_database import db, ma, migrate
from service_api.config import runtime_config
from service_api.keyspaces.keyspaces import create_db_api


def run_app():
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    app.config.from_object(runtime_config())
    app.register_blueprint(create_db_api)
    app.register_blueprint(author_api)
    app.register_blueprint(books_api)
    app.register_blueprint(character_api)
    app.register_blueprint(genre_api)
    app.register_blueprint(user_api)
    app.register_blueprint(id_card)
    return app
