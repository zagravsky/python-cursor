from utils.task_1 import *
from utils.task_2 import *
from utils.task_3 import *

if __name__ == "__main__":
    print('####### TASK 1 #######', end='\n\n')
    jv_dev = JavaDeveloper('Gosling', 10)
    py_dev = PythonDeveloper('Rossum', 8)
    rb_dev = RubyDeveloper('Matsumoto', 3)

    print(py_dev.about(), py_dev.write_code(), py_dev, py_dev(), sep='\n', end='\n\n')
    print(jv_dev.about(), jv_dev.write_code(), jv_dev, jv_dev(), sep='\n', end='\n\n')
    print(rb_dev.about(), rb_dev.write_code(), rb_dev, rb_dev(), sep='\n', end='\n\n')

    print('####### TASK 2 #######', end='\n\n')
    print(E.mro(), end='\n\n')

    print('####### TASK 3 #######', end='\n\n')
    new_company = ItCompany('New Code')

    new_company + py_dev
    new_company + jv_dev
    new_company + rb_dev
    print(new_company)
    new_company.firing_dev('Rossum')
    print(new_company)
    new_company.firing_dev('Jim')