def age_loading (lst_of_members:list):
    lst_of_members=list(filter(lambda i:i['age']<=200,lst_of_members))
    for j in range (len(lst_of_members)):
        lst_of_members[j]['loading']= lst_of_members[j]['age']*100/200
    return lst_of_members

