from flask import Flask
app = Flask(__name__)


class Developer:
    def __init__(self, first_name: str, last_name: str, language: str):
        self.first_name = first_name
        self.last_name = last_name
        self.language = language

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.language}"


developers = [
                {"first_name": "Student1", "last_name": "Last_name1", "language": "C"},
                {"first_name": "Student2", "last_name": "Last_name2", "language": "Python"},
                {"first_name": "Student3", "last_name": "Last_name3", "language": "Java"},
             ]


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
        output = ''
        for dev in developers:
            output += f"{dev['first_name']} {dev['last_name']} - {dev['language']}\n"
        return output.replace('\n', '<br />')
