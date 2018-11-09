class Developer:

    language = ''

    def __init__(self, name, years_experience: int):
        self.years_experience = years_experience
        self.name = name

    def about(self):
	level = 'Senior'
        if self.years_experience <= 3:
	    level = 'Junior'            
        elif 3 < self.years_experience <= 5:
            level = 'Middle'
        return 'My name is {} and I am a {} Developer'.format(self.name, level)

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
