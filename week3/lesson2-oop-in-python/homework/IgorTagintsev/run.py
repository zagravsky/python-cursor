from utils.task_1 import Developer, PythonDeveloper, JavaDeveloper, RubyDeveloper
from utils.task_2 import *
from utils.task_3 import it_company


#Task_1
print('\n-------------------------Task_1-------------------------')

if __name__ == "__main__":
    python_dev = PythonDeveloper(1, 'Igor Tagintsev')
    python_dev.about()
    python_dev.write_code()
    print(python_dev)
    print('-------------')
    java_dev = JavaDeveloper(4, 'Oleg Vinnik')
    java_dev.about()
    java_dev.write_code()
    print(java_dev)
    print('-------------')
    ruby_dev = RubyDeveloper(10, 'Mel Gibson')
    ruby_dev.about()
    ruby_dev.write_code()
    print(ruby_dev)


#Task_2
print('\n-------------------------Task_2-------------------------')

if __name__ == "__main__":
    print(E.mro())


#Task_3
print('\n-------------------------Task_3-------------------------')
if __name__ == "__main__":
    emp_1 = PythonDeveloper(13, 'Igor Tagintsev')
    emp_2 = PythonDeveloper(3, 'Adolf Gitler')
    emp_3 = JavaDeveloper(1, 'Donald Tramp')
    emp_4 = RubyDeveloper(13, 'Angela Mercel')
    emp_5 = Developer(1, 'Ivan Ivanov')
    emp_6 = JavaDeveloper(7, 'Bruse Lee')
    itcompany = it_company()

    itcompany + emp_1
    itcompany + emp_2
    itcompany + emp_3
    itcompany + emp_4
    itcompany + emp_5
    itcompany + emp_6
    print(itcompany)

    itcompany.firing('Angela Mercel')
    print(itcompany)

    itcompany.firing('Angela Mercel')
    print(itcompany)
