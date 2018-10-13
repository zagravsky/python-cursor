def sort_members_by_len_name(members_list: list):
    members_list.sort(key=lambda x: x['age'])
    return sorted(members_list, key=lambda x: len(x['name']))