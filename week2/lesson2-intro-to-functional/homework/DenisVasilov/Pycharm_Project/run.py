from utils.task_2 import name2uppercase
from utils.task_3 import age_loading
from utils.task_4 import o_include
from utils.task_5 import task_5_function
from utils.task_6 import func_task_6
from utils.task_7 import convert_to_roman
members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 47, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 49, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'}]

if __name__ == "__main__":
    print(members)
    print(name2uppercase(members))
    print(age_loading(members))
    print(o_include(members))
    print(task_5_function(members))
    print(func_task_6(members))
    print(convert_to_roman(9))

