from utils.task_1 import func_1
from utils.task_2 import func_2
from utils.task_3 import func_3
from utils.task_4 import func_4
from utils.task_5 import func_5
from utils.task_6 import func_6
from utils.task_7 import int_to_Roman

if __name__ == '__main__':
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

print('--------------Task 1--------------', end='\n\n')
print('Print originl list', end='\n\n')
print(func_1(members), end='\n\n')
print('--------------Task 2--------------', end='\n\n')
print('For each member make his name uppercase', end='\n\n')
print(func_2(members), end='\n\n')
print('--------------Task 3--------------', end='\n\n')
print('Each member will be exclude of group after reaching the age of 200 years.\n'
      'Add field "load" for each member, which shows percentage of progress', end='\n\n')
print(func_3(members), end='\n\n')
print('--------------Task 4--------------', end='\n\n')
print("Left only those members who have letter 'o' in names.", end='\n\n')
print(func_4(members), end='\n\n')
print('--------------Task 5--------------', end='\n\n')
print('Write function that return three values:\n'
      'Summary age of members.\n'
      'The youngest member\n'
      'The oldest member.', end='\n\n')
print(func_5(members))
print('--------------Task 6--------------', end='\n\n')
print('Sort members by length of their names. If length of names is equal than sort by age.', end='\n\n')
print(func_6(members), end='\n\n')
print('--------------Task 7--------------', end='\n\n')
print('Write function that will convert decimal values to Roman Numerals', end='\n\n')
print(int_to_Roman(5), end='\n\n')
