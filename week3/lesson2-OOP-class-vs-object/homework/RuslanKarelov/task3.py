

class ITcompany:

    employees = []

    def __add__(self, developer):
        if developer.years_experience >= 3: 
            self.employees.append(developer)
        else:
            print(f"Fuck off {developer.name}")
        return self
    
    def __str__(self):
        list_of_employees = ""
        for developer in self.employees:
            list_of_employees += f"{developer.name} - {developer.years_experience} years, {developer.language}\n"
        return list_of_employees

    def sorting(self):
        return self.employees.sort(key=lambda developer: developer.years_experience, reverse=True)
        
    def remove_dev(self, name: str):
        for developer in self.employees:
            if name is developer.name:
                self.employees.remove(developer)
                print(f"Developer {name} was removed")
                return self
        print(f"Developer not found")
        return self
