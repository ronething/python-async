# -*- coding:utf-8 _*-

__author__ = 'ronething'


class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v


user = User('panda')
print(user.name)
user.name = 'xzx'
print(user.name)