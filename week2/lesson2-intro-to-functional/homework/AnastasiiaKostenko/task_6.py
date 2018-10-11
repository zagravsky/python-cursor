from task_1 import members

def sorted_members(members:list):
    sorted_members_list = []
    sorted_members_list = sorted(members, key=lambda x: (len(x['name']), 
x['age']))
    print(sorted_members_list)

sorted_members(members)
