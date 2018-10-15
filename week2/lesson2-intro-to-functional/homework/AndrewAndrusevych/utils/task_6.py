def sort_members_by_len_name(members_list: list):
    return sorted(members_list, key=lambda k: (len(k['name']), k['age']))

