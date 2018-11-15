class Developer:

    def __init__(self, years_experience: int, name: str):
        self.years_experience = years_experience
        self.name = name

    def about(self):
        if self.years_experience <= 3:
            print(f"My name is {self.name} and I am a Junior Developer.")
        elif self.years_experience <= 5:
            print(f"My name is {self.name} and I am a Middle Developer.")
        else:
            print(f"My name is {self.name} and I am a Senior Developer.")

    def write_code(self):
        print("I am a developer and I write code.")

    def __str__(self):
        return f"{self.name} - {self.years_experience}, {self.language}"

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Python'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        print("I use %s to write code." % self.language)


class JavaDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Java'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        print("I use %s to write code." % self.language)


class RubyDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Ruby'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        print("I use %s to write code." % self.language)


dev_1 = PythonDeveloper(2, 'John Connor')
dev_1.about()
dev_1.write_code()

dev_2 = JavaDeveloper(4, 'Sara Connor')
dev_2.about()
dev_2.write_code()

dev_3 = RubyDeveloper(8, 'T800')
dev_3.about()
dev_3.write_code()


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
        for i, o in enumerate(self.list_devs):
            if o.name == fire_name:
                del self.list_devs[i]
                print(f'{fire_name} has been fired.')
                return self
        else:
            return print(f'There is no developer with name {fire_name} in the company')


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

it_comp.fire('T1000')
it_comp.fire('Alfred')

print(it_comp)
