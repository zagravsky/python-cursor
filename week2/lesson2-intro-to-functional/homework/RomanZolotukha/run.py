from Task_1 import members as memb
from Task_2 import uppercase_func
from Task_3 import years_func
from Task_4 import letter_func
from Task_5 import ret_func
from Task_6 import sort_func

import copy
"""
First task import a list members
"""
members = copy.deepcopy(memb)
print("Task 1:")
print(members)

"""
For each member make his name uppercase
"""
members = copy.deepcopy(memb)
print("Task 2:")
print(f"{uppercase_func(members)}")
"""
Each member will be exclude of group after reaching the age of 200 years.
"""
members = copy.deepcopy(memb)
print("Task 3:")
print(f"{years_func(members)}")
"""
Left only those members who have letter 'o' in names.
"""
members = copy.deepcopy(memb)
print("Task 4:")
print(f"{letter_func(members)}")
"""
Write function that return three values
"""
members = copy.deepcopy(memb)
print("Task 5:")
print(f"{ret_func(members)}")
"""
Sort members by length of their names. If length of names is equal than sort by age.
"""
members = copy.deepcopy(memb)
print("Task 6:")
print(f"{sort_func(members)}")

