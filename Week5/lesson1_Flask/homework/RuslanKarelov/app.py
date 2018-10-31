from flask import Flask

from api.config import my_config
from api.api import api
from view.home_page import home


app = Flask(__name__)

app.config.from_object(my_config())
app.register_blueprint(api)
app.register_blueprint(home)


if __name__ == "__main__":
    app.run(debug=True)
