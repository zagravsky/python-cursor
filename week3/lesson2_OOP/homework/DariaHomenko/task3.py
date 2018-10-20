class IT_Company:

    list_of_members = []

    def __add__(self, member):
        if member.years_experience < 3:
            print('{} experience is not enough.'.format(member.name))
        self.list_of_members.append(member)
        return self

    def __sub__(self, member):
        try:
            self.list_of_members.remove(member)
            print('{}: fired'.format(member.name))
            return self
        except ValueError:
            print('{}: Name not found'.format(member.name))
            return self

    def company_employee(self):
        print('List employees of the company: ', end='\n')
        self.list_of_members.sort(key=lambda member_years: member_years.years_experience)
        for member in self.list_of_members:
            print(member)



