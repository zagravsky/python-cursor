from utils.task_1 import PythonDeveloper, JavaDeveloper, RubyDeveloper
from utils.task_2 import E
from utils.task_3 import Team

if __name__ == "__main__":
    print('==== TASK 1 ====')
    py = PythonDeveloper('Pythonista', 8)
    ja = JavaDeveloper('Javista', 5)
    rb = RubyDeveloper('Rubyista', 2)

    print(vars(py), py.about(), py.write_code(), py, py(), sep='\n', end='\n\n')
    print(vars(ja), ja.about(), ja.write_code(), ja, ja(), sep='\n', end='\n\n')
    print(vars(rb), rb.about(), rb.write_code(), rb, rb(), sep='\n', end='\n\n')

    print('==== TASK 2 ====')
    print(E.mro(), end='\n\n')

    print('==== TASK 3 ====')
    new_team = Team()
    new_team.hire_employees(py, py, ja, rb)
    print()
    new_team.print_employees()
    print()
    new_team.dismiss_employees('Pythonista', 'Javista', 'Golangista')
    print()
    new_team.print_employees()
