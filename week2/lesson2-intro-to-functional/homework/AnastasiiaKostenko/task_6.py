from task_1 import members

def sorted_members(members:list):
    sorted_members_list = sorted(members, key=lambda x: (len(x['name']), 
x['age']))
    return sorted_members_list

print(sorted_members(members))
