class Developer():
    def __init__(self, years_experience: int, name: str, language=''):
        self.years_experience = years_experience
        self.name = name
        self.language = language

    def about(self):
        if self.years_experience <= 3:
            return f"My name is {self.name} and I am Junior Developer."
        elif self.years_experience <= 5:
            return f"My name is {self.name} and I am Middle Developer."
        else:
            return f"My name is {self.name} and I am a Senior Developer."

    def write_code(self):
        return "I am a developer and I write code"

    def __str__(self):
        return f"{self.name} - {self.years_experience} years, {self.language}"

    def __call__(self, *args, **kwargs):
        return self.write_code()


class Python(Developer):
    def __init__(self, years_experience, name, language='Python'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return f"I use {self.language} to write code"


class Ruby(Developer):
    def __init__(self, years_experience, name, language='Ruby'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return f"I use {self.language} to write code"


class Java(Developer):
    def __init__(self, years_experience, name, language='Java'):
        Developer.__init__(self, years_experience, name)
        self.language = language

    def write_code(self):
        return f"I use {self.language} to write code"
