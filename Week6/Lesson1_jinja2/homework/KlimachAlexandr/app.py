from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    date = datetime.now()
    return render_template('pages/home.html', date=date)


@app.route("/github")
def github():
    return render_template('pages/Github.html')


@app.route("/Jinja2")
def jinja2():
    return render_template('pages/Jinja2.html')


if __name__ == "__main__":
    app.run()
