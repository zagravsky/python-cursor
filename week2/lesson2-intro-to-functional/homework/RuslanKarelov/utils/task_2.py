def name_uppercase(data: list):
    i = 0
    while i < len(data):
        data[i]['name'] = data[i]['name'].upper()
        i += 1
    return data
