import datetime
from flask import Blueprint, render_template
from flask.views import MethodView


class Home(MethodView):
    def get(self):
        date_list = [datetime.datetime.utcnow() - datetime.timedelta(days=5*i) for i in range(3)]
        return render_template('home.html', date_list=date_list)


class Other(MethodView):
    def get(self):
        return render_template('other.html')


myjinja = Blueprint('myjinja', __name__)
myjinja.add_url_rule('/home', view_func=Home.as_view('home'))
myjinja.add_url_rule('/other', view_func=Other.as_view('other'))

