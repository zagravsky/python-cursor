def func_2(list_2: list) -> list:
    for x in list_2:
        x['name'] = x['name'].upper()
    return list_2

# def func_1_2(members: list) -> list:
#     return list(map(lambda x: {'age': x['age'], 'name': x['name'].upper()}, members))
# print (func_1_2(members))
