class Company:
    def __init__(self, company_name: str):
        self.name = company_name
        self.developer_list = []

    def __add__(self, dev):
        if dev.years_experience >= 3:
            self.developer_list.append(dev)
        else:
            print('Sorry. Little experience')

    def __str__(self):
        return '\n'.join([str(dev) for dev in self.developer_list])

    def __len__(self):
        return len(self.developer_list)

    def fire_an_employee(self, name_dev):
        for dev in self.developer_list:
            if dev.name == name_dev:
                self.developer_list.remove(dev)
                return print('OK. Employee fired')
        return print('Error. No such employee found')


if __name__ == "__main__":
    from Task1 import *

    comp = Company('Cursor')
    pDev = PythonDeveloper('Alexandr', 9)
    jDev = JavaDeveloper('Konstantin', 2)
    rDev = RubyDeveloper('Boris', 8)

    comp + pDev
    comp + jDev
    comp + rDev

    print(comp)

    comp.fire_an_employee('Boris')

    print(comp)