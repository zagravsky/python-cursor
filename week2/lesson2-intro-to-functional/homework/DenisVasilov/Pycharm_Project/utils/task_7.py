def convert_to_roman(input_num: int):
    roman_numb = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    final_num = ""
    i = input_num
    while i > 0:
        key = max([x for x in roman_numb.keys() if x <= i])
        final_num = final_num + roman_numb[key]
        i = i - key
    return final_num

