from flask import Flask

app = Flask(__name__)

devs_list = [{'first_name': 'Anton', 'last_name': 'Antonov', 'programming_language': 'Python'},
                {'first_name': 'Maxim', 'last_name': 'Maximov', 'programming_language': 'JS'},
                {'first_name': 'Dmitrii', 'last_name': 'Dmitriev', 'programming_language': 'Ruby'},
                {'first_name': 'Anton', 'last_name': 'Antonov', 'programming_language': 'Python'}]

class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.programming_language = str(programming_language)

    def __str__(self):
        return '{first_name} {last_name} - {programming_language}'.format(first_name=self.first_name,
                                                                          last_name=self.last_name,
                                                                          programming_language=self.programming_language)

@app.route('/')
def developer_controller():
    object_dev=Developer('Fedor','Fedorov','Python')
    return f'{object_dev}'

@app.route('/remove_developer')
def remove_developer():
    try:
        del devs_list[0]
    except:
        return 'List is empty'
    return '<br>'.join([f"{d['first_name']} {d['last_name']} - {d['programming_language']}" for d in devs_list])
