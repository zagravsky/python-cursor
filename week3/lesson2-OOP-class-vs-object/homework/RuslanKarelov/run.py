from task1 import*
from task2 import*
from task3 import*

# Task 1
dev = Developer("Vasyl", 6)
devPython = PythonDeveloper("Ruslan", 0)
devJava = JavaDeveloper("Tony", 10)
devRuby = RubyDeveloper("Jack", 3)

print(f"\n----------------------------------\n"
      f"Developer: {dev}\nName: {dev.name}\nExperiance: {dev.years_experience}\n"
      f"Using method .about(): {dev.about()}\nUsing method .write_code(): {dev.write_code()}\n"
      f"Using instance as function: {dev()}\n"
      f"----------------------------------")
print(f"\n----------------------------------\n"
      f"Developer: {devPython}\nName: {devPython.name}\nExperiance: {devPython.years_experience}\n"
      f"Using method .about(): {devPython.about()}\nUsing method .write_code(): {devPython.write_code()}\n"
      f"Using instance as function: {devPython()}\n"
      f"----------------------------------")
print(f"\n----------------------------------\n"
      f"Developer: {devJava}\nName: {devJava.name}\nExperiance: {devJava.years_experience}\n"
      f"Using method .about(): {devJava.about()}\nUsing method .write_code(): {devJava.write_code()}\n"
      f"Using instance as function: {devJava()}\n"
      f"----------------------------------")
print(f"\n----------------------------------\n"
      f"Developer: {devRuby}\nName: {devRuby.name}\nExperiance: {devRuby.years_experience}\n"
      f"Using method .about(): {devRuby.about()}\nUsing method .write_code(): {devRuby.write_code()}\n"
      f"Using instance as function: {devRuby()}\n"
      f"----------------------------------")

# Task 2

print(E.mro())

# Task 3

def dev_add(IT_comp, dataWithDev:list):
    for dev in dataWithDev:
        IT_comp += dev
    return IT_comp

dev1 = PythonDeveloper('Vasya', 4)
dev2 = PythonDeveloper('Tony', 6)
dev3 = PythonDeveloper('Sasha', 2)
dev4 = JavaDeveloper('Mark', 8)
dev5 = JavaDeveloper('Nestor', 1)
dev6 = JavaDeveloper('Igor', 10)
dev7 = RubyDeveloper('Vitya', 1)
dev8 = RubyDeveloper('Oleksa', 6)
dev9 = RubyDeveloper('John', 12)

company = IT_company()
dev_add(company, [dev1, dev2, dev3, dev4, dev5, dev6, dev7, dev8, dev9])
company.sorting()
company.removeDev('Vasya')
print(company)
