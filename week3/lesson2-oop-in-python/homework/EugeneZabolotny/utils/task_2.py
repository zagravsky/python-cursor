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


if __name__ == '__main__':
    print(E.mro())
