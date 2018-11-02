from flask import Blueprint

from Blog.database.db import db

init_db = Blueprint('init_db', __name__)


@init_db.route('/init_db')
def init_database():
    try:
        db.create_all()
        db.session.commit()
        return "Tables created"
    except:
        return "Check logs"
