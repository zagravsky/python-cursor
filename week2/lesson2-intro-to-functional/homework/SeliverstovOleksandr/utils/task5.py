def return_summary(members: list):
    return (sum([x.get('age') for x in members]),
        min(members, key=lambda x: x.get('age')),
        max(members, key=lambda x: x.get('age')))