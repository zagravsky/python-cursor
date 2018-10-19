def name_upper(members_list: list):
    for member_name in members_list:
        member_name["name"] = member_name["name"].upper()
    return members_list
