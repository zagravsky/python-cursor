from Task_1 import members

print(members)

members = list(map(lambda a: {'age': a['age'],
                              'name': a['name'].upper()},
                   members))

print(members)
