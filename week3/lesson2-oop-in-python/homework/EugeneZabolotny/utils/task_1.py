class Developer:
    def __init__(self, name, years_experience):
        self.name: str = name
        self.years_experience: int = years_experience
        self.language: str = ''

    def about(self):
        if self.years_experience <= 3:
            return "My name is {name} and I am a Junior Developer.".format(name=self.name)
        elif self.years_experience <= 5:
            return "My name is {name} and I am a Middle Developer.".format(name=self.name)
        else:
            return "My name is {name} and I am a Senior Developer.".format(name=self.name)

    def write_code(self):
        return "I am a developer and I write code."

    def __str__(self):
        return "{name} - {years_experience} years, {language}.".format(**self.__dict__)

    def __call__(self, *args, **kwargs):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Python'

    def write_code(self):
        return "I use {language} to write code.".format(language=self.language)


class JavaDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Java'

    def write_code(self):
        return "I use {language} to write code.".format(language=self.language)


class RubyDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Ruby'

    def write_code(self):
        return "I use {language} to write code.".format(language=self.language)


if __name__ == '__main__':
    py = PythonDeveloper('Pythonista', 8)
    ja = JavaDeveloper('Javista', 5)
    rb = RubyDeveloper('Rubyista', 2)

    print(vars(py),   py.about(),   py.write_code(),   py,  py(),  sep='\n', end='\n\n')
    print(vars(ja),   ja.about(),   ja.write_code(),   ja,  ja(),  sep='\n', end='\n\n')
    print(vars(rb),   rb.about(),   rb.write_code(),   rb,  rb(),  sep='\n', end='\n\n')
