from flask import Flask
from dev import Developer
import random 

app = Flask(__name__)

Pavlo = Developer('Pavlo', 'Kandiak', 'Python')
Vasyl = Developer('Vasyl', 'Sayko', 'JS')
Roma = Developer('Roma', 'Antonyshyn', 'C#')

developer_list = []
developer_list.append(Pavlo)
developer_list.append(Vasyl)
developer_list.append(Roma)

@app.route('/')
def developer_controller():
	p = Developer('Klymak', 'Anastasia', 'C++')
	return f'{p}'

@app.route('/remove_developer')
def remove_developer():
	
	if len(developer_list):
		developer_list.remove(random.choice(developer_list))
		if len(developer_list):
			st= ''
			for i in developer_list:
				st += f'{i}, '
			return st[:-2]
		else:
			return 'The list is empty'
	else:
		return 'The list is empty'
