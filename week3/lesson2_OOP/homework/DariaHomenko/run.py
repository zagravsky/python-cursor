import task_1 as members_of_company
import task_3 as company


if __name__ == "__main__":
    print('---------------------Task_1---------------------')
    Jek = members_of_company.PythonDeveloper("Jek", 5)
    print(Jek.about(), '\n', Jek.write_code(), '\n')

    Tom = members_of_company.JavaDeveloper("Tom", 3)
    print(Tom.about(), '\n', Tom.write_code(), '\n')

    Alex = members_of_company.RubyDeveloper("Alex", 9)
    print(Alex.about(), '\n', Alex.write_code(), '\n')

    Nik = members_of_company.RubyDeveloper("Nik", 2)
    print('Magic method - __str__:  {}'.format(Nik))
    print('Magic method - __call__:  {}'.format(Nik()))

    print('\n', '---------------------Task_3---------------------')
    my_IT_company = company.IT_Company()
    my_IT_company += Tom
    my_IT_company += Alex
    my_IT_company += Jek

    my_IT_company.company_employee()

    print('\n')
    my_IT_company -= Jek
    my_IT_company.company_employee()

    print('\n')
    my_IT_company -= Nik

    print('\n')
    my_IT_company += Nik
