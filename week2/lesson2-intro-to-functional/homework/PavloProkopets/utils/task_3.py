def func_3(list_3: list) -> list:
	for x in list_3:
		x['load']=x['age']*100/200
		if x['age']>=200:
			list_3.remove(x)
	return list_3

