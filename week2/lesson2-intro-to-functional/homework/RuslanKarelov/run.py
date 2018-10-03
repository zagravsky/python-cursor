from utils.task_2 import name_uppercase
from utils.task_3 import func_task3
from utils.task_4 import filter_data
from utils.task_5 import func_task5
from utils.task_6 import sorted_by_names
from utils.task_7 import convert_number
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
# Task 2
print(f"Task 2\n\n {name_uppercase(members)}")
print("\n")
# Task 3
print(f"Task 3\n\n {func_task3(members)}")
print("\n")
# Task 4
print(f"Task 4 \n\n {filter_data(members)}")
print("\n")
# Task 5
print(f"Task 5\n\n {func_task5(members)}")
print("\n")
# Task 6
print(f"Task 6\n\n {sorted_by_names(members)}")
print("\n")
# Task 7 Advaced
print(f"Task 7\n\n {convert_number(34)}")
