from flask import Flask
from api.api import user_api
from db_config import db



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookdatabase.db"
db.init_app(app)
app.register_blueprint(user_api)
