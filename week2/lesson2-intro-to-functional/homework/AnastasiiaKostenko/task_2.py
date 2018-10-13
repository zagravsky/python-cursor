from task_1 import members

def upper_name_in_dict(members:list):
    for name in members:
        name['name'] = name['name'].upper()
    return members

print(upper_name_in_dict(members))

