def members_excluder(members: list):
    for x in members:
        x['load'] = x['age'] * 100 / 200
        if x['age'] >= 200:
            members.remove(x)
    return members