import copy as c
from task_1 import members
from task_2 import name_upper
from task_3 import upto200_load
from task_4 import check_o
from task_5 import sum_young_old
from task_6 import sort_list

members_2 = c.deepcopy(members)
members_3 = c.deepcopy(members)
members_4 = c.deepcopy(members)
members_5 = c.deepcopy(members)
members_6 = c.deepcopy(members)

print("Task-1")
print(members)

print("Task-2")
print(name_upper(members_2))

print("Task-3")
print(upto200_load(members_3))

print("Task-4")
print(check_o(members_4))

print("Task-5")
print(sum_young_old(members_5))

print("Task-6")
print(sort_list(members_6))
