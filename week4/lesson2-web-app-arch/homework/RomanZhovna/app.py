from flask import Flask
app = Flask(__name__)


class Developer:
    def __init__(self, first_name: str, last_name: str, language: str):
        self.first_name = first_name
        self.last_name = last_name
        self.language = language

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.language}"


developers = []
dev1 = Developer('Student1', 'Last_name1', 'C')
dev2 = Developer('Student2', 'Last_name2', 'Python')
dev3 = Developer('Student3', 'Last_name3', 'Java')
developers.append(dev1)
developers.append(dev2)
developers.append(dev3)


@app.route('/')
def developer_controller():
    dev1 = Developer('Roman', 'Zhovna', 'Python')
    return f"{dev1}"


@app.route('/remove_developer')
def remove_developer():
    if not developers:
        return f"List of developers is empty"
    else:
        del developers[0]
        if not developers:
            return f"List of developers is empty"
        else:
            output = ''
            for dev in developers:
                output += f"{dev.first_name} {dev.last_name} - {dev.language}\n"
            return output.replace('\n', '<br />')
