from flask import Blueprint, render_template, current_app, url_for
from flask.views import MethodView
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from factory.model import PlayersTable


class ListPlayers(MethodView):
    def get(self):
        table = PlayersTable.query.order_by(PlayersTable.id).all()
        return render_template('players.html', db=table)


class Player(MethodView):
    def get(self, id):
        row = PlayersTable.query.filter_by(id=id).first()
        return render_template('player.html', player=row)


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
player.add_url_rule('/<id>', view_func=Player.as_view('player'))
