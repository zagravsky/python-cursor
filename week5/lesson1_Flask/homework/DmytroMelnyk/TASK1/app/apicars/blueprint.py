from flask import Blueprint, render_template

apicars = Blueprint('apicars', __name__, template_folder='templates')


@apicars.route('/')
def index():
    return render_template('apicars/home.html')
