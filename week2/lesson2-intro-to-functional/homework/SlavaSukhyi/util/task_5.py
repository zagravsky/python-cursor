def count_ages(members):
    sum_ages = sum([0 + int(age["age"]) for age in members])
    max_age = max(members, key=lambda x: list(x.values())[0])
    min_age = min(members, key=lambda x: list(x.values())[0])
    return f"({sum_ages}, {max_age}, {min_age})"
