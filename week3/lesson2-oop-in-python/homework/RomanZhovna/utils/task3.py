class Employees:

    employee_list = []

    def __add__(self, empl2add: object):
        if empl2add.years_experience >= 3:
            self.employee_list.append(empl2add)
            print(f"Employee {empl2add.name} successfully hired")
        else:
            print(f"Employee {empl2add.name} wasn't hired")
            print(f"Please, try again in {3 - empl2add.years_experience} year(s)")
        return self

    def print_employee(self):
        # sorted_employee = sorted(self.employee_list, key=lambda x: x.years_experience)
        for empl in sorted(self.employee_list, key=lambda x: x.years_experience):
            print(f"{empl.name} - {empl.years_experience} years, {empl.language}")

    def fire_employee(self, name2del: str):
        list2analize = [empl for empl in self.employee_list if empl.name == name2del]

        def fire_multi_emp():
            for empl in list2analize:
                print(f"Index: {list2analize.index(empl)}, {empl.name} - {empl.years_experience} years, {empl.language}")
            try:
                i = int(input("Choose index who should be fired:"))
                assert i in range(0, len(list2analize))
            except ValueError:
                print("You entered not an integer")
            except AssertionError:
                print("List index is out of range")
            else:
                self.employee_list.remove(list2analize[i])

        if len(list2analize) == 0:
            print(f"Employee with name - {name2del} not found")

        for empl in list2analize:
            if len(list2analize) == 1:
                self.employee_list.remove(empl)
            else:
                fire_multi_emp()
                break
