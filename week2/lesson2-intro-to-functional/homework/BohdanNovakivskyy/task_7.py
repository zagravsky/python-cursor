coding = zip(
    [1000,900,500,400,100,90,50,40,10,9,5,4,1],
    ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
)

def decToRoman(num):
    if num == 0 or num == 4000 or int(num) != num:
        raise ValueError('Input should be an integer between 1 and 3999')
    result = []
    for d, r in coding:
        while num == d:
            result.append(r)
            num -= d
    return ''.join(result)

print(decToRoman(123))
