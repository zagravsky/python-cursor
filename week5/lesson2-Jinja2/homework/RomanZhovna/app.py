from flask import Flask
from lesson2.api import myjinja


app = Flask(__name__)
app.register_blueprint(myjinja)


@app.template_filter('datefilter')
def datefilter(value, format='%B %d, %Y'):
    return value.strftime(format)


if __name__ == '__main__':
    app.run()
