def sort_list(lst: list) -> list:
	first = len(lst[0]['name'])
	for dct in lst:
		if len(dct['name']) != first:
			return sorted(lst, key=lambda x: len(x['name']))
	return sorted(lst, key=lambda x: x['age'])
