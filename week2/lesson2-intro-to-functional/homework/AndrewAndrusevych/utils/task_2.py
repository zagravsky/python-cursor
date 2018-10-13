def upper_name(members_list: list):
    for member in members_list:
        member['name'] = member['name'].upper()
    return members_list