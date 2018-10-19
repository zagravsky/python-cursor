def upto200_load (members_list: list):
    for member_age in members_list:
        current_index = members_list.index(member_age)
        if member_age["age"] >= 200:
            members_list.pop(members_list.index(member_age))
    list(map(lambda member_par: member_par.update({'load': (member_par['age'])/2}) ,members_list))
    return members_list

