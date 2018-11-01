from flask import Flask

app = Flask(__name__)

dev_list = []

class Developer():
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
    	return f'{self.first_name} {self.last_name} - {self.programming_language}'

marshall = Developer('Marshall', 'Mathers', 'PHP')
margaret = Developer('Margaret', 'Thatcher', 'Java')
anthony = Developer('Anthony', 'Hopkins', 'C++')

dev_list.append(marshall)
dev_list.append(margaret)
dev_list.append(anthony)

def output_list():
	return '<br>'.join([str(d) for d in dev_list])

@app.route('/')
def developer_controller():
    dev = Developer('Igor', 'Tagintsev', 'Python')
    return str(dev)

@app.route('/remove_developer')
def remove_developers():
	if not dev_list:
		return 'List is empty'
	else:
		dev_list.pop()
		return 'List is empty' if not dev_list else output_list()