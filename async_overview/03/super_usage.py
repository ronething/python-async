# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
为什么要调用 super
super 的执行顺序？ 不是执行父类的方法 而是根据 __mro__
"""


class A:
    def __init__(self):
        print('A')
        super().__init__()


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C:
    def __init__(self):
        print('C')
        super().__init__()


class D(C):
    def __init__(self):
        print('D')
        super().__init__()


class E(B, D):
    def __init__(self):
        print('E')
        super().__init__()


if __name__ == "__main__":
    print(E.__mro__)
    e = E()