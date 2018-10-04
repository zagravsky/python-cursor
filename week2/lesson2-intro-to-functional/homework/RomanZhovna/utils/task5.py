from functools import reduce


def print_values(l: list) -> list:
    out = [reduce(lambda x, y: x+y, list(map(lambda x: x['age'], l)))] \
          + list(filter(lambda x: x['age'] == min(list(map(lambda x: x['age'], l))), l)) \
          + list(filter(lambda x: x['age'] == max(list(map(lambda x: x['age'], l))), l))
    return out
