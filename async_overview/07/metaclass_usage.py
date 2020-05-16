# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
什么是元类 元类是创建类的类 type 就是元类 对象<-class(对象)<-type

python 中类的实例化过程，会首先寻找 metaclass，通过 metaclass 去创建 user 类
"""


class MetaClass(type):
    """继承 type 变成元类"""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class Base(metaclass=MetaClass):
    pass


class User:
    name = 'user'


def say(self):
    return 'say something'


user = type('User', (), {'name': 'user', 'say': say})
a = user()
print(type(a))  # <class '__main__.User'>
print(a.name)  # user
print(a.say())  # say something
