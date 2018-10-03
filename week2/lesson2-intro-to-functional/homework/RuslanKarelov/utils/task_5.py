
def func_task5(data: list):
    list_with_data = []
    list_with_data.append(sum(list(map(lambda x: x['age'], data))))
    list_with_data.append(min(data, key=lambda x: x['age']))
    list_with_data.append(max(data, key=lambda x: x['age']))
    return list_with_data
