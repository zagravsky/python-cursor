def func_5(list_5: list) -> tuple:
    sum_m = sum(x['age'] for x in list_5)
    min_m = min(list_5, key=lambda x: x['age'])
    max_m = max(list_5, key=lambda x: x['age'])
    return sum_m, min_m, max_m

# def func_4_2(list_4: list) -> tuple:
#     age_sum = reduce(lambda x, y: x + y, [x['age'] for x in list_4])
#     age_min = reduce(lambda x, y: x if x['age'] < y['age'] else y, list_4)
#     age_max = reduce(lambda x, y: x if x['age'] > y['age'] else y, list_4)
#     return age_sum, age_min, age_max
