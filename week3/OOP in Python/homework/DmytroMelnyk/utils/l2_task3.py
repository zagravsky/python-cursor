class ITCompany:
    _it_comp_arr = []

    def __add__(self, other):
        if other.years_experience >= 3:
            self._it_comp_arr.append(other)
        else:
            print('You have not necessary experience for this job!')
        return self

    def __str__(self):
        str_to_print = ''
        list_str_to_print = ['\n' + str(x) for x in sorted(self._it_comp_arr, key=lambda x: x.years_experience)]
        return str_to_print.join(i for i in list_str_to_print)

    def fire_employee(self, name_employee):
        count = len(list(filter(lambda x: x.name == name_employee, self._it_comp_arr)))
        if count > 1:
            list_fire_candidats = list(filter(lambda x: x.name == name_employee, self._it_comp_arr))
            print(f'There are some candidats for fire with name {name_employee}:')
            for n, candidats in enumerate(list_fire_candidats, start=1):
                print(n, candidats)
            ask = input('Who will be fire?(type number):')
            self._it_comp_arr.remove(list_fire_candidats[int(ask) - 1])
            print(f'Employee {list_fire_candidats[int(ask)-1]} - is fired!')
        elif count == 1:
            # self._it_comp_arr.remove(list(filter(lambda x: x.name == name_employee, self._it_comp_arr))[0])
            for emp in self._it_comp_arr:
                if emp.name == name_employee:
                    self._it_comp_arr.remove(emp)
                    print(f'Employee {name_employee} - is fired!')
        else:
            print(f'There is no employee {name_employee} in our company')
        return self._it_comp_arr


if __name__ == '__main__':
    from l2_task1 import Developer, PythonDeveloper, JavaDeveloper, RubyDeveloper
    newemp = JavaDeveloper(1, 'Pavlo')
    newemp1 = RubyDeveloper(3, 'Pashko')
    newemp2 = PythonDeveloper(10, 'Boris')
    newemp3 = Developer(7, 'Adolf')
    newemp4 = RubyDeveloper(7, 'Den')
    newemp5 = PythonDeveloper(4, 'Den')
    itcomp = ITCompany()
    itcomp += newemp
    itcomp += newemp1
    itcomp += newemp2
    itcomp += newemp3
    itcomp += newemp4
    itcomp += newemp5
    itcomp.fire_employee('Den')
    print(itcomp)
