from RuslanKarelov.Developers_task3 import *

from flask import Flask

app = Flask(__name__)

dev1 = Developer("Igor", "Petrenko", "R")
dev2 = Developer("Sergiy", "Zeleniy", "Go")
dev3 = Developer("Sasha", "Grey", "PHP")
Developers = {}
Developers["dev1"] = f"{dev1.first_name} {dev1.last_name} - {dev1.programing_language}"
Developers["dev2"] = f"{dev2.first_name} {dev2.last_name} - {dev2.programing_language}"
Developers["dev3"] = f"{dev3.first_name} {dev3.last_name} - {dev3.programing_language}"


@app.route('/remove_developer')
def remove_dev():
    key = [j for j in Developers.keys()]
    try:
        del Developers[key[0]]
        developers = ""
        for dev in Developers.values():
            developers += dev+",\n"
        if developers == "":
            return "List of developers is empty"
        else:
            return developers
    except IndexError:
        return "List of developers is empty"
