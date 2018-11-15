from flask import Flask
import random
app = Flask(__name__)


class Developer:
    def __init__(self, first_name, last_name, programing_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programinig_language = programing_language

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.programinig_language}"


dev_1 = Developer("Julius", "Ceasar", "imperial")
dev_2 = Developer("Markus", "Avrelius", "C++")
dev_3 = Developer("Neron", "X3", "burn_rome")
dev_4 = Developer("Volodymyr", "Monomah", "python")
devs = [dev_1, dev_2, dev_3, dev_4]


@app.route('/')
def developer_controller():
    return str(dev_1)


@app.route('/remove_developer')
def remove_developer():
    devs_view = ""
    if len(devs) == 1:
        return "There is no developers left."
    else:
        devs.remove(random.choice(devs))
        for dev in devs:
            devs_view += f"{dev.first_name} {dev.last_name} - {dev.programinig_language}<br>"
        return devs_view


app.run()
