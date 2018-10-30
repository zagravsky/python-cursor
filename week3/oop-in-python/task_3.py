class IT_company():

    employees = []

    def __add__(self, employee):
        if employee.years_experience > 3:

            self.employees.append(employee)
        else:
            return 'Sorry, but {} year(s) of experience are not enough for the company'.format(employee.years_experience)
        return self

    def __str__(self):
        employee_name = ''
        for i in sorted(self.employees, key=lambda x: x.years_experience):
            employee_name += ('%s - %s years, %s' % (i.name, i.years_experience, i.language) + '\n')
        return employee_name
