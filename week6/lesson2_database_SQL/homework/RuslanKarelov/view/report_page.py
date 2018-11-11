from flask import Blueprint
from view.start_page import MyView
from datetime import date

from api_server.model import CarsTable


report_page = Blueprint('report_page', __name__)


class SeptemberReportView(MyView):

    def template_name(self):
        return 'report_page.html'

    def get_object(self):
        return CarsTable.query.filter(CarsTable.date <= date(2018, 9, 30), CarsTable.date >= date(2018, 9, 1)).all()


class OctoberReportView(SeptemberReportView):
    def get_object(self):
        return CarsTable.query.filter(CarsTable.date <= date(2018, 10, 31), CarsTable.date >= date(2018, 10, 1)).all()


report_page.add_url_rule('/september', view_func=SeptemberReportView.as_view('report_september'))
report_page.add_url_rule('/october', view_func=OctoberReportView.as_view('report_october'))
