def sort_list(members_list):
    return sorted(members_list, key=lambda t: (t['age'], t['name']))

