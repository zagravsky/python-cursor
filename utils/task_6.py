def sort_members(members: list) -> list:
    output = sorted(members, key=lambda s: (len(s['name']), s['age']))
    return output
