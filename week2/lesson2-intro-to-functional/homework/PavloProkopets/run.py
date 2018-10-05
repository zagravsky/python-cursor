from utils import * 

members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 47, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 49, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'}
]

print('''
*****************
Task 1
For each member make his name uppercase
*****************
''')
print(task_2.func_2(members))
print('''
*****************
Task 2
Each member will be exclude of group after reaching the age of 200 years.
Add field "load" for each member, which shows percentage of progress
*****************
''')
print(task_3.func_3(members))
print('''
*****************
Task 3
Left only those members who have letter 'o' in names.
*****************
''')
print(task_4.func_4(members))
print('''
*****************
Task 4
Write function that return three values
*****************
''')
print(task_5.func_5(members))
print('''
*****************
Task 5
Sort members by length of their names. If length of names is equal than sort by age.
*****************
''')
print(task_6.func_6(members))
