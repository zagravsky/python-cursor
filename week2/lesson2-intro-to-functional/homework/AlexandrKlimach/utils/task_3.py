def find_letter(lst: list) -> list:
	new_lst = []
	for dct in lst:
		if 'o' in dct['name'].lower():
			new_lst.append(dct)
	return new_lst