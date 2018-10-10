from functools import reduce

def ages(memb: list) -> list:
    return sum(map(lambda x: x['age'], memb)), min(memb, key=lambda x: x['age']), max(memb, key=lambda x: x['age'])