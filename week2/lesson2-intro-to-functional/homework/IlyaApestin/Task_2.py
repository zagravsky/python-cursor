def upper_name(members):
    members_upper = list(map(lambda a: {'age': a['age'],
                                  'name': a['name'].upper()},
                       members))
    return members_upper
