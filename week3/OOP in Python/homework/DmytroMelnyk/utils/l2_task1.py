class Developer:
    def __init__(self, years_experience: int, name: str):
        self.years_experience = years_experience
        self.name = name
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            print(f"My name is {self.name} and I am a Junior Developer.")
        elif self.years_experience <= 5:
            print(f"My name is {self.name} and I am a Middle Developer.")
        else:
            print(f"My name is {self.name} and I am a Senior Developer.")

    def write_code(self):
        return print("I am a developer and I write code")

    def __str__(self):
        return f'{self.name} - {self.years_experience} years, {self.language}'

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Python'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return print(f"I use {self.language} to write code")


class JavaDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Java'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return print(f"I use {self.language} to write code")


class RubyDeveloper(Developer):
    def __init__(self, years_experience: int, name: str, language='Ruby'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return print(f"I use {self.language} to write code")


if __name__=='__main__':
    print('Task_1.3')
    a = Developer(2, "John")
    a.about()
    a.write_code()
    print('\n')
    b = Developer(5, "Mukhamed")
    b.about()
    b.write_code()
    print('\n')
    c = Developer(7, "Silvester")
    c.about()
    c.write_code()
    print('\n')
    d = PythonDeveloper(7, 'Arnold')
    d.about()
    d.write_code()
    print('\n')
    e = JavaDeveloper(2, 'Adolf')
    e.about()
    e.write_code()
    print('\n')
    f = RubyDeveloper(5, 'Adolf')
    f.about()
    f.write_code()
    print('\n')

    print('Task_1.4')
    g = Developer(7, 'Roman')
    print(g)
    h = PythonDeveloper(7, 'Roman')
    print(h)
    i = JavaDeveloper(7, 'Roman')
    print(i)
    j = RubyDeveloper(7, 'Roman')
    print(j)
    print('\n')

    print('Task_1.5')
    developer = PythonDeveloper(5, 'Anton')
    developer()
    developerR = RubyDeveloper(5, 'Anton')
    developerR()