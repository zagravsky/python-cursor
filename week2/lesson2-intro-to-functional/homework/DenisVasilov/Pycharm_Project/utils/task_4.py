def o_include (lst_of_members:list):
    from re import search
    lst_of_members=list(filter(lambda i: search(r'o', i['name'].lower()), lst_of_members))
    return lst_of_members

