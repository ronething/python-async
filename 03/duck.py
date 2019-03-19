# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
鸭子类型
和 java 的多态不同
Cat Dog Duck 不需要继承 animal
直接 animal().say()
"""


class Cat(object):
    def say(self):
        print("cat")


class Dog(object):
    def say(self):
        print("dog")


class Duck(object):
    def say(self):
        print("duck")


animal = [Cat, Dog, Duck]
for i in animal:
    i().say()
