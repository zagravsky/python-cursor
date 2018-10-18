def load_add(members: list):
<<<<<<< Updated upstream

    return list(map(lambda member: {'age': member['age'], 'name': member['name'], 'load': member['age']/2} if member['age']<= 200 else '', members))
=======
    sorted_mem=[]
    for member in members:
        if member['age'] < 200:
            sorted_mem.append({'age': member['age'], 'name': member['name'], 'load': member['age']/2})
        else:
            pass
    return (sorted_mem)

#    return list(map(lambda member: {'age': member['age'], 'name': member['name'], 'load': member['age']/2} if member['age'] <=200 else '', members))
>>>>>>> Stashed changes
