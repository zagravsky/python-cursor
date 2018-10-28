from flask import Blueprint, render_template, current_app, url_for
from flask.views import MethodView
from werkzeug.exceptions import abort
from werkzeug.utils import redirect


class ListPlayers(MethodView):
    def get(self):
        db = current_app.config.get('DB')
        return render_template('players.html', db=db)


class Player(MethodView):
    def get(self, name):
        db = current_app.config.get('DB')
        player = db[name]
        return render_template('player.html', player=player)


class RedirectPage(MethodView):
    def get(self):
        return redirect(url_for('player.nonexistant'))


class ErrorPage(MethodView):
    def get(self):
        abort(404, "PLease, specify correct url")


player = Blueprint('player', __name__, static_folder='./static', template_folder='./template')
player.add_url_rule('/', view_func=RedirectPage.as_view('redirect'))
player.add_url_rule('/nonexistant', view_func=ErrorPage.as_view('nonexistant'))
player.add_url_rule('/list', view_func=ListPlayers.as_view('list'))
player.add_url_rule('/<name>', view_func=Player.as_view('player'))
