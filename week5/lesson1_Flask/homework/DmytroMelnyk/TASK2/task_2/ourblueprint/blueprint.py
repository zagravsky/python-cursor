from flask import Blueprint, render_template

carposts = Blueprint('carposts', __name__, template_folder='templates')


@carposts.route('/')
def index():
    return render_template('ourblueprint/index.html')
