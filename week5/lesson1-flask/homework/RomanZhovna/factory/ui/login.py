from flask import Blueprint, render_template
from flask.views import MethodView


class LoginPage(MethodView):
    def get(self):
        return render_template('login.html')


login = Blueprint('login', __name__)
login.add_url_rule('/login', view_func=LoginPage.as_view('login'))
