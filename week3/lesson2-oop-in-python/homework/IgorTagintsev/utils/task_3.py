class it_company():
    dev_list = []

    def __add__(self, other):
        if other.years_experience >= 3:
            self.dev_list.append(other)
        else:
            print('Try later!')
        return self

    def __str__(self):
        string = ''
        list_string_sort = ['\n' + str(x) for x in sorted(self.dev_list, key=lambda x: x.years_experience)]
        return string.join(list_string_sort)

    def __len__(self):
        return len(self.dev_list)

    def firing(self, dev_name):
        for dev in self.dev_list:
            if dev.name == dev_name:
                self.dev_list.remove(dev)
                return print('Employee was fired')
        return print('No such employee found')
