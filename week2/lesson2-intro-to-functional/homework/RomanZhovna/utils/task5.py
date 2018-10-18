from functools import reduce


def print_values(l: list) -> list:
    ages_list = list(map(lambda x: x['age'], l))
    summary = [reduce(lambda x, y: x+y, ages_list)]
    min_age = list(filter(lambda x: x['age'] == min(ages_list), l))
    max_age = list(filter(lambda x: x['age'] == max(ages_list), l))
    return summary + min_age + max_age
