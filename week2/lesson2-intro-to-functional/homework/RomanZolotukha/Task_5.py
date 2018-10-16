def ret_func(data: list):
    age_sum = sum(diction['age'] for diction in data)
    younger_man = min(data, key=lambda x: x['age'])
    oldest_man = max(data, key=lambda x: x['age'])
    return age_sum, younger_man, oldest_man
