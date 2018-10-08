def sum_max_min_members(members_list: list):
    list_of_sum_min_max = [sum(list(map(lambda member_item: list(member_item.values())[0], members_list))),
                           min(members_list, key=(lambda member_item: member_item['age'])),
                           max(members_list, key=(lambda member_item: member_item['age']))
                           ]

    return list_of_sum_min_max
