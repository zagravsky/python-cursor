def sort_members(member_list: list):
    return sorted(sorted(member_list, key=(lambda member_item: member_item['age'])),
                  key=(lambda member_item: len(member_item['name'])))
