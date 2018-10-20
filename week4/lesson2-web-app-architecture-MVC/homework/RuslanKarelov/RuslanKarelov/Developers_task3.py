class Developer:
    def __init__(self, first_name: str, last_name: str, programing_language: str):
        self.first_name = first_name
        self.last_name = last_name
        self.programing_language = programing_language

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.programing_language}"
