from flask import Flask


class Developer():
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.programming_language = str(programming_language)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


class Devs_list():
    devs = []

    def __add__(self, dev):
        self.devs.append(dev)
        return self

    def __str__(self):
        current_devs = [(dev.first_name, dev.last_name, dev.programming_language) for dev in self.devs]
        return f'{current_devs}'

    def delete_dev(self):
        del self.devs[0]


dev_1 = Developer("VIktor", "Burlakov", "Python")
dev_2 = Developer("Kolya", "Shotakoe", "C#")
dev_3 = Developer("Nastya", "Koma", "Salesforce")
dev_4 = Developer("Robot", "1100", "JS")
devs_list = Devs_list()

devs_list += dev_1
devs_list += dev_2
devs_list += dev_3
devs_list += dev_4

app = Flask(__name__)


@app.route('/')
def developer_controller():
    dev = Developer("Viktor", "Burlakov", "Python")
    return f'{dev}'


@app.route('/remove_developer')
def remove_developer():
    try:
        devs_list.delete_dev()  # разрабы не удаляются!!!!
        return f'{devs_list}'

    except:
        return f"List is empty"

