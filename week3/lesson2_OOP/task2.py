class A:
    None


class B:
    None


class C(B, A):
    None


class D(C, A):
    None


class E(D, B):
    None


if __name__ == '__main':
    E.mro()


print(E.mro())