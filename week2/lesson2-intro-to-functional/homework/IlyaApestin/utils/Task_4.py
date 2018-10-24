def members_o(members):
    members_o = list(filter(lambda a: 'o' in a['name'].lower(), members))
    return members_o
