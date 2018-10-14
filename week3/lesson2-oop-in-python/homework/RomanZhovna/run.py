from utils.task1 import Developer, Python, Ruby, Java
from utils.task2 import E
from utils.task3 import Employees

if __name__ == "__main__":
    break_line = '=' * 50

    print("Task1")
    dev1 = Developer(2, 'Homer')
    print(dev1.about())
    print(dev1.write_code())
    print(dev1)
    print(dev1())
    print(break_line)

    dev2 = Python(3, 'Batman')
    print(dev2.about())
    print(dev2.write_code())
    print(dev2)
    print(dev2())
    print(break_line)

    dev3 = Ruby(5, 'Hulk')
    print(dev3.about())
    print(dev3.write_code())
    print(dev3)
    print(dev3())
    print(break_line)

    dev4 = Java(7, 'Superman')
    print(dev4.about())
    print(dev4.write_code())
    print(dev4)
    print(dev4())

    dev5 = Python(4, 'Hulk')
    print(break_line)

    print("Task2")
    print(E.mro())
    print(break_line)

    print("Task3")
    Emp = Employees()
    Emp += dev1
    Emp += dev2
    Emp += dev3
    Emp += dev4
    Emp += dev5
    print(break_line)
    Emp.print_employee()
    print(break_line)
    Emp.fire_employee('Hulk')
    print(break_line)
    Emp.print_employee()
