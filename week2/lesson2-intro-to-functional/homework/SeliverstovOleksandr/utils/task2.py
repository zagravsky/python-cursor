
def name_uppercase(members: list):
    return list(map(lambda members: {'age': members['age'], 'name': members['name'].upper()}, members))

