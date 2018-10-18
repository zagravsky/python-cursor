
def if_o(members: list):
    return list(filter(lambda member:'o' in member['name'].lower(), members))