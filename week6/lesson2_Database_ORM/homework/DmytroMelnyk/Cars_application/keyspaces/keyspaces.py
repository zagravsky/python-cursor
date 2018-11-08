from flask import Blueprint
from flask.views import MethodView

from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.db.app_database import db

create_db = Blueprint('create_db', __name__)


class CreateDataBaseVeiw(MethodView):
    """
    Create db tables
    """

    def post(self):
        db.create_all()
        db.session.commit()
        return "Successfully created all tables"


create_db.add_url_rule('/keyspaces', view_func=CreateDataBaseVeiw.as_view('create_db'))
