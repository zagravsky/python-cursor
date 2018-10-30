from flask import Flask

app = Flask(__name__)


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


@app.route('/')
def developer_controller():
    dev = Developer('Roman', 'Zolotukha', 'Python')
    return str(dev)


dev_list = []

dev1 = Developer('Andy', 'Nazarenko', 'Java')
dev2 = Developer('Yuriy', 'Dudy', 'JS')
dev3 = Developer('Andry', 'Poltava','C++')

dev_list.append(dev1)
dev_list.append(dev2)
dev_list.append(dev3)


def new_list_devs():
    return '<br>'.join([str(x) for x in dev_list])


@app.route('/remove_developer')
def remove_developer():
    null = 'list of Developers is vacant'
    if not dev_list:
        return null
    else:
        dev_list.pop()
        return null if not dev_list else new_list_devs()


if __name__ == '__main__':
    app.run()
