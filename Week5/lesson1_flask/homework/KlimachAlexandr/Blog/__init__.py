from datetime import timedelta
from flask import Flask, render_template
from Blog.config import runtime_config
from Blog.RESTapi.api import API
from Blog.blog import blog
from Blog.auth import auth


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config.from_object(runtime_config())
    app.register_blueprint(API)
    app.register_blueprint(blog)
    app.register_blueprint(auth)
    app.permanent_session_lifetime = timedelta(minutes=5)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('blog/404.html'), 404

    return app
