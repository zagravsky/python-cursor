from utils.task_1 import PythonDeveloper, JavaDeveloper, RubyDeveloper
from utils.task_2 import E
from utils.task_3 import company


# Task 1
python_developer = PythonDeveloper(1, "Olga Tregub")
print (vars(python_developer))
print(python_developer)
print(python_developer())
print(python_developer.about())
print(python_developer.write_code())
print("\n")

java_developer = JavaDeveloper(50, "Bill Gates")
print (vars(java_developer))
print(java_developer)
print(java_developer())
print(java_developer.about())
print(java_developer.write_code())
print("\n")

ruby_developer = RubyDeveloper(5, "Ruby Rubynovich")
print (vars(ruby_developer))
print(ruby_developer)
print(ruby_developer())
print(ruby_developer.about())
print(ruby_developer.write_code())
print("\n")

# Task 2
print(E.mro())
print("\n")

# Task 3
dev_1 = PythonDeveloper(4, "Mark Li")
dev_2 = PythonDeveloper(15, "Holly Tregy")
dev_3 = JavaDeveloper(1, "Den Petrov")
dev_4 = RubyDeveloper(13, "Simone Millenium")
dev_5 = RubyDeveloper(2, "Diana Quine")
dev_6 = JavaDeveloper(7, "Arni Malachovich")
Apple_Inc = company()

Apple_Inc += dev_1
Apple_Inc += dev_2
Apple_Inc += dev_3
Apple_Inc += dev_4
Apple_Inc += dev_5
Apple_Inc += dev_6

print(Apple_Inc)
print("\n")

print(Apple_Inc.firing("Simone Millenium"))
print(Apple_Inc)
print("\n")

print(Apple_Inc.firing("Simone Millenium"))
