from flask import Blueprint, render_template
from flask.views import MethodView

api= Blueprint('api', __name__, template_folder='templates', static_folder='static')

@api.route('/')
def show():
    return render_template('my_api/index.html')