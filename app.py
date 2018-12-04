from flask import Flask
app = Flask(__name__)


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    dev_instance = Developer('roman', 'ponomaryov', 'python3')
    return str(dev_instance)


dev_array = [
            Developer('Guido', 'van Rossum', 'Python'),
            Developer('Dennis', 'Ritchie', 'C'),
            Developer('James', 'Gosling', 'Java'),
            Developer('Yukihiro', 'Matsumoto', 'Ruby')
            ]


@app.route('/remove_developer')
def remove_developer():
    if not dev_array:
        return 'Developers list is empty'
    dev_array.pop(0)
    if dev_array:
        output_string = '<br>'.join(list(map(lambda dev: str(dev), dev_array)))
        return output_string.replace('[', '').replace(']', '').replace('\'', '')
    return 'Last developer was removed'
