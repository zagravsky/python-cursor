from flask import Flask

app = Flask(__name__)

class Developer:
    def __init__(self, firs_name, last_name, programming_language):
        self.f_name = firs_name
        self.l_name = last_name
        self.p_lang = programming_language

    def __str__(self):
        return f'{self.f_name} {self.l_name} - {self.p_lang}'

dev0 = Developer("pvlo", "prokopets", "puthon")
dev1 = Developer("dsfsd", "fsdfsd", "sfdsdf")
dev2 = Developer("sdf", "sgfbhg", "sfvbxvdsdf")
dev3 = Developer("dsfsguty1d", "fsd445fsd", "sfuidsdf")
dev4 = Developer("dsxcfsd", "fsdfsdop;", "sfdsd,mf")
dev5 = Developer("dsfcvsd", "fsd4fsd", "sfds14df")
devs = [dev0, dev1, dev2, dev3, dev4, dev5]

@app.route('/')
def developer_controller():
    return str(dev0)

@app.route('/remove_developer')
def remove_developer():
    if len(devs) == 1:
        return f'list is empty'
    else:
        devs.pop()
        return "<br>".join(map(lambda d: str(d), devs))

if __name__ == '__main__':
    app.run(port=4001, host="127.0.0.1", debug=True)
