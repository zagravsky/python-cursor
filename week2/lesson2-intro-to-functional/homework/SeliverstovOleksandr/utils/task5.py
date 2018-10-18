def return_summary(members: list):
    sum_of_ages = sum([x.get('age') for x in members])
    min_age = min(members, key=lambda x: x.get('age'))
    max_age = max(members, key=lambda x: x.get('age'))

    return (sum_of_ages, min_age, max_age)