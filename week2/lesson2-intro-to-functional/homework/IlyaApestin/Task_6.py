def sort_members(members):
    members_sorted = sorted(members, key=lambda x: (len(x['name']), x['age']))
    return members_sorted
