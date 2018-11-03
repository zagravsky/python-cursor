from flask import Flask, render_template
import json
from datetime import datetime

app = Flask(__name__, template_folder='./template', static_folder='./static')

with open('database/data.json', 'r') as file:
    data = json.load(file)


def convert_to_datetime(some_data):
    for dict_with_data in some_data:
        for data in dict_with_data["data"]:
            data["date"] = datetime.strptime(data["date"], "%Y/%m/%d")
    return some_data


convert_to_datetime(data)


@app.route('/')
def home_page():
    return render_template('home.html', data=data)


@app.route('/<string:id>')
def data_from_db(id):
    for d in data:
        if id == d["id"]:
            return render_template('report.html', data=data, month=d)


if __name__ == "__main__":
    app.run(debug=True)
