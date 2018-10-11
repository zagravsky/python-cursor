class Developer():
    def __init__(self, name, exp):
        self.language = ''
        self.name = name
        self.years_experience = exp

    def about(self):
        if self.years_experience <= 3:
            print('My name is {name} and I am Junior Developer'.format(name=self.name))
        elif self.years_experience <= 5:
            print('My name is {name} and I am Middle Developer'.format(name=self.name))
        else:
            print('My name is {name} and I am Senior Developer'.format(name=self.name))

    def write_code(self):
        print('I am a developer and I write code')

    def __str__(self):
        return '{name}-{years_experience} years exp., {language}'.format(name=self.name,years_experience=self.years_experience,
                                                                    language=self.language)
    def __repr__(self):
        return '{name}-{years_experience} years exp., {language}'.format(name=self.name,
                                                                         years_experience=self.years_experience,
                                                                         language=self.language)
class JavaDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Java'

    def write_code(self):
        print('I use {language} to write code'.format(language=self.language))


class RubyDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Ruby'

    def write_code(self):
        print('I use {language} to write code'.format(language=self.language))


class PythonDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Python'

    def write_code(self):
        print('I use {language} to write code'.format(language=self.language))

if __name__ == "__main__":
    pyDev = PythonDeveloper('Viktor', 1)
    jaDev = JavaDeveloper('Nikolay', 3)
    ruDev = RubyDeveloper('Vasiliy', 5)

    pyDev.about()
    pyDev.write_code()
    print(pyDev)
    print("------")
    jaDev.about()
    jaDev.write_code()
    print(jaDev)
    print("------")
    ruDev.about()
    ruDev.write_code()
    print(ruDev)