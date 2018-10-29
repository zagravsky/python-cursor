class Developer:
    def __init__(self, years_experience: int, name: str):
        self.years_experience = years_experience
        self.name = name
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            return "My name is {} and I am a Junior Developer".format(self.name)
        elif self.years_experience <= 5:
            return "My name is {} and I am a Middle Developer".format(self.name)
        else:
            return "My name is {} and I am a Senior Developer".format(self.name)

    def write_code(self):
        return "I am a developer and I write code"

    def __str__(self):
        return '%s - %s years, %s' % (self.name, self.years_experience, self.language)

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, years_experience, name, language='Python'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return "I use Python to write code"


class JavaDeveloper(Developer):
    def __init__(self, years_experience, name, language='Java'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return "I use Java to write code"


class RubyDeveloper(Developer):
    def __init__(self, years_experience, name, language='Ruby'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return "I use Ruby to write code"
