def sort_func(data: list):
    data = sorted(data, key=lambda x: (len(x['name']), x['age']))
    return data