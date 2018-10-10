from functools import reduce


def three_values_func(members):
    new_list = list(map(lambda d: d['age'], members))
    output = list()
    output.append(reduce(lambda x, y: x + y, new_list))
    output.append(max(members, key=lambda v: list(v.values())[0]))
    output.append(min(members, key=lambda z: list(z.values())[0]))
    return output
