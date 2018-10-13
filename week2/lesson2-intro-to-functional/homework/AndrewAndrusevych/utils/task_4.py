def get_member_with_symbol_in_name (members_list: list, symbol:str):
    new_member_list = []
    for member in members_list:
        if  member['name'].find(symbol) != -1:
            new_member_list.append(member)
    return new_member_list