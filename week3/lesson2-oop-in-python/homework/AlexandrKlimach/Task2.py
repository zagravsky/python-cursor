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


if __name__ == "__main__":
    print(E.mro())

# E.mro()
# [<class 'Task2.E'>, <class 'Task2.D'>, <class 'Task2.C'>, <class 'Task2.B'>, <class 'Task2.A'>, <class 'object'>]
