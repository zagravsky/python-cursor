from functools import reduce
def func_5(list_5: list) -> tuple:
	age_sum = reduce(lambda x, y: x + y, [x['age'] for x in list_5])
	age_max = reduce(lambda x, y: x if x['age'] > y['age'] else y, list_5)
	age_min = reduce(lambda x, y: x if x['age'] < y['age'] else y, list_5)
	return age_sum, age_max, age_min
