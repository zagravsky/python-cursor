from task_1 import *


class It_company():

    employee = []

    def show_emloyee(self):
        for e in (sorted(self.employee, key=lambda developer: developer.years_experience)):
            print (e)


    def add_employee(self, new_employee):
        if isinstance(new_employee, Developer):
            if new_employee.years_experience < 3:
                 print('Not enough experience')
            else:
               self.employee.append(new_employee)
        else:
            print(str(new_employee) + ' is not a programmer')


    def fire_employee(self, name):
        for e in self.employee:
            if e.name == name:
                self.employee.remove(e)
                return "Employee " + name + " is fired"
            else:
                return "Employee " + name + " not found"
