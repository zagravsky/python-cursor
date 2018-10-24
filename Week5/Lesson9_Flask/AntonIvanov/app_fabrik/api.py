from flask import Blueprint, render_template
from flask.views import MethodView

from flask import current_app


class FabrikApiView(MethodView):
    def get(self):
        return current_app.config.get("TEST_VARIABLE")

class HomePageView(MethodView):
    def get(self):
        return render_template("test.html")
        # return "Hello World"



factory_api = Blueprint('factory_api', __name__, static_folder='../static', template_folder='../templates')

factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))

homepage_api = Blueprint('homepage_api', __name__, static_folder='../static',template_folder='../templates')
homepage_api.add_url_rule('/',view_func=HomePageView.as_view('homepage_api'))
