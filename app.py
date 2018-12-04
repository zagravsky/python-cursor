from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def developer_controller():
    dev_instance = Developer('roman', 'ponomaryov', 'python3')
    return dev_instance.get_info()


dev_array = [['Guido', 'van Rossum', 'Python'],
            ['Dennis', 'Ritchie', 'C'],
            ['James', 'Gosling', 'Java'],
            ['Yukihiro', 'Matsumoto', 'Ruby']]


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.programming_language = str(programming_language)

    def get_info(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/remove_developer')
def remove_developer():
    if len(dev_array) >= 2:
        dev_array.pop(0)
        output_string = ''
        for i in dev_array:
            dev_instance = Developer(i[0], i[1], i[2])
            output_string += f'{dev_instance.get_info()} <br>'
        return json.dumps(output_string).replace('"', '')
    elif len(dev_array) == 1:
        dev_array.pop(0)
        return 'Developers list is empty'
    else:
        return 'Developers list is empty'
