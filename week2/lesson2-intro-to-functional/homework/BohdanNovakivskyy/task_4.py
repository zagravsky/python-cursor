def check_o(members_list):
    new_list = list(filter(lambda x: "o" in x['name'].lower(), members_list))
    return new_list
