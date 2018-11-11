from flask import Blueprint, render_template
from flask.views import View

from api_server.model import CarsTable

start_page = Blueprint('start_page', __name__, template_folder='./templates', static_folder='../../static')


class MyView(View):
    def template_name(self):
        raise NotImplementedError()

    def get_object(self):
        raise NotImplementedError()

    def render_template(self, data):
        return render_template(self.template_name(), **data)

    def dispatch_request(self):
        data = {'obj': self.get_object()}
        return self.render_template(data)


class StartPageView(MyView):
    def template_name(self):
        return 'start_page.html'

    def get_object(self):
        return CarsTable.query.all()


start_page.add_url_rule('/', view_func=StartPageView.as_view('start_page'))
