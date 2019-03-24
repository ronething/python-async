# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
尽量不要传可变参数 list 可以被改变 因为是指针
"""


def add(a, b):
    """
    +=背后的魔法方法是__iadd__
    +背后的魔法方法是__add__
    a = a + b 两者不同 += 直接修改本身 + 则是新声明一个 左边 a 和右边 a 无直接联系
    """
    a += b
    return a


a = 1
b = 2
c = add(a, b)
print(c)  # 3
print(a, b)  # 1 2

a = [1, 2, 3]
b = [4]

c = add(a, b)
print(c)  # [1, 2, 3, 4]
print(a, b)  # [1, 2, 3, 4] [4]
