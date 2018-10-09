def load_add(members: list):
    return list(map(lambda member: {'age': member['age'], 'name': member['name'], 'load': member['age']/2}, members))