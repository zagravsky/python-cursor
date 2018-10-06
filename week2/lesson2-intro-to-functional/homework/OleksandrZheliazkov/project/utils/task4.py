def members_remover(members: list):
    members = list(filter(lambda x: 'o' and 'O' in x['name'], members))
    return members