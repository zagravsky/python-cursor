from functools import reduce


def three_values_func(members):
    new_list = list(map(lambda d: d['age'], members))
    summary = reduce(lambda x, y: x + y, new_list)
    youngest = min(members, key=lambda z:  z['age'])
    oldest = max(members, key=lambda v: v['age'])
    return summary, youngest, oldest
