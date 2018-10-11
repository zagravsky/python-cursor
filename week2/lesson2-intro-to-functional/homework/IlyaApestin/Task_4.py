from Task_1 import members

print(members)

members = list(filter(lambda a: 'o' in a['name'], members))

print(members)
