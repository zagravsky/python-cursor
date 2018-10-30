from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Task 1 page', time=datetime.now())


@app.route('/newpage')
def newpage():
    return render_template('newpage.html', title='Task 2 page')


if __name__ == '__main__':
    app.run(debug=True)
