def letter_func(data: list):
    data = list(filter(lambda x: 'o' in x['name'].lower(), data))
    return data