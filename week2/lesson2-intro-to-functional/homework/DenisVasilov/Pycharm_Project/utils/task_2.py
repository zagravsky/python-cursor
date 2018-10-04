def name2uppercase(list_of_members:list):
    i = 0
    while i < len(list_of_members):
        list_of_members[i]['name']=list_of_members[i]['name'].upper()
        i+=1
    return list_of_members

