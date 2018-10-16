from utils.task1 import *
from utils.task2 import *
from utils.task3 import *

if __name__ == '__main__':
    print("\n" + " Task1")
    py_dev = PythonDeveloper(6, "Anton")
    py_dev.about()
    py_dev.write_code()
    print(py_dev,"\n")

    py_dev1 = PythonDeveloper(4, "Alexandr")
    py_dev1.about()
    py_dev1.write_code()
    print(py_dev1, "\n")

    ja_dev = JavaDeveloper(2, "Greg")
    ja_dev.about()
    ja_dev.write_code()
    print(ja_dev, "\n")

    ja_dev1 = JavaDeveloper(5, "Roman")
    ja_dev1.about()
    ja_dev1.write_code()
    print(ja_dev1, "\n")

    ru_dev = RubyDeveloper(3, "Igor")
    ru_dev.about()
    ru_dev.write_code()
    print(ru_dev, "\n")

    ru_dev1 = RubyDeveloper(1, "Gleb")
    ru_dev1.about()
    ru_dev1.write_code()
    print(ru_dev1, "\n")

    print("\n" + " Task2")
    print(E.mro())
    # порядок поиска: E, D, C, B, A, object

    print("\n" + " Task3")
    it_co = IT_company()
    it_co.add(py_dev)
    it_co.add(py_dev1)
    it_co.add(ja_dev)
    it_co.add(ja_dev1)
    it_co.add(ru_dev)
    it_co.add(ru_dev1)

    print('\n')
    it_co.lay_off_emp("Igor")

    print('\n')
    it_co.sort_team()
