class Developer:
    def __init__(self, years_experience, name):
        self.years_experience = years_experience
        self.name = name
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            print (f'My name is {self.name} and I am a Junior Developer.')
        elif self.years_experience <= 5:
            print (f'My name is {self.name} and I am a Middle Developer.')
        else:
            print (f'My name is {self.name} and I am a Senior Developer.')

    def write_code(self):
        print ('I am a developer and I write code')

    def __str__(self):
        return f'{self.name} - {self.years_experience} years, {self.language}'

    def __call__(self):
        return f'I use {self.language} to write code'


class PythonDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Python'

    def write_code(self):
        print (f'I use {self.language} to write code')

class JavaDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Java'

    def write_code(self):
        print(f'I use {self.language} to write code')

class RubyDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Ruby'

    def write_code(self):
        print(f'I use {self.language} to write code')

class Company():
    members_list = []

    def __add__(self, member):
        if member.years_experience >= 3:
            self.members_list.append(member)
        else:
            print(f'{member.name} doesnt have enough years experience')
        return self

    def __repr__(self):
        sotred_member_list = sorted(self.members_list, key=lambda member: member.years_experience)
        return repr([str(member) for member in sotred_member_list])

    def delete(self, key_name):
        for member in self.members_list:
            if member.name == key_name:
                self.members_list.remove(member)
                return print(f"{member.name} is fired")
        return print(f"No member with name {key_name} in compny")