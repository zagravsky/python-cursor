class Developer:
    def __init__(self, name, years_experience):
        self.name = str(name)
        self.years_experience = int(years_experience)
        self.language = None

    def about(self):
        if self.years_experience <= 3:
            return f"My name is {self.name} and I am a Junior Developer" 
        elif self.years_experience <= 5:
            return f"My name is {self.name} and I am a Middle Developer"
        else:
            return f"My name is {self.name} and I am a Senior Developer"

    def write_code(self):
        return "I am a developer and I write code"

    def __str__(self):
        return f"{self.name} - {self.years_experience} years, {self.language}"

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Python'

    def write_code(self):
        return f"I use {self.language} to write code"


class JavaDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Java'

    def write_code(self):
        return f"I use {self.language} to write code"


class RubyDeveloper(Developer):
    def __init__(self, name, years_experience):
        Developer.__init__(self, name, years_experience)
        self.language = 'Ruby'

    def write_code(self):
        return f"I use {self.language} to write code"

