def func_3(list_3: list) -> list:
	for x in list_3:
		if x['age'] >= 200:
			members.remove(x)
	for x in list_3:
		x['load'] = x['age']*100/200
	return list_3

# def func_2_2(list_2: list) -> list:
#    list(map(lambda x: x.update({'load': (x['age'])*100/200}), list_2))
#    return list(filter(lambda x: x['age'] < 200, list_2))
# print (func_2_2(members))
