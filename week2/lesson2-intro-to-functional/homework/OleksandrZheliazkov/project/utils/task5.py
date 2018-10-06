def summary(members: list):
    result = []
    result.append(sum(list(map(lambda x: x['age'], members))))
    result.append(min(members, key=lambda x: x['age']))
    result.append(max(members, key=lambda x: x['age']))
    return result

