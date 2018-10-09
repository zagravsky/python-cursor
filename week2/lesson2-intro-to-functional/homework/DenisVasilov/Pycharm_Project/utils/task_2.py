def name2uppercase(list_of_members:list)-> list:
    for member in list_of_members:
        member['name']= member['name'].upper()
    return list_of_members

