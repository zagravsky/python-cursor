
class ItCompany:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.developers_list = []

    def __add__(self, developer):
        if developer.years_experience >= 3:
            print(f"{developer.name} has enough years of experience. Hired to the IT company '{self.company_name}'!!!", end='\n\n')
            self.developers_list.append(developer)
        else:
            print(f"Sorry {developer.name}. We need at least dev with 3 years of experience!!!")
        return self

    def __str__(self):
        printing = ''
        sorted_dev_list = ['\n' + str(x) for x in sorted(self.developers_list, key=lambda x: x.years_experience)]
        return printing.join(i for i in sorted_dev_list)

    def firing_dev(self, dev_name: str):
        for dev in self.developers_list:
            if dev.name == dev_name:
                self.developers_list.remove(dev)
                print(f"Developer {dev.name} was fired from the IT company '{self.company_name}'!!!")
                return self
            else:
                print(f"Developer was not found in the IT company '{self.company_name}'. Please check!!!")
                return self
