# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
使用 instance 而不是 type
"""


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A)) # 检查继承🔗

print(type(b) is B) # True 相当于 id(type(b)) == id(B) 因为指向的都是 B 所以结果为 True
print(type(b) is A) # False
