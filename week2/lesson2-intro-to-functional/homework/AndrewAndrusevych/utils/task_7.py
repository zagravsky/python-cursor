import roman
def to_roman(arab:int):
    assert 0 < arab < 5000 and int(arab) == arab, 'Number must be an integer in [1:4999]'
    return roman.toRoman(arab)

