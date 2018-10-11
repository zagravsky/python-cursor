

class IT_company():
    employees = []

    def __add__(self, developer):
        if developer.years_experience >= 3: 
            self.employees.append(developer)
        else:
            print(f"Fuck off {developer.name}")
        return self
    
    def __str__(self):
        listOfEmployees = ""       
        for developer in self.employees:
            listOfEmployees += f"{developer.name} - {developer.years_experience} years, {developer.language}\n"
        return listOfEmployees

    def sorting(self):
        return self.employees.sort(key=lambda developer: developer.years_experience, reverse = True)
        
    def removeDev(self, name:str):
        # Метод removeDev видаляє працівників, але якщо буде декілька розробників із однаковим ім'я,
        #  то видалить обох. Не можу зрозуміти як правильно написати код, тому як є так є))))) 
        for developer in self.employees:
            if name is developer.name:
                self.employees.remove(developer)
        return self


