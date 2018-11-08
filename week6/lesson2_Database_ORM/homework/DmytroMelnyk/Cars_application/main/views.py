from datetime import datetime

from flask import Blueprint, render_template
from flask.views import MethodView

main = Blueprint('main', __name__)


class HomePageView(MethodView):
    def get(self):
        return render_template('home_page.html', title='HomePage')


class AboutPageView(MethodView):
    def get(self):
        return render_template('about_page.html', title='AboutPage')


class IndexPageView(MethodView):
    def get(self):
        return render_template('index_page.html', time=datetime.now(), title='indexPage')


main.add_url_rule('/about', view_func=AboutPageView.as_view('about'), methods=['GET'])
main.add_url_rule('/home', view_func=HomePageView.as_view('home'), methods=['GET'])
main.add_url_rule('/', view_func=IndexPageView.as_view('index'), methods=['GET'])
