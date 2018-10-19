from flask import Flask

app = Flask(__name__)

developers_list = [
    {'f_name': 'Konrad', 'l_name': 'Zuse', 'p_lang': 'Plankalkul'},
    {'f_name': 'Bruce', 'l_name': 'Willis', 'p_lang': 'Assembly'},
    {'f_name': 'Kenneth', 'l_name': 'Thompson', 'p_lang': 'C'}
]


class Developer:
    def __init__(self, f_name, l_name, p_lang):
        self.first_name = f_name
        self.last_name = l_name
        self.programming_language = p_lang

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    dev = Developer('Alex', 'Klimach', 'Python')
    return str(dev)


@app.route('/remove_developer')
def remove_developer():
    if len(developers_list) > 1:
        developers_list.pop()
        return '\n'.join([str(f"{d['f_name']} {d['l_name']} - {d['p_lang']}") for d in developers_list])
    else:
        return 'List of dev is empty'
