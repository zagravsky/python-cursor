from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "5f31c532e88134d18c12517d3c70a80a"


from task_2 import routes
