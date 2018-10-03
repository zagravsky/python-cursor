def sorted_by_names(data: list):
    from re import findall
    data = sorted(data, key=lambda x: (len(findall(r'.', x['name'])), x['age']))
    return data
