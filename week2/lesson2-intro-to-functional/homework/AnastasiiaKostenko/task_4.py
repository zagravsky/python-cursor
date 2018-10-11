from task_1 import members

def left_members(members:list):
    new_members = [i for i in members if "o" in i['name']]
    print(new_members)

left_members(members)
