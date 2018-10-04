# this is "simple" convertor for arabic to roman conversion and numbers from initial_map are enough only for arabic numbers up to 3999.
def arabic2roman(i: int) -> str:
    assert 0 < i <= 3999 and int(i)
    initial_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    roman = ''
    while i > 0:
        for n, r in initial_map:
            while i >= n:
                roman += r
                i -= n
    return roman
