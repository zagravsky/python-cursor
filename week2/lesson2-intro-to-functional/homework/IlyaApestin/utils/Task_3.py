def load_und_200(members):
    members_load = list(filter(lambda x: x['age'] < 200,
                               members))
    members_load = list(map(lambda a: {'age': a['age'],
                              'name': a['name'],
                              'load': a['age']/2},
                            members_load))
    return members_load
