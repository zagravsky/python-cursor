from utils.task_1 import *
from utils.task_2 import *
from utils.task_3 import *

if __name__ == "__main__":

    print('--------------Task 1--------------', end='\n\n')

    pd = PythonDeveloper(2, 'Oleg')
    jd = JavaDeveloper(4, 'Andriy')
    rd = RubyDeveloper(6, 'Vitaliy')

    pd.about()
    pd.write_code()
    print(pd)
    print(pd(), end='\n\n')

    jd.about()
    jd.write_code()
    print(jd)
    print(jd(), end='\n\n')

    rd.about()
    rd.write_code()
    print(rd)
    print (rd(), end='\n\n')

    print('--------------Task 2--------------', end='\n\n')

    print(E.mro(), end='\n\n')

    print('--------------Task 3--------------', end='\n\n')

    cursor = Company()

    pd = PythonDeveloper(2, 'Xander')
    jd = JavaDeveloper(4, 'Ostin')
    rd = RubyDeveloper(6, 'Zed')
    pd1 = PythonDeveloper(4, 'Perry')
    jd1 = JavaDeveloper(5, 'Zyz')
    rd1 = RubyDeveloper(3, 'Oliver')
    pd2 = PythonDeveloper(7, 'Perry')
    jd2 = JavaDeveloper(4, 'Elder')
    rd2 = RubyDeveloper(9, 'Kyle')

    cursor += pd
    cursor += jd
    cursor += rd
    cursor += pd1
    cursor += jd1
    cursor += rd1
    cursor += pd2
    cursor += jd2
    cursor += rd2

    cursor.delete('Elder')
    cursor.delete('Endy')

    print(cursor)