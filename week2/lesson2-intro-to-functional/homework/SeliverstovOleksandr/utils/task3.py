def load_add(members: list):

    sorted_mem=[]
    for member in members:
        if member['age'] < 200:
            sorted_mem.append({'age': member['age'], 'name': member['name'], 'load': member['age']/2})
        else:
            pass
    return (sorted_mem)

