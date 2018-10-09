
def if_o(members: list):
    return list(filter(lambda member: member if 'o' in member['name'] else '', members))