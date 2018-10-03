def load_progress(lst: list) -> list:
	for dct in lst:
		if dct['age'] >= 200:
			lst.remove(dct)
			continue
		dct['load'] = 100 * dct['age'] / 200
	return lst