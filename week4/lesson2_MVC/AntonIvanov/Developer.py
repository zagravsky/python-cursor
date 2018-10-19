class Developer:
    def __init__(self, first_name: str, last_name:str, programming_language: str):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language


    def __call__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'
