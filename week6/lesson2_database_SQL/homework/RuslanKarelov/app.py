from flask import Flask

from database.data import db, ma
from api_server.api import api
from view.start_page import start_page
from view.report_page import report_page

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ruslan:1994@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)
app.register_blueprint(api)
app.register_blueprint(start_page)
app.register_blueprint(report_page)

if __name__ == "__main__":
    app.run(debug=True)
