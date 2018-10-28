from flask import Blueprint, json
from flask.views import MethodView
from flask import request, current_app


class ModMembers(MethodView):
    def post(self):
        db = current_app.config.get('DB')
        data = json.loads(request.data)
        if not data:
            return f"Please, specify footballer info to be added as data"
        else:
            for key, value in data.items():
                db[key] = value
                return f"Footballer {key} successfully added"

    def delete(self):
        db = current_app.config.get('DB')
        args = request.args
        if not args:
            return f"Please, specify surname to be deleted as a parameter"
        else:
            db.pop(args.get("Surname"))
            return f"Footballer successfully deleted"


bpmod = Blueprint('bpmod', __name__)
bpmod.add_url_rule('/modmembers', view_func=ModMembers.as_view('bpmod'))
