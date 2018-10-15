def upper_name(members_list: list):
    for i in members_list:
        i["name"] = i["name"].upper()
    return members_list
