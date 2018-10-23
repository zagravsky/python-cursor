class company:
    develop_list = []

    def __add__(self, dev):
        if dev.years_experience >= 3:
            self.develop_list.append(dev)
        else:
            print ("{name}, your experience - {years_experience} years is not enough!".format(name=dev.name,
                                                                      years_experience=dev.years_experience))
        return self


    def __str__(self):
        string = ""
        list_string = ["\n" + str(x) for x in sorted(self.develop_list, key=lambda x: x.years_experience)]
        return string.join(list_string)


    def firing(self, dev_name):
        for dev in self.develop_list:
            if dev.name == dev_name:
                self.develop_list.remove(dev)
                return "Employee {dev_name} was fired!".format(dev_name=dev.name)
        return "No such employee found."
