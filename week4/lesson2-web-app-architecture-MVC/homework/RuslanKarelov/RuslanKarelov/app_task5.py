from flask import Flask

app = Flask(__name__)


Developers = {"Dev1": ("Igor", "Petrenko", "R"),
              "Dev2": ("Valera", "Mihalok", "Java"),
              "Dev3": ("Sasha", "Grey", "PHP")}


@app.route('/remove_developer')
def remove_dev():
    for dev in Developers.keys():
        Developers.pop(dev, "GH")
        text = ""
        for val in Developers.values():
            text += f"<p>{val[0]} {val[1]} - {val[2]}</p>"
        if not text == "":
            return text
        else:
            return "List of developers is empty"

    return "List of developers is empty"

