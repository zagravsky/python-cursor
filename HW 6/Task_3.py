class IT_company:
    def __init__(self, company_name:str):
        self.company_name=company_name
        self.developers=[]

    def __add__(self, developer):
        self.experience=developer.years_experience
        if self.experience <=3:
            print('We need middle developer. Experience of dev {name} too small for this job.'.format(name=developer.name))
        else:
            self.developers.append(developer)

    def __str__(self):
        sorted_list = sorted(self.developers, key=lambda developer:developer.years_experience)

        return '\n'.join([str(dev) for dev in sorted_list])


    def dev_fire(self, name_of_dev):
        for dev in self.developers:
            if dev.name == name_of_dev:
                self.developers.remove(dev)
                return print("{name} was fired.".format(name=name_of_dev))

        return print("We don't have this employee!")


if __name__ == '__main__':
    from HW6.Task_1 import *

    company = IT_company('SoftServe')
    pyDev = PythonDeveloper('Mihail', 7)
    jaDev = JavaDeveloper('Viktor', 3)
    ruDev = RubyDeveloper('Nikolay', 5)

    company + pyDev
    company + jaDev
    company + ruDev

    print('\n')
    print('Before party:')
    print(company)
    print('\n')
    company.dev_fire('Mihail')
    print("After party")
    print(company)

