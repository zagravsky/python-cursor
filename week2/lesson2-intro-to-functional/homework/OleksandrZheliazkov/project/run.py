from utils.task1 import print_members
from utils.task2 import case_converter
from utils.task3 import members_excluder
from utils.task4 import members_remover
from utils.task5 import summary
from utils.task6 import members_sort

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

if __name__ == "__main__":
    print("\ntask1\n\n", print_members(members))
    print("\ntask2\n\n", case_converter(members))
    print("\ntask3\n\n", members_excluder(members))
    print("\ntask4\n\n", members_remover(members))
    print("\ntask5\n\n", summary(members))
    print("\ntask6\n\n", members_sort(members))
    print("\ntask7\n\n")