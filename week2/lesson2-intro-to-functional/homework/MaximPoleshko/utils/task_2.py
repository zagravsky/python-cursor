def up_name(memb: list) -> list:
	for m in memb:
		m['name'] = m['name'].upper()
	return memb
