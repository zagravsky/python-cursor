from flask import Blueprint, render_template, current_app
from flask.views import MethodView


class HomePage(MethodView):
    def get(self):
        news = current_app.config.get('NEWS')
        return render_template('home.html', news=news)


home = Blueprint('home', __name__)
home.add_url_rule('/home', view_func=HomePage.as_view('home'))
