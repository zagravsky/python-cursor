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
        sorted_list = sorted(self.developer_list, key=lambda dev: dev.years_experience)
        return '\n'.join([str(dev) for dev in sorted_list])

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
    rDev = RubyDeveloper('Boris', 1)
    pDev_1 = PythonDeveloper('Grigoriy', 7)
    jDev_2 = JavaDeveloper('Banjamin', 5)
    rDev_3 = RubyDeveloper('Denis', 3)
    pDev_4 = PythonDeveloper('Fedor', 11)
    jDev_5 = JavaDeveloper('Bogdan', 4)
    rDev_6 = RubyDeveloper('Kolya', 2)

    comp + pDev
    comp + jDev
    comp + rDev
    comp + pDev_1
    comp + jDev_2
    comp + rDev_3
    comp + pDev_4
    comp + jDev_5
    comp + rDev_6

    print(comp)

    comp.fire_an_employee('Fedor')

    print(comp)