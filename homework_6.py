# Task 1
class Developer:
    def __init__(self, years_experience: int, name: str, language: str):
        self.years_experience = years_experience
        self.name = name
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            return f'My name is {self.name} and I am a Junior Developer.'
        elif self.years_experience <= 5:
            return f'My name is {self.name} and I am a Middle Developer.'
        else:
            return f'My name is {self.name} and I am a Senior Developer.'

    def write_code(self):
        return 'I am a developer and I write code'

    def __str__(self):
        return f'{self.name} - {self.years_experience} years, {self.language}'

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, years_experience, name, language='Python'):
        Developer.__init__(self, years_experience, name, language)
        self.language = 'Python'

    def write_code(self):
        return f'I use {self.language} to write code.'


class JavaDeveloper(Developer):
    def __init__(self, years_experience, name, language='Java'):
        Developer.__init__(self, years_experience, name, language)
        self.language = 'Java'

    def write_code(self):
        return 'I use ' + self.language + ' to write code.'


class RubyDeveloper(Developer):
    def __init__(self, years_experience, name, language='Ruby'):
        Developer.__init__(self, years_experience, name, language)
        self.language = 'Ruby'

    def write_code(self):
        return 'I use ' + self.language + ' to write code.'


if __name__ == '__main__':
    employee_A = PythonDeveloper(1, 'Joe')
    employee_B = JavaDeveloper(4, 'Michael')
    employee_C = RubyDeveloper(10, 'Andrew')
    print(employee_A.about())
    print(employee_A.write_code())
    print(employee_B.about())
    print(employee_B.write_code())
    print(employee_C.about())
    print(employee_C.write_code())
    print(employee_A.__str__())
    print(employee_B.__str__())
    print(employee_C.__str__())
    print(employee_A.__call__())
    print(employee_B.__call__())
    print(employee_C.__call__())


# Task 2
class A:
    pass


class B:
    pass


class C(B, A):
    pass


class D(C, A):
    pass


class E(D, B):
    pass


if __name__ == '__main__':
    print(E.__mro__)

# (<class '__main__.E'>, <class '__main__.D'>, <class '__main__.C'>,
#  <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# Task 3

class Company:

    list_of_employees = []

    def __add__(self, employee):
        if employee.years_experience >= 3:
            self.list_of_employees.append(employee)
        else:
            print(f"{employee.name} doesn't have enough experience.")
        return self

    def __repr__(self):
        sort_list = sorted(self.list_of_employees, key=lambda a: a.years_experience)
        return repr([str(emp) for emp in sort_list])

    def fired(self, name: str):
        for employee in self.list_of_employees:
            if name is employee.name:
                self.list_of_employees.remove(employee)
                print(f'Employee {name} was fired from the company!')
                return self
        print(f'Sorry! It seems that employee with name {name} does not work for the company!')
        return self


if __name__ == '__main__':
    employee_A = PythonDeveloper(1, 'Joe')
    employee_B = JavaDeveloper(4, 'Michael')
    employee_C = RubyDeveloper(10, 'Andrew')
    employee_D = PythonDeveloper(5, 'Peter')
    employee_E = JavaDeveloper(7, 'Alex')
    company = Company()
    company += employee_A
    company += employee_B
    company += employee_C
    company += employee_D
    company += employee_E
    print(company)
    print(company.fired('Andrew'))
    print(company.fired('Sam'))




