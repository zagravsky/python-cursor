print('Task_1')
members_1 = [
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

print('Task_2')

print(members_1)

members_2 = list(map(lambda a: {'age': a['age'],
                                'name': a['name'].upper()},
                     members_1))

print(members_2)

print('Task_3')

members_3 = list(map(lambda a: {'age': a['age'],
                                'name': a['name'],
                                'load': a['age']/2}, members_1))

print(members_3)

print('Task_4')

members_4 = list(filter(lambda a: 'o' in a['name'], members_1))

print(members_4)

print('Task_5')


def sum_yong_old_func(a: list):
    sum_age = sum(list(map(lambda x: x['age'], a)))
    yong = min(a, key=lambda x: x['age'])
    old = max(a, key=lambda x: x['age'])
    return sum_age, yong, old


print(sum_yong_old_func(members_1))

print('Task_6')

members_6 = sorted(sorted(members_1,
                          key=(lambda x: x['name'])),
                   key=(lambda x: x['age']))

print(members_6)

print('Task_7')


def arab_to_rom(number):
    roman_arab_dict = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    roman_numerals = ''
    for numeral, value in roman_arab_dict:
        while value <= number:
            number -= value
            roman_numerals += numeral
    return roman_numerals


print('Examples: ')
print(arab_to_rom(121))
print(arab_to_rom(3555))
print(arab_to_rom(499))
