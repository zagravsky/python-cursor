class A:
    pass

class B:
    pass

class C(B, A):
    pass

class D(C, A):
    pass

class E(D, B):
    pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
