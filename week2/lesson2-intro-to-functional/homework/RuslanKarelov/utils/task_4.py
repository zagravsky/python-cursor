def filter_data(data: list):
    from re import search
    data = list(filter(lambda x: search(r'o', x['name'].lower()), data))
    return data
