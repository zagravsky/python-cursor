def sort_members(members: list):
    return sorted(members, key = lambda x: (len(x.get('name')), x.get('age')))