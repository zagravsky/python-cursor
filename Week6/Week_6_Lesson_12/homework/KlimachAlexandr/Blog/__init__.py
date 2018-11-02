from datetime import timedelta
from flask import Flask, render_template
from Blog.config import runtime_config
from Blog.RESTapi.api import API
from Blog.blog import blog
from Blog.auth import auth
from Blog.database.init_db import init_db
from Blog.database.db import db, ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alexandr:1@localhost:5432/w6l2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
    app.secret_key = 'secret'
    app.register_blueprint(init_db)
    app.config.from_object(runtime_config())
    app.register_blueprint(API)
    app.register_blueprint(blog)
    app.register_blueprint(auth)
    app.permanent_session_lifetime = timedelta(minutes=5)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('blog/404.html'), 404

    return app
