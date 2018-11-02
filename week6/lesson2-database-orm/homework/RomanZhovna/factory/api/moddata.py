from flask import Blueprint, request
from flask.views import MethodView
from factory.model import PlayersTable
from factory.schema import player_schema
from factory.flask_db import db


class ModMembers(MethodView):
    def post(self):
        data = request.get_json()
        if not data:
            return f"Please, specify footballer info to be added as data"
        else:
            new_player = PlayersTable(**data)
            db.session.add(new_player)
            db.session.commit()
            return player_schema.jsonify(new_player)

    def delete(self, id):
        row = PlayersTable.query.filter_by(id=id).first()
        db.session.delete(row)
        db.session.commit()
        return player_schema.jsonify(row)


bpmod = Blueprint('bpmod', __name__)
bpmod.add_url_rule('/modmembers', view_func=ModMembers.as_view('bpmod_post'))
bpmod.add_url_rule('/modmembers/<id>', view_func=ModMembers.as_view('bpmod_del'))
