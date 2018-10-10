def uppercase_list(members: list) -> list:
    return list(map(lambda y: {'age': y['age'], 'name': y['name'].upper()}, members))
