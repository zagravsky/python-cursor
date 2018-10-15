def get_summery_age_youngest_and_oldest_member(members: list):
    return sum([member['age'] for member in members]), min(members, key=lambda x: x['age']), max(members, key=lambda x: x['age'])

