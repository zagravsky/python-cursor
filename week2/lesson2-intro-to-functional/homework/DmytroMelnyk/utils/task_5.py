def sum_min_max(l: list):
    """
    Write function that return three values
    :param l: input list of dict
    :return:
    - Summary age of members.
    - The youngest member
    - The oldest member
    """
    return sum(map(lambda x: x['age'], l)), min(l, key=lambda x: x['age']), max(l, key=lambda x: x['age'])


if __name__ == '__main__':
    members = [
        {'age': 43, 'name': 'Denis'},
        {'age': 49, 'name': 'Roman'},
        {'age': 36, 'name': 'Godzilla'},
        {'age': 47, 'name': 'Spike'},
        {'age': 31, 'name': 'SuperMan'},
        {'age': 49, 'name': 'Batman'},
        {'age': 37, 'name': 'Claus'},
        {'age': 55, 'name': 'Frank'},
        {'age': 83, 'name': 'Homer'}
    ]

    print(sum_min_max(members))
