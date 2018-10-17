# Wrong gcd find 5 mistakes

def gcd(a, b):
    assert a >= 0 and b >= 0
    while a and b:
        if a > b:
            if a % b == 0:
                return b
            else:
                a = a % b
        else:
            if b % a == 0:
                return a
            else:
                b = b % a
    return a + b

print ('result: ',gcd(10, 0))
print ('result: ',gcd(123, 3))
print ('result: ',gcd(10000000, 64))
print ('result: ',gcd(0, 0))
# Examples
#gcd(10, 0) #=> 10
#gcd(123, 3) #=> 3
#gcd(1000000, 64) #=> 64
#gcd(0, 0) #=> 0
