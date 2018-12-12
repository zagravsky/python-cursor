from flask import Flask
from developer_controller import Developer

app = Flask(__name__)

@app.route('/')
def developer_controller():
    devs_1 = Developer('Anton', 'Antonov', 'Python')
    return f'{devs_1}'

devs_2 = Developer ('Maxim', 'Maximov', 'JS')
devs_3 = Developer ('Dmitrii', 'Dmitriev', 'Ruby')
devs_4 = Developer ('Anton', 'Antonov', 'Python')

devs_list = []
devs_list.append(devs_2)
devs_list.append(devs_3)
devs_list.append(devs_4)



@app.route('/remove_developer')
def remove_developer():
    try:
        del devs_list[0]
        return '<br>'.join([f"{d}" for d in devs_list])
    except:
        return 'List is empty'