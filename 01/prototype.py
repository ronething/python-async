# -*- coding:utf-8 _*-

__author__ = 'ronething'

# 全局只有一个 None
a = None
b = None
# print(id(a), id(b))
assert id(a) == id(b)
