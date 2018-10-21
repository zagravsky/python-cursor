from flask import Flask

app = Flask(__name__)

dev_list = []


class Developer:
    def __init__(self, f_name, l_name, p_lang):
        self.first_name = f_name
        self.last_name = l_name
        self.programming_language = p_lang

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'


konrad = Developer('Konrad', 'Zuse', 'Plankalkul')
bruce = Developer('Bruce', 'Willis', 'Assembly')
kenneth = Developer('Kenneth', 'Thompson', 'C')

dev_list.append(konrad)
dev_list.append(bruce)
dev_list.append(kenneth)


def output_list():
    return '<br>'.join([str(f"{d.first_name} "
                            f"{d.last_name} - "
                            f"{d.programming_language}") for d in dev_list])


@app.route('/')
def developer_controller():
    dev = Developer('Alex', 'Klimach', 'Python')
    return str(dev)


@app.route('/remove_developer')
def remove_developer():
    empty = 'List of dev is empty'
    if not dev_list:
        return empty
    else:
        dev_list.pop()
        return empty if not dev_list else output_list()


if __name__ == '__main__':
    app.run()
