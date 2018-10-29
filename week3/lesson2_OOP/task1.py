class Developer:
    def __init__(self, name: str, years_experience: int):
        self.years_experience = years_experience
        self.name = name
        self.language = ""

    def about(self):
        if self.years_experience <= 3:
            print("My name is {name} and I am a Junior Developer.".format(name = self.name))
        elif self.years_experience <= 5:
            print("My name is {name} and I am a Middle Developer.".format(name=self.name))
        else:
            print("My name is {name} and I am a Senior Developer.".format(name=self.name))

    def write_code(self):
        print("I am a developer and I write code")

    def __str__(self):
        return '{name} - {years_experience} years, {language} '.format(name=self.name, years_experience=self.years_experience, language=self.language)

    def __call__(self):
        print("I use Python to write code")

class PythonDeveloper(Developer):
    def __init__(self, name: str, years_experience: int):
        Developer.__init__(self, name, years_experience)
        self.language = 'Python'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))


class JavaDeveloper(Developer):
    def __init__(self, name: str, years_experience: int):
        Developer.__init__(self, name, years_experience)
        self.language = 'Java'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))


class RubyDeveloper(Developer):
    def __init__(self, name: str, years_experience: int):
        Developer.__init__(self, name, years_experience)
        self.language = 'Ruby'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))


if __name__ == '__main__':
    dev_python = PythonDeveloper('Gusev', 5)
    dev_java = JavaDeveloper('Rebrov', 2)
    dev_ruby = RubyDeveloper('Sheva', 7)

    dev_java.about()
    dev_java.write_code()
    print(dev_java)

    dev_ruby.about()
    dev_ruby.write_code()
    print(dev_ruby)

    dev_python.about()
    dev_python.write_code()
    print(dev_python)

