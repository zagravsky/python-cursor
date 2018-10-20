from task_1 import *
from task_3 import *


if __name__== '__main__':
    print('--> create programer')
    j1 = JavaDeveloper(2, 'Jameson')
    print(j1)
    print(j1.about())
    print(j1.write_code())
    print('--> create programer')
    p1 = PythonDeveloper(10, 'Jack')
    print(p1)
    print(p1.about())
    print(p1.write_code())
    print('--> create programer')
    r1 = RubyDeveloper(3, 'Danials')
    print(r1)
    print(r1.about())
    print(r1.write_code())

    print('--> create company')

    nemirof = It_company()
    nemirof.add_employee(j1)
    nemirof.add_employee(p1)
    nemirof.add_employee(r1)
    print('--> show employee in company')
    nemirof.show_emloyee()