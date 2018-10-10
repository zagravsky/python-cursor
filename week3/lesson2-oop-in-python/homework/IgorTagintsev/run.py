from utils.task_1 import *
from utils.task_2 import *
from utils.task_3 import *


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
