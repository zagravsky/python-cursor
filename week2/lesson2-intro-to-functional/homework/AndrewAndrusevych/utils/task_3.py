def add_load(members_list: list):
    for member in members_list:
        member['load'] = (member['age']*100)/200
    return members_list

