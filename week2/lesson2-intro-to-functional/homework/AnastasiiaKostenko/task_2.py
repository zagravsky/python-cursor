from task_1 import members

def upper_name_in_dict(members:list):
    for name in members:
        name['name'] = name['name'].upper()
    print(type(members))
    print(members)

upper_name_in_dict(members)

