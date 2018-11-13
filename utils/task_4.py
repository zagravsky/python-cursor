def names_with_o_letter(members: list) -> list:
    return list(filter(lambda b: 'o' in b['name'].lower(), members))
