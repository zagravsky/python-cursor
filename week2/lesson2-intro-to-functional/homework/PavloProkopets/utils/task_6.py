def func_6(list_6: list) -> list:
	members = sorted(list_6, key=lambda x: (len(x["name"]), x['age']), reverse=True)
	return members

