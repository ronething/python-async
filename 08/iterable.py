# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
什么是迭代协议 __iter__
迭代器是什么 迭代器是访问集合内元素的一种方式，一般用来遍历数据

可迭代和迭代器 不一样 实现 __iter__ 可迭代 实现 __iter__ and __next__ 迭代器
"""

from collections.abc import Iterable, Iterator

a = [1, 2]
print(isinstance(a, Iterable))  # True
print(isinstance(a, Iterator))  # False
b = iter(a)
print(isinstance(b, Iterable))  # True
print(isinstance(b, Iterator))  # True
