from task_1 import Developer, PythonDeveloper, JavaDeveloper, RubyDeveloper
from task_2 import *
from task_3 import It_company

"""
Task 1 about Developers
"""
print("Task 1:")

if __name__ == '__main__':
    dev_1 = PythonDeveloper(1, 'Roman Zolotukha')
    dev_1.about()
    dev_1.write_code()
    print(dev_1)
    dev_2 = RubyDeveloper(15, 'Ivan Ivanenko')
    dev_2.about()
    dev_2.write_code()
    print(dev_2)
    dev_3 = JavaDeveloper(4, 'Roman Romanenko')
    dev_3.about()
    dev_3.write_code()
    print(dev_3)

"""
Task 2 about classes A,B,C,D,E
"""
print('Task 2:')
if __name__ == '__main__':
    print(E.mro())

"""
Task 3 about class IT company
"""
print('Task 3:')
if __name__ == '__main__':
    work_1 = PythonDeveloper(35 , 'Roman Zolotukha')
    work_2 = PythonDeveloper(2, 'Vasya Pupkin')
    work_3 = JavaDeveloper(22, 'Taras Shevshenko')
    work_4 = JavaDeveloper(1, 'Andriy Shevshenko')
    work_5 = RubyDeveloper(12, 'Petro Poroshenko')
    work_6 = RubyDeveloper(2, 'Oleksandra Loboda')
    work_7 = Developer(1, "Secret Guest")

    itcompany = It_company()

    itcompany + work_1
    itcompany + work_2
    itcompany + work_3
    itcompany + work_4
    itcompany + work_5
    itcompany + work_6
    itcompany + work_7

    print(itcompany)

    print(itcompany.firing('Petro Poroshenko'))

    print(itcompany.firing('Petro Poroshenko'))