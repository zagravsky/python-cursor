from flask import Blueprint
from flask.views import MethodView
from factory.model import PlayersTable
from factory.schema import player_schema, players_schema


class Footballers(MethodView):
    def get(self, id=''):
        if id:
            player = PlayersTable.query.filter_by(id=id).first()
            return player_schema.jsonify(player)
        else:
            player = PlayersTable.query.order_by(PlayersTable.id).all()
            return players_schema.jsonify(player)


bpinfo = Blueprint('bpinfo', __name__)
bpinfo.add_url_rule('/getinfo', view_func=Footballers.as_view('bpinfo_all'))
bpinfo.add_url_rule('/getinfo/<id>', view_func=Footballers.as_view('bpinfo_one'))

