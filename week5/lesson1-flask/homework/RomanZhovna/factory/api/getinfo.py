from flask import Blueprint
from flask.views import MethodView
from flask import request, jsonify
from flask import current_app


class Footballers(MethodView):
    def get(self):
        db = current_app.config.get('DB')
        args = request.args
        if not args:
            return jsonify(db)
        else:
            return jsonify(db.get(args.get("Surname")))


bpinfo = Blueprint('bpinfo', __name__)
bpinfo.add_url_rule('/getinfo', view_func=Footballers.as_view('bpinfo'))
