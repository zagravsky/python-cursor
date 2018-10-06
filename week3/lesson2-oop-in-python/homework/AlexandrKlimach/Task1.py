class Developer:
    def __init__(self, name, years_experience):
        self.name = name
        self.years_experience = years_experience
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            print('My name is {name} and I am a Junior Developer'.format(name=self.name))
        elif self.years_experience <= 5:
            print('My name is {name} and I am a Middle Developer'.format(name=self.name))
        else:
            print('My name is {name} and I am a Senior Developer'.format(name=self.name))

    def write_code(self):
        print('I am a developer and I write code')

    def __str__(self):
        return '{name} - {years_experience} years, {language}'.format(name=self.name,
                                                                      years_experience=self.years_experience,
                                                                      language=self.language)

    def __call__(self):
        return 'I use Python to write code'


class PythonDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Python'

    def write_code(self):
        print('I use {language} to write code'.format(language=self.language))


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


if __name__ == "__main__":
    pDev = PythonDeveloper('Alexandr', 5)
    jDev = JavaDeveloper('Konstantin', 2)
    rDev = RubyDeveloper('Boris', 8)

    pDev.about()
    pDev.write_code()
    print(pDev)

    jDev.about()
    jDev.write_code()
    print(jDev)

    rDev.about()
    rDev.write_code()
    print(rDev)
