from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html', title='Home')


@app.route('/time')
def time():
    time_now = datetime.now()
    return render_template('time.html', title='Time', time=time_now)


@app.route('/new_page')
def new_page():
    return render_template('new_page_1.html', title='new_page_1')


@app.route('/new_page_2')
def new_page_2():
    return render_template('new_page_2.html', title='new_page_2')


if __name__ == '__main__':
    app.run(debug=True)
