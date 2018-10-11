from Task_1 import members

print(members)

members = sorted(sorted(members,
                        key=(lambda x: x['name'])),
                 key=(lambda x: x['age']))

print(members)
