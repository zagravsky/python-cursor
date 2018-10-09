def o_include (lst_of_members:list) -> list:
    return list(filter(lambda x: 'o' in x['name'].lower(), lst_of_members))


