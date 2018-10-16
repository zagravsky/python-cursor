
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

#[<class '__main__.E'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
#порядок поиска: E, D, C, B, A, object