from typing import List, Dict, Any, Union


class Team:
    def __init__(self):
        self.team: List[Dict[str, Any]] = []

    def hire_employees(self, *args: Dict[str, Union[str, int]]) -> None:
        print('Hiring:')
        for applicant in args:
            if applicant['years_experience'] < 3:
                print(f"!! Experience of {applicant['name']} is not enough")
            else:
                print(f"{applicant['name']} is added to the team")
                self.team.append(applicant)

    def print_employees(self) -> None:
        if self.team:
            print('Employees list:')
            for employee in sorted(self.team, key=lambda employee_: employee_['years_experience']):
                print("{} - {} years, {}".format(*employee.values()))
        else:
            print('No employees')

    def dismiss_employees(self, *args: str) -> None:
        dismission_list: list = list(args)
        if self.team:
            print('Dismission:')
            for name in dismission_list:
                if name not in [employee['name'] for employee in self.team]:
                    print(f"No employee with name {name}")
            for employee in reversed(self.team):
                if employee['name'] in dismission_list:
                    self.team.remove(employee)
                    dismission_list.remove(employee['name'])
        else:
            print('No employees')


if __name__ == '__main__':
    from task_1 import PythonDeveloper, JavaDeveloper, RubyDeveloper

    py = PythonDeveloper('Pythonista', 8)
    ja = JavaDeveloper('Javista', 5)
    rb = RubyDeveloper('Rubyista', 2)

    new_team = Team()
    new_team.hire_employees(vars(py), vars(py), vars(ja), vars(rb)); print()
    new_team.print_employees(); print()
    new_team.dismiss_employees('Pythonista', 'Javista', 'Golangista'); print()
    new_team.print_employees()
