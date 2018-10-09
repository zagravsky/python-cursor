def age_loading (lst_of_members:list) -> list:
    lst_of_members=list(filter(lambda i:i['age']<=200,lst_of_members))
    for load in lst_of_members:
        load['loading']= load['age']*100/200
    return lst_of_members

