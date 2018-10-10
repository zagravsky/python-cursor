def add_field_load(members: list) -> list:
    list(map(lambda x: x.update({'load': (x['age']) / 2}), members))
    return list(filter((lambda a: a['age'] < 200), members))

