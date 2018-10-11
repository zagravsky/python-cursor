from task_1 import members

def three_values_func(members:list):
    age_list_members = []
    age_list_members.append(sum([i['age'] for i in members]))
    age_list_members.append(min(members, key=lambda x: 
list(x.values())[0]))
    age_list_members.append(max(members, key=lambda x: 
list(x.values())[0]))
    print(age_list_members)

three_values_func(members)
