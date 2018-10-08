def members_with_o(members_list: list):
    return list(filter(lambda member_item: member_item if 'o' in member_item['name'] else '', members_list))

