from flask import Blueprint, render_template, redirect
from flask.views import MethodView


class ApiView(MethodView):
    def get(self):
        return redirect('/login')
            # render_template("home.html")


api = Blueprint('api', __name__, static_folder='./static', template_folder='./template')

api.add_url_rule('/api', view_func=ApiView.as_view('api'))
