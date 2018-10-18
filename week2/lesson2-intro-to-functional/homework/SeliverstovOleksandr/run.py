from utils.task2 import name_uppercase
from utils.task3 import load_add
from utils.task4 import if_o
from utils.task5 import return_summary
from utils.task6 import sort_members


members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 300, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 49, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'}
]
print('Task2')
print(name_uppercase(members))
print('Task3')
print(load_add(members))
print('Task4')
print(if_o(members))
print('Task5')
print(return_summary(members))
print('Task6')
print(sort_members(members))