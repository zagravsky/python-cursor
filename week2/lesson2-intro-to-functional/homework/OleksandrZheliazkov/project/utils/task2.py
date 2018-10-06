def case_converter(members: list):
    for i in members:
        i['name'] = i['name'].upper()
    return members