from flask import Blueprint, render_template, current_app
from flask.views import MethodView

apicars = Blueprint('apicars', __name__, template_folder='templates')


@apicars.route('/')
def index():
    return render_template('apicars/home.html', title=current_app.config.get("TEST_VARIABLE"))
