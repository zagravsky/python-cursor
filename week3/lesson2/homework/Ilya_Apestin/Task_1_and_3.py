class Developer:

    def __init__(self, years_experience: int, name: str):
        self.years_experience = years_experience
        self.name = name

    def about(self):
        if self.years_experience <= 3:
            position = "Junior"
        elif self.years_experience <= 5:
            position = "Middle"
        else:
            position = "Senior"
        return f"My name is {self.name} and I am {position} Developer"

    def write_code(self):
        return "I am a developer and I write code."

    def __str__(self):
        return f"{self.name} - {self.years_experience}, {self.language}"

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Python'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return f"I use {self.language} to write code."


class JavaDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Java'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return f"I use {self.language} to write code."


class RubyDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Ruby'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return f"I use {self.language} to write code."


dev_1 = PythonDeveloper(2, 'John Connor')
print(dev_1.about())
print(dev_1.write_code())

dev_2 = JavaDeveloper(4, 'Sara Connor')
print(dev_2.about())
print(dev_2.write_code())

dev_3 = RubyDeveloper(8, 'T800')
print(dev_3.about())
print(dev_3.write_code())


class ITcompany:
    list_devs = []

    def __add__(self, new_dev):
        if new_dev.years_experience >= 3:
            self.list_devs.append(new_dev)
        else:
            print(f"{new_dev.name} does not have enough experience.")
        return self

    def __str__(self):
        view_list = ''
        for dev in sorted(self.list_devs, key=lambda a: a.years_experience):
            view_list += f'{dev.name} - {dev.years_experience} years, {dev.language}\n'
        return view_list

    def fire(self, fire_name):
        for i in self.list_devs:
            if i.name == fire_name:
                self.list_devs.remove(i)
                return f'{fire_name} has been fired.'
        else:
            return f'There is no developer with name {fire_name} in the company'


dev_4 = PythonDeveloper(18, 'T1000')
dev_5 = JavaDeveloper(28, 'Terminatrix')
dev_6 = RubyDeveloper(-6, 'Kyle Rees')

it_comp = ITcompany()

it_comp += dev_1
it_comp += dev_2
it_comp += dev_3
it_comp += dev_4
it_comp += dev_5
it_comp += dev_6

print(it_comp.fire('T1000'))
print(it_comp.fire('Alfred'))

print(it_comp)
