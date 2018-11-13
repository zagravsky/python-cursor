def dec_to_roman(numbers):
    numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    output = ""
    if numbers > 3999:
        print("Values over 3999 are not allowed!")
    elif numbers < 0:
        print("Negative values are not allowed!")
    else:
        for value, numeral in sorted(numerals.items(), reverse=True):
            while numbers >= value:
                output += numeral
                numbers -= value
    return output
