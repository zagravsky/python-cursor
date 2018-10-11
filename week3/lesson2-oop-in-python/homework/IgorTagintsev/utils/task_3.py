class it_company():
    developers_list = []

    def __add__(self, developer):
        if developer.years_experience >= 3:
            self.developers_list.append(developer)
        else:
            print('Try again! You must be lucky next time!')
        return self

    def __str__(self):
        stroka = ''
        list_iz_strok = ['\n' + str(x) for x in sorted(self.developers_list, key=lambda x:x.years_experience)]
        return stroka.join(y for y in list_iz_strok)


    def firing(self, dev_name):
        for developer in self.developers_list:
            if developer.name == dev_name:
                self.developers_list.remove(developer)
                return 'Employee was fired'
        return 'Employee not found'
