# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
不建议继承 dict 因为 dict 使用 c 语言编写 有时候会有一些意想不到的问题发生
可以继承 UserDict
"""

from collections import UserDict


class MyDict(UserDict):
    def __setitem__(self, k, v):
        super().__setitem__(k, v * 2)


a = MyDict(one=1)
print(a)  # {'one': 2}
