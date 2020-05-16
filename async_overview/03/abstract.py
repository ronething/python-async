# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
抽象基类 (abc模块)
"""

# 检查某个类是否有某种方法


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['panda', 'ronething'])
print(hasattr(com, '__len__'))

# 在某些情况希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(com, Sized))

# 在某些情况需要强制某个子类必须实现某些方法

import abc


# @abc.abstractclassmethod 打上这个装饰器之后 如果子类没有覆写 get set 方法 实例化之后会报错
# TypeError: Can't instantiate abstract class RedisCache with abstract methods get, set
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get(self, key):
        pass

    @abc.abstractclassmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    pass


redis_cache = RedisCache()
print(redis_cache.get('panda'))

# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError

#     def set(self, key, value):
#         raise NotImplementedError

# class RedisCache(CacheBase):
#     def get(self, key):
#         return 'panda'

# redis_cache = RedisCache()
# print(redis_cache.get('panda'))
