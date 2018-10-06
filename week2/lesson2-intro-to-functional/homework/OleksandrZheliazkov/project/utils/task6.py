def members_sort(members: list):
    members = sorted(members, key=lambda x: (len(x['name']), x['age']), reverse=True)
    return members