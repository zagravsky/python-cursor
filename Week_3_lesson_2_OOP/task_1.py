class Developer:

    def __init__(self, years_experience, name):
        self.years_experience = years_experience
        self.name = name
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            print("My name is %s and I am a Junior Developer." % (self.name))
        elif self.years_experience <= 5:
            print("My name is %s and I am a Middle Developer." % (self.name))
        else:
            print("My name is %s and I am a Senior Developer." % (self.name))

    def write_code(self):
        return "I am a developer and I write code"

    def __str__(self):
        return '%s - %s years, %s ' % (self.name, self.years_experience, self.language)

    def __call__(self):
        print(f"I use {self.language} to write code")

class PythonDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Python'

    def write_code(self):
        return "I use %s to write code" % (self.language)


class JavaDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Java'

    def write_code(self):
        return "I use %s to write code" % (self.language)

class RubyDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Ruby'

    def write_code(self):
        return "I use %s to write code" % (self.language)



