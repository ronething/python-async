# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
__new__ 和 __init__ 的区别
"""


class User:
    def __new__(cls, *args, **kwargs):
        """
        用来控制对象的生成过程
        如果 new 方法不返回 则不会调用 __init__
        传入 cls 在 __init__ 之前被调用
        """
        print('in new')
        return super().__new__(cls)

    def __init__(self):
        """
        对象的实例化过程 传入 self
        """
        print('in init')