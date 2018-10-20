class Developer:

    language = ''

    def __init__(self, name, years_experience: int):
        self.years_experience = years_experience
        self.name = name

    def about(self):
        if self.years_experience <= 3:
            return 'My name is {} and I am a Junior Developer'.format(self.name)
        elif 3 < self.years_experience <= 5:
            return 'My name is {} and I am a Middle Developer'.format(self.name)
        else:
            return 'My name is {} and I am a Senior Developer'.format(self.name)

    def write_code(self):
        return 'I am developer and I write code'

    def __str__(self):
        return '{} - {} years, {}'.format(self.name, self.years_experience, self.language)

    def __call__(self):
        return self.write_code()


class PythonDeveloper(Developer):

    language = 'Python'

    def write_code(self):
        return 'I use {} to write code'.format(self.language)


class JavaDeveloper(Developer):

    language = 'Java'

    def write_code(self):
        return 'I use {} to write code'.format(self.language)


class RubyDeveloper(Developer):

    language = 'Ruby'

    def write_code(self):
        return 'I use {} to write code'.format(self.language)
