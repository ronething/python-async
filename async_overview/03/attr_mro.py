# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
MRO 算法
类属性和实例属性

深度优先 DFS
广度优先 BFS

C3 算法
"""
"""
A->B,C 
B,C->D
"""

# 新式类
# class D:
#     pass

# class C(D):
#     pass

# class B(D):
#     pass

# class A(B, C):
#     pass

# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
# print(A.__mro__)


class D:
    pass


class E:
    pass


class B(D):
    pass


class C(E):
    pass


class A(B, C):
    pass


# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
print(A.__mro__)
