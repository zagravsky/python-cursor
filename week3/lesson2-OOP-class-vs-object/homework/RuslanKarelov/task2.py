class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(C, A):
    pass

class E(D, B):
    pass
    