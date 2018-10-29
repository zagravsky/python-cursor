from task_1 import *

if __name__ == '__main__':
    python_developer = PythonDeveloper(1, 'Nastia')
    print(python_developer)
    print(python_developer.about())
    print(python_developer.write_code())

    java_developer = JavaDeveloper(5, 'Dima')
    print(java_developer)
    print(java_developer.about())
    print(java_developer.write_code())

    ruby_developer = RubyDeveloper(7, 'Ira')
    print(ruby_developer)
    print(ruby_developer.about())
    print(ruby_developer.write_code())

    company_employees = IT_company()
    company_employees += python_developer
    company_employees += java_developer
    company_employees += ruby_developer
    print(company_employees)
