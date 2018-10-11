from Task_1 import members

print(members)


def sum_yong_old_func(a: list):
    sum_age = sum(list(map(lambda x: x['age'], a)))
    yong = min(a, key=lambda x: x['age'])
    old = max(a, key=lambda x: x['age'])
    return sum_age, yong, old


print(sum_yong_old_func(members))
