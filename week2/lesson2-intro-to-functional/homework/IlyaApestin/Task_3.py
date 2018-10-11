from Task_1 import members

print(members)

members = list(map(lambda a: {'age': a['age'] < 200,
                              'name': a['name'],
                              'load': a['age']/2},
                   members))

print(members)
